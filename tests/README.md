# tests

## Overview

Unit tests for the `matplotlib_utilities` package, drawn non-interactively.

## Components

| Component | Description |
| --------- | ----------- |
| [conftest.py](./conftest.py) | Puts `src` on `sys.path`. |
| [test.py](./test.py) | Smoke tests of the maker. |
| [test_maker_usability.py](./test_maker_usability.py) | Default subplot index, layout validation and `finalize` cleanup. |
| [test_figure_helpers.py](./test_figure_helpers.py) | Figure title, unused subplots and grid placement. |
| [test_keyword_arguments.py](./test_keyword_arguments.py) | Parameter dataclasses consistent with the TypedDicts their `to_dict` returns. |
| [test_bar.py](./test_bar.py) | Vertical bars. |
| [test_barh_and_font.py](./test_barh_and_font.py) | Horizontal bars, ticks and the Japanese font family. |
| [test_series_shapes.py](./test_series_shapes.py) | Step, error bar, filled-area and stacked-area plots. |
| [test_distribution.py](./test_distribution.py) | Histograms, box and violin plots, and 2-D binning. |
| [test_pie.py](./test_pie.py) | Pie charts and wedge styling. |
| [test_colorbar_and_line_styles.py](./test_colorbar_and_line_styles.py) | Colorbars, line styles and level validation. |
| [test_grid_values.py](./test_grid_values.py) | Contours, pseudocolor meshes, streamlines, image scatter and spans. |
| [test_readme_figures.py](./test_readme_figures.py) | Example figures of the drawing methods, and their regeneration. |
| [test_readme_axis_figures.py](./test_readme_axis_figures.py) | Example figures of the axis methods, and their regeneration. |
