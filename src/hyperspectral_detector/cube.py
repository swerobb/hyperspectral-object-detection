import numpy as np
from PIL import Image

def x2cube(img, cell_size=4):
    """
    Convert a raw hyperspectral sensor mosiac into a spectral cube.

    A cell_size X cell_size block in the raw mosiac becomes one
    spatial pixel with cell_size * cell_size spectral channels.
    """

    block_size = [cell_size, cell_size]
    skip = [cell_size, cell_size]

    height, width = img.shape

    col_extent = width - block_size[1] + 1
    row_extent = height - block_size[0] + 1

    start_idx = (
        np.arange(block_size[0])[:, None] * width
        + np.arange(block_size[1])
    )

    didx = height * width * np.arange(1)

    start_idx = (
        didx[:, None] + start_idx.ravel()
    ).reshape((-1, block_size[0], block_size[1]))

    offset_idx = (
            np.arange(row_extent)[:, None] * width
            + np.arange(col_extent)
    )

    out = np.take(
        img,
        start_idx.ravel()[:, None]
        + offset_idx[::skip[0], ::skip[1]].ravel()
    )

    out = np.transpose(out)

    return out.reshape(
        height // cell_size,
        width // cell_size,
        cell_size * cell_size
    )


def load_hyperspectral_image(image_path):
    """
    Load a raw hyperspectral PNG and reconstruct its spectral cube.

    Returns:
        raw_image: original 2D sensor mosaic
        cube: reconstructed 3D hyperspectral cube
    """

    with Image.open(image_path) as image:
        raw_image = np.array(image)

    if raw_image.ndim != 2:
        raise ValueError(
            f"Expected a 2D sensor mosaic, received shape {raw_image.shape}"
        )

    cube = x2cube(raw_image)

    return raw_image, cube