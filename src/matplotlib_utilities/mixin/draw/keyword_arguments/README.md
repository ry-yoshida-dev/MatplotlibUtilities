# keyword_arguments

## Overview

TypedDicts describing the keyword arguments each draw parameter dataclass produces. `to_dict` returns them, so mypy and basedpyright check every unpacked argument against the Matplotlib signature. Keys must match the dataclass fields; `tests/test_keyword_arguments.py` enforces this.

## Components

| Path | Description |
| ---- | ----------- |
| [`annotate.py`](./annotate.py) | `AnnotateKeywordArguments` — keys of `AnnotateParameters.to_dict` |
| [`arrow.py`](./arrow.py) | `ArrowKeywordArguments` — keys of `ArrowParameters.to_dict` |
| [`arrow_properties.py`](./arrow_properties.py) | `ArrowPropertiesKeywordArguments` — keys of `ArrowProperties.to_dict` |
| [`bar.py`](./bar.py) | `BarKeywordArguments` — keys of `BarParameters.to_dict` |
| [`barh.py`](./barh.py) | `BarhKeywordArguments` — keys of `BarhParameters.to_dict` |
| [`boxplot.py`](./boxplot.py) | `BoxplotKeywordArguments` — keys of `BoxplotParameters.to_dict` |
| [`colorbar.py`](./colorbar.py) | `ColorbarKeywordArguments` — keys of `ColorbarParameters.colorbar_keyword_arguments` |
| [`contour.py`](./contour.py) | `ContourKeywordArguments` — keys of `ContourParameters.to_dict` |
| [`contourf.py`](./contourf.py) | `ContourfKeywordArguments` — keys of `ContourfParameters.to_dict` |
| [`errorbar.py`](./errorbar.py) | `ErrorbarKeywordArguments` — keys of `ErrorbarParameters.to_dict` |
| [`fill_between.py`](./fill_between.py) | `FillBetweenKeywordArguments` — keys of `FillBetweenParameters.to_dict` |
| [`hexbin.py`](./hexbin.py) | `HexbinKeywordArguments` — keys of `HexbinParameters.to_dict` |
| [`hist.py`](./hist.py) | `HistKeywordArguments` — keys of `HistParameters.to_dict` |
| [`hist2d.py`](./hist2d.py) | `Hist2dKeywordArguments` — keys of `Hist2dParameters.to_dict` |
| [`imshow.py`](./imshow.py) | `ImshowKeywordArguments` — keys of `ImshowParameters.to_dict` |
| [`legend.py`](./legend.py) | `LegendKeywordArguments` — keys of `LegendParameters.to_dict` |
| [`line.py`](./line.py) | `LineKeywordArguments` — keys of `LineParameters.to_dict` |
| [`pcolormesh.py`](./pcolormesh.py) | `PcolormeshKeywordArguments` — keys of `PcolormeshParameters.to_dict` |
| [`pie.py`](./pie.py) | `PieKeywordArguments` — keys of `PieParameters.to_dict` |
| [`plot.py`](./plot.py) | `PlotKeywordArguments` — keys of `PlotParameters.to_dict` |
| [`quiver.py`](./quiver.py) | `QuiverKeywordArguments` — keys of `QuiverParameters.to_dict` |
| [`scatter.py`](./scatter.py) | `ScatterKeywordArguments` — keys of `ScatterParameters.to_dict` |
| [`span.py`](./span.py) | `SpanKeywordArguments` — keys of `SpanParameters.to_dict` |
| [`stackplot.py`](./stackplot.py) | `StackplotKeywordArguments` — keys of `StackplotParameters.to_dict` |
| [`step.py`](./step.py) | `StepKeywordArguments` — keys of `StepParameters.to_dict` |
| [`streamplot.py`](./streamplot.py) | `StreamplotKeywordArguments` — keys of `StreamplotParameters.to_dict` |
| [`violinplot.py`](./violinplot.py) | `ViolinplotKeywordArguments` — keys of `ViolinplotParameters.to_dict` |
| [`wedge_style.py`](./wedge_style.py) | `WedgeStyleKeywordArguments` — keys of `WedgeStyle.to_dict` |
