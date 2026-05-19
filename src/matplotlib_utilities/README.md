# matplotlib_utilities

## Overview

| Layer | Types | Role |
| ----- | ----- | ---- |
| Layout | `GraphLayout`, `TableAxis` | Subplot grid; helpers to build layout from a count |
| Global style | `GraphParameters` | Font, spacing, DPI, figure size |
| Per-plot kwargs | `*Parameters` dataclasses | Typed kwargs → `to_dict` for Matplotlib |
| Coordinator | `MatplotGraphMaker` | Builds `Figure` / `Axes`; drawing methods on the maker; see **`axis`** below |

**Mixin API:** [`mixin/`](./mixin/) — `DrawMixin` and `AxisMixin` on `MatplotGraphMaker` (e.g. `maker.scatter`, `maker.set_label`). Draw examples: [`mixin/draw/README.md`](./mixin/draw/README.md).

Exported names: [`__init__.py`](./__init__.py). Utilities and subplot index types: [`utils/README.md`](./utils/README.md).

## `MatplotGraphMaker` (cheat sheet)

| Attribute | Role |
| --------- | ---- |
| `layout`, `parameters` | Grid + figure defaults (applied when the figure is created) |
| `fig`, `ax` | Raw Matplotlib objects (`ax` is 2D, `squeeze=False`) |
| `axis` | Axis helpers; drawing uses flat methods on the maker (`scatter`, `plot`, …) |

| Method | Role |
| ------ | ---- |
| `access_subplot(index)` | `Axes` for a `SubplotIndex` |
| `get_subplot_index_from_number` / `..._row_column` | Build indices |
| `finalize(...)` | `subplots_adjust`, optional save / show / close |

## Layout and indices (minimal)

| Type | Note |
| ---- | ---- |
| `GraphLayout` | `number`, `row`, `column`; factories in [`layout.py`](./layout.py) |
| `SubplotIndex` | `RowColumnIndex` or `SubplotNumber` — see [`utils/index`](./utils/index/subplot_index.py) |
| `GraphAxis` | `X` / `Y` for axis helpers — [`graph_axis.py`](./graph_axis.py) |

## Components

| Path | Contents |
| ---- | -------- |
| [`maker.py`](./maker.py) | `MatplotGraphMaker` |
| [`layout.py`](./layout.py); enums in [`utils/table_axis.py`](./utils/table_axis.py), [`graph_axis.py`](./graph_axis.py) | Layout / table vs graph axis |
| [`parameter.py`](./parameter.py), [`subparameter.py`](./subparameter.py) | `GraphParameters`, `Subparameters` base |
| [`mixin/`](./mixin/) | `DrawMixin`, `AxisMixin`, and per-feature `*Parameters` — see [`mixin/README.md`](./mixin/README.md) |

Install and a short example: [../../README.md](../../README.md).
