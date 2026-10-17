import matplotlib.pyplot as plt
import matplotlib.patches as patches


def plot_spectral_band(
    band,
    annotations,
    channel_index,
    colormap="viridis"
):
    """
    Create a visualization of one spectral band with
    ground-truth bounding boxes and class labels.
    """

    fig, ax = plt.subplots()

    image_display = ax.imshow(
        band,
        cmap=colormap
    )

    for annotation in annotations:
        xmin = annotation["xmin"]
        ymin = annotation["ymin"]
        xmax = annotation["xmax"]
        ymax = annotation["ymax"]

        width = xmax - xmin
        height = ymax - ymin

        rectangle = patches.Rectangle(
            (xmin, ymin),
            width,
            height,
            fill=False,
            edgecolor="red",
            linewidth=2
        )

        ax.add_patch(rectangle)

        ax.text(
            xmin,
            ymin,
            annotation["label"],
            color="red"
        )

    ax.set_title(
        f"Spectral channel {channel_index} with bounding boxes"
    )

    fig.colorbar(
        image_display,
        ax=ax,
        label="Sensor measurement"
    )

    return fig