# matplotlib_utilities

## Overview

`MatplotGraphMaker` and what it is built from: the subplot layout, figure-wide `GraphParameters`, the frozen parameter base classes, and the drawing and axis mixins. Public names are re-exported from the package root.

## Components

| Component | Description |
| --------- | ----------- |
| [`maker.py`](./maker.py) | `MatplotGraphMaker`, which creates the figure and subplots and finalizes them |
| [`layout.py`](./layout.py) | `GraphLayout`, the number of subplots and their rows and columns |
| [`parameter.py`](./parameter.py) | `GraphParameters`, figure-wide font, spacing, DPI and size |
| [`subparameter.py`](./subparameter.py) | `Subparameters`, the frozen base of parameter dataclasses, with `rebuild` |
| [`keyword_subparameter.py`](./keyword_subparameter.py) | `KeywordSubparameters`, parameters unpacked into Matplotlib through a typed `to_dict` |
| [`font_family.py`](./font_family.py) | `FontFamily`, the font family a figure is drawn in, including a Japanese one |
| [`graph_axis.py`](./graph_axis.py) | `GraphAxis`, the x or y axis of a subplot |
| [`protocols.py`](./protocols.py) | `MakerCanvas`, the structural type of the maker the mixins draw on |
| [`types/`](./types/README.md) | Shared type aliases |
| [`mixin/`](./mixin/README.md) | Drawing and axis methods of `MatplotGraphMaker` and their parameters |
| [`utils/`](./utils/README.md) | Enums, color types and subplot indices used in parameters |
