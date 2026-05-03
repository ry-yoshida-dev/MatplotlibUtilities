# `utils` — shared types

Small **enums**, **type aliases**, and **subplot index** types used by `mixin.draw.parameters`, `mixin.axis` helpers, and `MatplotGraphMaker`. Most symbols are also re-exported from the package root (`matplotlib_utilities`).

## By topic

| Topic | Location | Role |
| ----- | -------- | ---- |
| Subplot addressing | [`index/`](./index/README.md) | `SubplotIndex`, `RowColumnIndex`, `SubplotNumber` |
| Markers | [`marker.py`](./marker.py) | `Marker` enum (Matplotlib marker strings) |
| Colormaps & colors | [`color/`](./color/) | `ColorMap`; palette types from `color` + Matplotlib/numpy shims |
| Layout / axes (enums) | [`../graph_axis.py`](../graph_axis.py); [`table_axis.py`](./table_axis.py), [`grid.py`](./grid.py) | `GraphAxis` lives at package root; `TableAxis` (row/column layout), `GridWhich` / `GridAxis` (`Axes.grid` kwargs) |
| Imshow / colorbar / lines | top-level `*.py` | `Aspect`, `Origin`, `InterpolationMethod`, `InterpolationStage`, `ColorbarExtend`, `ColorbarSpacing`, … |
| Lines, arrows, layout hints | [`linestyle.py`](./linestyle.py), [`arrow_shape.py`](./arrow_shape.py), [`orientation.py`](./orientation.py), [`location.py`](./location.py) | Kwargs-friendly enums |

## Exports (`utils.__all__`)

| Name | Kind | Summary |
| ---- | ---- | ------- |
| `SubplotIndex` | Type alias | `RowColumnIndex \| SubplotNumber` — see [`index/subplot_index.py`](./index/subplot_index.py) |
| `RowColumnIndex` | Dataclass | Zero-based `(row_index, column_index)` |
| `SubplotNumber` | Dataclass | Linear subplot index with row hint — [`index/subplot_number.py`](./index/subplot_number.py) |
| `GraphAxis` | Enum | X/Y axis for labels and limits (`AxisMixin`) |
| `TableAxis` | Enum | Row/column when building `GraphLayout` |
| `GridWhich`, `GridAxis` | Enum | `Axes.grid` `which` / `axis` kwargs (`GridParameters`) |
| `Marker` | Enum | Scatter/plot marker styles |
| `ColorMap` | Enum | Named colormaps — [`color/color_map.py`](./color/color_map.py) |
| `ColorType`, `HexType`, `HsvFloatType`, `RgbFloatType`, `RgbIntType`, `RgbaIntType` | Type aliases | From the `color` package |
| `MplColor` | Type alias | `color.ColorType \| matplotlib.typing.ColorType` |
| `ScatterColorArg` | Type alias | Single colors or per-point `ArrayLike` for scatter `c` |
| `Aspect` | Enum | Axes aspect modes |
| `Origin` | Enum | `imshow` origin |
| `InterpolationMethod`, `InterpolationStage` | Enums | `imshow` interpolation |
| `Location` | Enum | Legend (and similar) placement |
| `Orientation` | Enum | Horizontal vs vertical (`line`, etc.) |
| `ArrowShape` | Enum | `Axes.arrow` head shape (`full` / `left` / `right`) |
| `Linestyle` | Enum | Line dash patterns (strings or Matplotlib tuples) |
| `ColorbarExtend` | Enum | Colorbar over/under extension |
| `ColorbarSpacing` | Enum | Colorbar tick spacing style |

## On-disk layout

| Path | Notes |
| ---- | ----- |
| [`index/`](./index/) | Subplot indices; [detailed README](./index/README.md) |
| [`color/`](./color/) | `color_map.py`, `color_types.py` |
| [`colorbar/`](./colorbar/) | `extend.py`, `spacing.py` |
| [`interpolation/`](./interpolation/) | `method.py`, `stage.py` |
| `../graph_axis.py`, `table_axis.py`, `grid.py` | Axis-related enums (distinct roles; see table above) |
| `aspect.py`, `origin.py`, `location.py`, `orientation.py`, `linestyle.py`, `arrow_shape.py`, `marker.py` | One enum (or small helper) per module |

Authoritative list: [`__init__.py`](./__init__.py). Package overview: [../README.md](../README.md).
