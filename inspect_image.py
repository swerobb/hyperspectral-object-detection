from pathlib import Path

import matplotlib.pyplot as plt

from hyperspectral_detector.annotations import load_annotations
from hyperspectral_detector.cube import load_hyperspectral_image
from hyperspectral_detector.visualization import plot_spectral_band


# Find the folder containing this Python script.
project_dir = Path(__file__).resolve().parent


# Build the path to the training VIS images.
image_dir = (
    project_dir
    / "data"
    / "hyperspectral-object-detection-challenge-2026"
    / "data_train"
    / "data_train"
    / "VIS"
)


# Find PNG images and sort them by filename.
image_paths = sorted(image_dir.glob("*.png"))


# Stop if no PNG images are found.
if not image_paths:
    raise FileNotFoundError(
        f"No images found in: {image_dir}"
    )


# Select the first image for inspection.
image_path = image_paths[0]


# Find the annotation folder.
annotation_dir = (
    image_dir.parent
    / "Annotations"
    / "VIS"
)


# Build the matching XML annotation path.
annotation_path = (
    annotation_dir
    / image_path.with_suffix(".xml").name
)


print("Annotation path:", annotation_path)
print("Annotation exists:", annotation_path.is_file())


# Load annotations from the XML file.
annotations = load_annotations(annotation_path)

print("Labeled objects:", len(annotations))

for annotation in annotations:
    print("Object:", annotation["label"])
    print(
        "Bounding box:",
        annotation["xmin"],
        annotation["ymin"],
        annotation["xmax"],
        annotation["ymax"]
    )


# Load the raw sensor image and reconstruct the hyperspectral cube.
raw_image, cube = load_hyperspectral_image(image_path)


# Print image information.
print("\nProject directory:", project_dir)

print("\nImage folder exists:", image_dir.is_dir())

print("\nSelected image:", image_path.name)

print("Raw image shape:", raw_image.shape)

print("\nData type:", raw_image.dtype)

print("\nLowest measurement:", raw_image.min())

print("\nHighest measurement:", raw_image.max())

print("\nSpectral cube shape:", cube.shape)


# Select one spectral channel.
channel_index = 8

band = cube[:, :, channel_index]

print("Band shape:", band.shape)


# Create the visualization.
fig = plot_spectral_band(
    band,
    annotations,
    channel_index
)


# Display the figure.
plt.show()