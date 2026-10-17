import xml.etree.ElementTree as ET


def load_annotations(annotation_path):
    """
    Load object labels and bounding boxes from an XML annotation file.

    Returns a list of dictionaries.
    """

    tree = ET.parse(annotation_path)
    root = tree.getroot()

    annotations = []

    for obj in root.findall("object"):
        label = obj.findtext("name")

        box = obj.find("bndbox")

        xmin = int(box.findtext("xmin"))
        ymin = int(box.findtext("ymin"))
        xmax = int(box.findtext("xmax"))
        ymax = int(box.findtext("ymax"))

        annotations.append(
            {
                "label": label,
                "xmin": xmin,
                "ymin": ymin,
                "xmax": xmax,
                "ymax": ymax,
            }
        )

    return annotations