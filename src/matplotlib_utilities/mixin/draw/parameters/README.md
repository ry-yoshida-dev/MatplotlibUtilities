# parameters

## Overview

Frozen parameter dataclasses for each draw helper. Most derive from `KeywordSubparameters` and unpack into the Matplotlib call through `to_dict`; shared fields live in [`base/`](./base/).

## Components

| Path | Description |
| ---- | ----------- |
| [`base/`](./base/) | Mixin dataclasses with fields shared across parameters |
| [`annotate.py`](./annotate.py) | `AnnotateParameters` — keyword arguments for matplotlib.axes.Axes.annotate |
| [`arrow.py`](./arrow.py) | `ArrowParameters` — keyword arguments for matplotlib.axes.Axes.arrow |
| [`arrow_properties.py`](./arrow_properties.py) | `ArrowProperties` — arrow drawn by an annotation, passed to Matplotlib as arrowprops |
| [`bar.py`](./bar.py) | `BarParameters` — bar plot |
| [`barh.py`](./barh.py) | `BarhParameters` — horizontal bar plot |
| [`boxplot.py`](./boxplot.py) | `BoxplotParameters` — box plot |
| [`colorbar.py`](./colorbar.py) | `ColorbarParameters` — colorbar |
| [`contour.py`](./contour.py) | `ContourParameters` — contour line plot |
| [`contourf.py`](./contourf.py) | `ContourfParameters` — filled contour plot |
| [`errorbar.py`](./errorbar.py) | `ErrorbarParameters` — error bar plot |
| [`fill_between.py`](./fill_between.py) | `FillBetweenParameters` — area filled between two curves |
| [`hexbin.py`](./hexbin.py) | `HexbinParameters` — hexagonal binning plot |
| [`hist.py`](./hist.py) | `HistParameters` — histogram |
| [`hist2d.py`](./hist2d.py) | `Hist2dParameters` — two-dimensional histogram |
| [`imscatter.py`](./imscatter.py) | `ImscatterParameters` — image scatter plot |
| [`imshow.py`](./imshow.py) | `ImshowParameters` — imshow plot |
| [`legend.py`](./legend.py) | `LegendParameters` — legend |
| [`line.py`](./line.py) | `LineParameters` — line |
| [`pcolormesh.py`](./pcolormesh.py) | `PcolormeshParameters` — pseudocolor mesh |
| [`pie.py`](./pie.py) | `PieParameters` — pie chart |
| [`plot.py`](./plot.py) | `PlotParameters` — plot |
| [`quiver.py`](./quiver.py) | `QuiverParameters` — `matplotlib.axes.Axes.quiver` |
| [`scatter.py`](./scatter.py) | `ScatterParameters` — scatter plot |
| [`span.py`](./span.py) | `SpanParameters` — a shaded band across the subplot |
| [`stackplot.py`](./stackplot.py) | `StackplotParameters` — stacked area plot |
| [`step.py`](./step.py) | `StepParameters` — step plot |
| [`streamplot.py`](./streamplot.py) | `StreamplotParameters` — streamline plot |
| [`violinplot.py`](./violinplot.py) | `ViolinplotParameters` — violin plot |
| [`wedge_style.py`](./wedge_style.py) | `WedgeStyle` — styling applied to every wedge of a pie chart (matplotlib wedgeprops) |
