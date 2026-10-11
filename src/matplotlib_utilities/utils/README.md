# `utils` — shared types

Small **enums**, **type aliases**, and **subplot index** types used by `mixin.draw.parameters`, `mixin.axis` helpers, and `MatplotGraphMaker`. Most symbols are also re-exported from the package root (`matplotlib_utilities`).

## By topic

| Topic | Location | Role |
| ----- | -------- | ---- |
| Subplot addressing | [`index/`](./index/README.md) | `SubplotIndex`, `RowColumnIndex` |
| Markers | [`marker.py`](./marker.py) | `Marker` enum (Matplotlib marker strings) |
| Colormaps & colors | [`color/`](./color/) | `ColorMap`; palette types from `color` + Matplotlib/numpy shims |
| Layout / axes (enums) | [`../graph_axis.py`](../graph_axis.py); [`table_axis.py`](./table_axis.py), [`grid.py`](./grid.py) | `GraphAxis` lives at package root; `TableAxis` (row/column layout), `GridWhich` / `GridAxis` (`Axes.grid` kwargs) |
| Imshow / colorbar / lines | top-level `*.py` | `Aspect`, `Origin`, `InterpolationMethod`, `InterpolationStage`, `ColorbarExtend`, `ColorbarSpacing`, … |
| Lines, arrows, layout hints | [`linestyle.py`](./linestyle.py), [`arrow_shape.py`](./arrow_shape.py), [`arrow_style.py`](./arrow_style.py), [`orientation.py`](./orientation.py), [`location.py`](./location.py), [`legend_location.py`](./legend_location.py) | Kwargs-friendly enums |
| Line ends, bars, fills | [`cap_style.py`](./cap_style.py), [`join_style.py`](./join_style.py), [`draw_style.py`](./draw_style.py), [`bar_align.py`](./bar_align.py), [`hatch.py`](./hatch.py) | Enums for `plot`, `bar` / `barh`, `fill_between` / `span` / `contourf` |
| Text and annotations | [`font_size.py`](./font_size.py), [`font_weight.py`](./font_weight.py), [`horizontal_alignment.py`](./horizontal_alignment.py), [`vertical_alignment.py`](./vertical_alignment.py), [`rotation_mode.py`](./rotation_mode.py), [`coordinate_system.py`](./coordinate_system.py) | Enums for `annotate` and `legend` |
| Enum base | [`keyword_enum.py`](./keyword_enum.py) | `KeywordEnum` — base of every string enum passed to Matplotlib |
| Distributions, areas, grids, fields | [`hist_type.py`](./hist_type.py), [`bandwidth_method.py`](./bandwidth_method.py), [`step_where.py`](./step_where.py), [`stack_baseline.py`](./stack_baseline.py), [`shading.py`](./shading.py), [`integration_direction.py`](./integration_direction.py) | Enums for `hist`, `violinplot`, `step` / `fill_between`, `stackplot`, `pcolormesh`, `streamplot` |

## Exports (`utils.__all__`)

