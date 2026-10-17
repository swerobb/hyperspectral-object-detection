import numpy as np

from hyperspectral_detector.cube import x2cube

def test_x2cube_converts_4x4_mosaic_to_16_channels():
    raw_image = np.arange(16).reshape(4,4)

    cube = x2cube(raw_image)

    assert cube.shape == (1, 1, 16)

    expected_spectrum = np.arange(16)

    np.testing.assert_array_equal(
        cube[0, 0],
        expected_spectrum
    )