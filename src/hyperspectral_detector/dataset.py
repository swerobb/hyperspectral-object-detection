from pathlib import Path
import xml.etree.ElementTree as ET
from collections import Counter


def find_unmatched_files(image_dir, annotation_dir):
    """
    Find PNG images without matching XML annotations
    and XML annotations without matching PNG images.
    """

    image_paths = sorted(Path(image_dir).glob("*.png"))
    annotation_paths = sorted(Path(annotation_dir).glob("*.xml"))

    image_names = {path.stem for path in image_paths}
    annotation_names = {path.stem for path in annotation_paths}

    images_without_annotations = image_names - annotation_names
    annotations_without_images = annotation_names - image_names

    return images_without_annotations, annotations_without_images


def summarize_dataset(image_dir, annotation_dir):
    """
    Calculate dataset statistics using only matched image/XML pairs.
    """

    image_paths = sorted(Path(image_dir).glob("*.png"))
    annotation_paths = sorted(Path(annotation_dir).glob("*.xml"))

    image_names = {path.stem for path in image_paths}

    matched_annotation_paths = [
        path
        for path in annotation_paths
        if path.stem in image_names
    ]

    class_counts = Counter()
    class_image_counts = Counter()
    total_objects = 0

    for annotation_path in matched_annotation_paths:
        tree = ET.parse(annotation_path)
        root = tree.getroot()

        objects = root.findall("object")

        classes_in_this_image = set()

        for obj in objects:
            class_name = obj.findtext("name")

            class_counts[class_name] += 1
            total_objects += 1

            classes_in_this_image.add(class_name)

        for class_name in classes_in_this_image:
            class_image_counts[class_name] += 1

    return {
        "total_images": len(image_paths),
        "total_annotations": len(annotation_paths),
        "usable_pairs": len(matched_annotation_paths),
        "total_objects": total_objects,
        "class_counts": class_counts,
        "class_image_counts": class_image_counts,
    }