| Name | Kind | Summary |
| ---- | ---- | ------- |
| `SubplotIndex` | Type alias | `RowColumnIndex \| int` — see [`index/subplot_index.py`](./index/subplot_index.py) |
| `RowColumnIndex` | Dataclass | Zero-based `(row_index, column_index)` |
| `GraphAxis` | Enum | X/Y axis for labels and limits (`AxisMixin`) |
| `TableAxis` | Enum | Row/column when building `GraphLayout` |
| `GridWhich`, `GridAxis` | Enum | `Axes.grid` `which` / `axis` kwargs (`GridParameters`) |
| `Marker` | Enum | Scatter/plot marker styles |
| `ColorMap` | Enum | Named colormaps — [`color/color_map.py`](./color/color_map.py) |
| `ColorType`, `HexType`, `HsvFloatType`, `RgbFloatType`, `RgbIntType`, `RgbaIntType` | Type aliases | From the `color` package |
| `MplColor` | Type alias | `matplotlib.typing.ColorType` — a name, a hex string, or an RGB(A) tuple of floats in 0–1 |
| `ScatterColorArg` | Type alias | `MplColor` or per-point `ArrayLike` for scatter `c` |
| `Aspect` | Enum | Axes aspect modes |
| `Origin` | Enum | `imshow` origin |
| `InterpolationMethod`, `InterpolationStage` | Enums | `imshow` interpolation |
| `Location` | Enum | Side of the subplot a colorbar is attached to |
| `Orientation` | Enum | Horizontal vs vertical (`line`, `span`, `hist`, `boxplot`, …) |
| `ArrowShape` | Enum | `Axes.arrow` head shape (`full` / `left` / `right`) |
| `Linestyle` | Enum | Line dash patterns (strings or Matplotlib tuples) |
| `ColorbarExtend` | Enum | Colorbar over/under extension |
| `ColorbarSpacing` | Enum | Colorbar tick spacing style |
| `HistType` | Enum | `hist` drawing style (`bar`, `barstacked`, `step`, `stepfilled`) |
| `BandwidthMethod` | Enum | `violinplot` kernel bandwidth rule (`scott`, `silverman`) |
| `StepWhere` | Enum | Where a step changes level (`pre`, `post`, `mid`) |
| `StackBaseline` | Enum | `stackplot` baseline (`zero`, `sym`, `wiggle`, `weighted_wiggle`) |
| `Shading` | Enum | `pcolormesh` cell fill (`flat`, `nearest`, `gouraud`, `auto`) |
| `IntegrationDirection` | Enum | `streamplot` tracing direction (`forward`, `backward`, `both`) |
| `KeywordEnum` | Enum base | Declares `str` member values so type checkers see what reaches Matplotlib |
| `LegendLocation` | Enum | Legend placement inside the subplot (`best`, `upper right`, …) |
| `ArrowStyle` | Enum | Arrow shape for annotations and `streamplot` (`->`, `-|>`, `fancy`, …) |
| `CapStyle`, `JoinStyle` | Enums | Line end and corner drawing for `plot` / `step` |
| `DrawStyle` | Enum | How `plot` connects points (`default`, `steps-pre`, …) |
| `BarAlign` | Enum | Bar placement against its position (`center`, `edge`) |
| `Hatch` | Enum | Fill pattern for `fill_between`, `span`, `contourf` |
| `CoordinateSystem` | Enum | Coordinates of an annotation point or text (`data`, `axes fraction`, `offset points`, …) |
| `FontSize`, `FontWeight` | Enums | Named text size and weight |
| `HorizontalAlignment`, `VerticalAlignment`, `RotationMode` | Enums | Text alignment and rotation for `annotate` |

## On-disk layout

| Path | Notes |
| ---- | ----- |
| [`index/`](./index/) | Subplot indices; [detailed README](./index/README.md) |
| [`color/`](./color/) | `color_map.py`, `color_types.py` |
| [`colorbar/`](./colorbar/) | `extend.py`, `spacing.py` |
| [`interpolation/`](./interpolation/) | `method.py`, `stage.py` |
| `../graph_axis.py`, `table_axis.py`, `grid.py` | Axis-related enums (distinct roles; see table above) |
| `aspect.py`, `origin.py`, `location.py`, `legend_location.py`, `orientation.py`, `linestyle.py`, `arrow_shape.py`, `arrow_style.py`, `marker.py`, `hist_type.py`, `bandwidth_method.py`, `step_where.py`, `stack_baseline.py`, `shading.py`, `integration_direction.py`, `cap_style.py`, `join_style.py`, `draw_style.py`, `bar_align.py`, `hatch.py`, `coordinate_system.py`, `font_size.py`, `font_weight.py`, `horizontal_alignment.py`, `vertical_alignment.py`, `rotation_mode.py`, `keyword_enum.py` | One enum (or small helper) per module |

Authoritative list: [`__init__.py`](./__init__.py). Package overview: [../README.md](../README.md).
