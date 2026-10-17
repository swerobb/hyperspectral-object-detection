from hyperspectral_detector.annotations import load_annotations


def test_load_annotations_reads_label_and_bbox(tmp_path):
    xml_content = """
    <annotation>
        <object>
            <name>rubik</name>
            <bndbox>
                <xmin>226</xmin>
                <ymin>26</ymin>
                <xmax>265</xmax>
                <ymax>66</ymax>
            </bndbox>
        </object>
    </annotation>
    """

    xml_path = tmp_path / "test.xml"

    xml_path.write_text(xml_content)

    annotations = load_annotations(xml_path)

    assert len(annotations) == 1
    assert annotations[0]["label"] == "rubik"
    assert annotations[0]["xmin"] == 226
    assert annotations[0]["ymin"] == 26
    assert annotations[0]["xmax"] == 265
    assert annotations[0]["ymax"] == 66