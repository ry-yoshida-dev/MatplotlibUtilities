# base

## Overview

Dataclasses holding fields shared by several draw parameters. They are combined by multiple inheritance and validate their own fields in `__post_init__`.

## Components

| Path | Description |
| ---- | ----------- |
| [`artist.py`](./artist.py) | `ArtistParameters` — common artist kwargs shared by many matplotlib draw calls |
| [`cmap.py`](./cmap.py) | `CmapParameters` — colormap scaling (cmap, vmin, vmax) |
| [`color.py`](./color.py) | `ColorParameters` — base color parameters shared by patch-like artists |
| [`contour_level.py`](./contour_level.py) | `ContourLevelParameters` — level and coloring options shared by line and filled contours |
| [`label.py`](./label.py) | `LabelParameters` — common label keyword argument for matplotlib artists and related API |
| [`line.py`](./line.py) | `LineStyleParameters` — common line-like kwargs shared by line and plot style artists |
| [`marker_line.py`](./marker_line.py) | `MarkerLineParameters` — marker and line-end options shared by line plots and step plots |
| [`norm.py`](./norm.py) | `NormParameters` — colormap scaling that also accepts an explicit normalization |
