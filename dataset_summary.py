from pathlib import Path

from hyperspectral_detector.dataset import (
    find_unmatched_files,
    summarize_dataset,
)


# Find the folder containing this script.
project_dir = Path(__file__).resolve().parent


# Path to the VIS training images.
image_dir = (
    project_dir
    / "data"
    / "hyperspectral-object-detection-challenge-2026"
    / "data_train"
    / "data_train"
    / "VIS"
)


# Path to the VIS annotation files.
annotation_dir = (
    project_dir
    / "data"
    / "hyperspectral-object-detection-challenge-2026"
    / "data_train"
    / "data_train"
    / "Annotations"
    / "VIS"
)


# Check for unmatched files.
images_without_annotations, annotations_without_images = find_unmatched_files(
    image_dir,
    annotation_dir
)


print("Images without matching annotations:")
for name in sorted(images_without_annotations):
    print(name)


print("\nAnnotations without matching images:")
for name in sorted(annotations_without_images):
    print(name)


# Calculate dataset statistics.
summary = summarize_dataset(
    image_dir,
    annotation_dir
)


# Print overall statistics.
print("\nTotal images:", summary["total_images"])
print("Total annotation files:", summary["total_annotations"])
print("Usable image/annotation pairs:", summary["usable_pairs"])
print("Total usable labeled objects:", summary["total_objects"])


# Print object counts for each class.
print("\nClasses:")
for class_name, count in summary["class_counts"].items():
    print(f"{class_name}: {count}")


# Print how many images contain each class.
print("\nImages containing each class:")
for class_name, count in summary["class_image_counts"].items():
    print(f"{class_name}: {count}")