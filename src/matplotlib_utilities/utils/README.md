# utils

## Overview

Enums, color types and subplot indices that parameters and maker methods take. Each enum lists the values one Matplotlib keyword argument accepts, so finite choices are never passed as bare strings. Public names are re-exported from the package root.

## Components

| Component | Description |
| --------- | ----------- |
| [`keyword_enum.py`](./keyword_enum.py) | `KeywordEnum`, the base of every string enum passed to Matplotlib |
| [`index/`](./index/README.md) | `SubplotIndex` and `RowColumnIndex`, which address a subplot |
| [`table_axis.py`](./table_axis.py) | `TableAxis`, rows or columns when building a `GraphLayout` |
| [`grid.py`](./grid.py) | `GridWhich` and `GridAxis`, which grid lines `set_grid` affects |
| [`color/`](./color/README.md) | `ColorMap` and the color types parameters take |
| [`colorbar/`](./colorbar/README.md) | Colorbar extension and spacing |
| [`interpolation/`](./interpolation/README.md) | `imshow` interpolation method and stage |
| [`quiver/`](./quiver/README.md) | `quiver` angles, pivot and units |
| [`aspect.py`](./aspect.py) | `Aspect`, the aspect ratio of `imshow` |
| [`origin.py`](./origin.py) | `Origin`, the corner `imshow` places index `[0, 0]` in |
| [`location.py`](./location.py) | `Location`, the side of a subplot a colorbar is attached to |
| [`orientation.py`](./orientation.py) | `Orientation`, horizontal or vertical |
| [`legend_location.py`](./legend_location.py) | `LegendLocation`, where a legend is placed inside its subplot |
| [`marker.py`](./marker.py) | `Marker`, marker styles |
| [`linestyle.py`](./linestyle.py) | `Linestyle`, line dash patterns |
| [`cap_style.py`](./cap_style.py) | `CapStyle`, how the ends of a solid line are drawn |
| [`join_style.py`](./join_style.py) | `JoinStyle`, how the corners of a solid line are drawn |
| [`draw_style.py`](./draw_style.py) | `DrawStyle`, how the points of a line plot are connected |
| [`bar_align.py`](./bar_align.py) | `BarAlign`, where a bar sits relative to its position |
| [`hatch.py`](./hatch.py) | `Hatch`, the pattern drawn inside a filled area |
| [`hist_type.py`](./hist_type.py) | `HistType`, the drawing style of a histogram |
| [`bandwidth_method.py`](./bandwidth_method.py) | `BandwidthMethod`, the kernel density bandwidth rule of a violin plot |
| [`step_where.py`](./step_where.py) | `StepWhere`, where each step of a step plot changes level |
| [`stack_baseline.py`](./stack_baseline.py) | `StackBaseline`, the baseline of a stacked area plot |
| [`shading.py`](./shading.py) | `Shading`, the fill style of a pseudocolor mesh |
| [`integration_direction.py`](./integration_direction.py) | `IntegrationDirection`, the direction streamlines are traced in |
| [`arrow_shape.py`](./arrow_shape.py) | `ArrowShape`, the head shape of `arrow` |
| [`arrow_style.py`](./arrow_style.py) | `ArrowStyle`, the arrow drawn by `annotate` and `streamplot` |
| [`coordinate_system.py`](./coordinate_system.py) | `CoordinateSystem`, the coordinates of an annotation point or its text |
| [`font_size.py`](./font_size.py) | `FontSize`, named font sizes |
| [`font_weight.py`](./font_weight.py) | `FontWeight`, named font weights |
| [`horizontal_alignment.py`](./horizontal_alignment.py) | `HorizontalAlignment`, which side of a text box sits at its x position |
| [`vertical_alignment.py`](./vertical_alignment.py) | `VerticalAlignment`, which part of a text box sits at its y position |
| [`rotation_mode.py`](./rotation_mode.py) | `RotationMode`, whether text is aligned before or after rotation |
