# Hyperspectral Object Detection

A portfolio project for exploring hyperspectral imagery and developing an object detection pipeline using 16-channel spectral data.

## Project Goals

- Reconstruct raw hyperspectral sensor mosaics into spectral cubes
- Parse and validate object annotations
- Analyze dataset class distributions
- Visualize spectral bands and bounding boxes
- Develop and evaluate object detection models

## Current Features

- Loads raw hyperspectral PNG sensor mosaics
- Reconstructs images into 16-channel hyperspectral cubes
- Parses XML annotations and bounding boxes
- Detects unmatched image and annotation files
- Calculates dataset statistics
- Visualizes spectral bands with ground-truth bounding boxes
- Includes automated tests using pytest

## Technologies

- Python
- NumPy
- Pillow
- Matplotlib
- XML
- pytest
- Git / GitHub

## Project Structure

```text
src/hyperspectral_detector/
├── annotations.py
├── cube.py
├── dataset.py
└── visualization.py

tests/
├── test_annotations.py
└── test_cube.py