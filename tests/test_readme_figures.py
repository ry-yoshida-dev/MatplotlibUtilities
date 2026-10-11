"""README figures under mixin/draw/readme_figures/.

Default pytest skips regeneration. Refresh assets:

    UPDATE_README_FIGURES=1 pytest tests/test_readme_figures.py -k update
"""

from __future__ import annotations

import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pytest
from PIL import Image

from matplotlib_utilities import (
    AnnotateParameters,
    ArrowProperties,
    ColorMap,
    BoxplotParameters,
    ContourfParameters,
    ContourParameters,
    ErrorbarParameters,
    FillBetweenParameters,
    HexbinParameters,
    Hist2dParameters,
    HistParameters,
    ImscatterParameters,
    Marker,
    PcolormeshParameters,
    Shading,
    SpanParameters,
    StackplotParameters,
    StepParameters,
    StepWhere,
    StreamplotParameters,
    ViolinplotParameters,
    ArrowParameters,
    BarhParameters,
    ColorbarParameters,
    GraphLayout,
    GraphParameters,
    ImshowParameters,
    LineParameters,
    MatplotGraphMaker,
    Orientation,
    PieParameters,
    PlotParameters,
    QuiverAngles,
    QuiverParameters,
    ScatterParameters,
    TableAxis,
    WedgeStyle,
)
from matplotlib_utilities.mixin.draw.parameters import BarParameters

DRAW_README = Path(__file__).resolve().parents[1] / "src/matplotlib_utilities/mixin/draw"
FIGURES_ROOT = DRAW_README / "readme_figures"

UPDATE = os.environ.get("UPDATE_README_FIGURES") == "1"

# README embeds: fixed canvas (400×250 px) matches width/height in mixin/draw/README.md.
README_GRAPH_PARAMETERS = GraphParameters(figsize=(4.0, 2.5), dpi=100, font_size=9)
README_FIGURE_SIZE = (
    int(README_GRAPH_PARAMETERS.figsize[0] * README_GRAPH_PARAMETERS.dpi),
    int(README_GRAPH_PARAMETERS.figsize[1] * README_GRAPH_PARAMETERS.dpi),
)

FIGURE_PATHS = [
    "image/imshow.png",
    "image/colorbar.png",
    "series/plot.png",
    "series/scatter.png",
    "series/bar.png",
    "series/barh.png",
    "proportion/pie.png",
    "vector/quiver.png",
    "vector/arrow.png",
    "misc/legend.png",
    "misc/line.png",
    "misc/annotate.png",
    "misc/span.png",
    "series/step.png",
    "series/errorbar.png",
    "series/fill_between.png",
    "series/stackplot.png",
    "distribution/hist.png",
    "distribution/boxplot.png",
    "distribution/violinplot.png",
    "distribution/hexbin.png",
    "distribution/hist2d.png",
    "image/contour.png",
    "image/contourf.png",
    "image/pcolormesh.png",
    "image/imscatter.png",
    "vector/streamplot.png",
]


def _maker() -> MatplotGraphMaker:
    layout = GraphLayout.from_number(number=1, axis=TableAxis.COLUMN, axis_value=1)
    return MatplotGraphMaker(layout=layout, parameters=README_GRAPH_PARAMETERS)


def _index(maker: MatplotGraphMaker):
    return maker.get_subplot_index_from_number(number=0)


def _save(maker: MatplotGraphMaker, rel_path: str) -> Path:
    """Save at fixed pixel size (no bbox_inches='tight') so README embeds align."""
    out = FIGURES_ROOT / rel_path
    out.parent.mkdir(parents=True, exist_ok=True)
    maker.fig.subplots_adjust(
        wspace=maker.parameters.w_space,
        hspace=maker.parameters.h_space,
    )
    maker.fig.savefig(str(out), dpi=maker.parameters.dpi)
    plt.close(maker.fig)
    return out


@pytest.mark.parametrize("rel_path", FIGURE_PATHS)
def test_readme_figure_committed(rel_path: str) -> None:
    path = FIGURES_ROOT / rel_path
    assert path.is_file(), f"missing {path}; run UPDATE_README_FIGURES=1 pytest -k update"
    assert path.stat().st_size > 0
    with Image.open(path) as image:
        assert image.size == README_FIGURE_SIZE, (
            f"{rel_path} is {image.size}, expected {README_FIGURE_SIZE}; "
            "run UPDATE_README_FIGURES=1 pytest -k update"
        )


@pytest.mark.skipif(not UPDATE, reason="set UPDATE_README_FIGURES=1 to regenerate PNGs")
class TestUpdateReadmeFigures:
    def test_imshow(self) -> None:
        maker = _maker()
        data = np.linspace(0, 1, 64 * 64).reshape(64, 64)
        maker.imshow(image=data, index=_index(maker), subparams=ImshowParameters())
        _save(maker, "image/imshow.png")

    def test_colorbar(self) -> None:
        maker = _maker()
        data = np.linspace(0, 1, 32 * 32).reshape(32, 32)
        idx = _index(maker)
        image = maker.imshow(image=data, index=idx, subparams=ImshowParameters())
        _ = maker.set_colorbar(
            index=idx,
            mappable=image,
            subparams=ColorbarParameters(label="value"),
        )
        _save(maker, "image/colorbar.png")

    def test_plot(self) -> None:
        maker = _maker()
        x = np.linspace(0, 2 * np.pi, 50)
        maker.plot(x=x, y=np.sin(x), index=_index(maker), subparams=PlotParameters())
        _save(maker, "series/plot.png")

    def test_scatter(self) -> None:
        maker = _maker()
        rng = np.random.default_rng(0)
        x = rng.standard_normal(40)
        y = rng.standard_normal(40)
        maker.scatter(
            x=x,
            y=y,
            index=_index(maker),
            subparams=ScatterParameters(s=40),
        )
        _save(maker, "series/scatter.png")

    def test_bar(self) -> None:
        maker = _maker()
        maker.bar(
            x=np.arange(4.0),
            height=np.array([3.0, 5.0, 2.0, 4.0]),
            index=_index(maker),
            subparams=BarParameters(width=0.6),
        )
        _save(maker, "series/bar.png")

    def test_barh(self) -> None:
        maker = _maker()
        maker.barh(
            y=np.arange(4.0),
            width=np.array([3.0, 5.0, 2.0, 4.0]),
            index=_index(maker),
            subparams=BarhParameters(height=0.6),
        )
        _save(maker, "series/barh.png")

    def test_pie(self) -> None:
        maker = _maker()
        maker.pie(
            values=np.array([45.0, 30.0, 15.0, 10.0]),
            index=_index(maker),
            labels=["A", "B", "C", "D"],
            subparams=PieParameters(
                autopct="%1.0f%%",
                startangle=90.0,
                counterclock=False,
                wedgeprops=WedgeStyle(edgecolor="white", linewidth=1.5),
            ),
        )
        _save(maker, "proportion/pie.png")

    def test_quiver(self) -> None:
        maker = _maker()
        x = np.linspace(-2, 2, 5)
        y = np.linspace(-2, 2, 5)
        xx, yy = np.meshgrid(x, y)
        maker.quiver(
            u=-xx,
            v=-yy,
            x=xx,
            y=yy,
            index=_index(maker),
            subparams=QuiverParameters(angles=QuiverAngles.XY, scale=20.0),
        )
        _save(maker, "vector/quiver.png")

    def test_arrow(self) -> None:
        maker = _maker()
        maker.arrow(
            x=0.0,
            y=0.0,
            dx=0.8,
            dy=0.5,
            index=_index(maker),
            subparams=ArrowParameters(width=0.05, color="C0"),
        )
        _save(maker, "vector/arrow.png")

    def test_legend(self) -> None:
        maker = _maker()
        x = np.linspace(0, 1, 20)
        idx = _index(maker)
        maker.plot(x=x, y=x, index=idx, subparams=PlotParameters(label="a"))
        maker.plot(x=x, y=1 - x, index=idx, subparams=PlotParameters(label="b"))
        maker.legend(index=idx)
        _save(maker, "misc/legend.png")

    def test_line(self) -> None:
        maker = _maker()
        x = np.linspace(-1, 1, 30)
        idx = _index(maker)
        maker.plot(x=x, y=x**2, index=idx)
        maker.line(
            value=0.0,
            orientation=Orientation.VERTICAL,
            index=idx,
            subparams=LineParameters(color="red"),
        )
        _save(maker, "misc/line.png")

    def test_annotate(self) -> None:
        maker = _maker()
        rng = np.random.default_rng(0)
        x = rng.standard_normal(30)
        y = rng.standard_normal(30)
        idx = _index(maker)
        maker.scatter(x=x, y=y, index=idx)
        maker.annotate(
            text="mean",
            xy=(float(np.mean(x)), float(np.mean(y))),
            index=idx,
            xytext=(float(np.mean(x)) + 0.5, float(np.mean(y)) + 0.5),
            subparams=AnnotateParameters(arrowprops=ArrowProperties()),
        )
        _save(maker, "misc/annotate.png")

    def test_span(self) -> None:
        maker = _maker()
        x = np.linspace(0, 10, 100)
        idx = _index(maker)
        maker.plot(x=x, y=np.sin(x), index=idx)
        maker.span(
            start=3.0,
            end=5.0,
            orientation=Orientation.VERTICAL,
            index=idx,
            subparams=SpanParameters(color="orange", alpha=0.3),
        )
        _save(maker, "misc/span.png")

    def test_step(self) -> None:
        maker = _maker()
        maker.step(
            x=np.arange(8.0),
            y=np.array([1.0, 3.0, 2.0, 4.0, 4.0, 1.0, 2.0, 3.0]),
            index=_index(maker),
            subparams=StepParameters(where=StepWhere.MID),
        )
        _save(maker, "series/step.png")

    def test_errorbar(self) -> None:
        maker = _maker()
        x = np.arange(6.0)
        maker.errorbar(
            x=x,
            y=np.sqrt(x),
            yerr=np.full(6, 0.3),
            index=_index(maker),
            subparams=ErrorbarParameters(marker=Marker.CIRCLE, capsize=3.0),
        )
        _save(maker, "series/errorbar.png")

    def test_fill_between(self) -> None:
        maker = _maker()
        x = np.linspace(0, 2 * np.pi, 50)
        idx = _index(maker)
        maker.fill_between(
            x=x,
            y1=np.sin(x) - 0.3,
            y2=np.sin(x) + 0.3,
            index=idx,
            subparams=FillBetweenParameters(alpha=0.3),
        )
        maker.plot(x=x, y=np.sin(x), index=idx)
        _save(maker, "series/fill_between.png")

    def test_stackplot(self) -> None:
        maker = _maker()
        x = np.arange(6.0)
        maker.stackplot(
            x=x,
            ys=[np.array([1.0, 2.0, 2.0, 3.0, 3.0, 4.0]), np.array([2.0, 2.0, 3.0, 2.0, 3.0, 3.0])],
            index=_index(maker),
            labels=["a", "b"],
            subparams=StackplotParameters(alpha=0.8),
        )
        _save(maker, "series/stackplot.png")

    def test_hist(self) -> None:
        maker = _maker()
        rng = np.random.default_rng(0)
        maker.hist(
            x=rng.standard_normal(500),
            index=_index(maker),
            subparams=HistParameters(bins=20, edgecolor="white"),
        )
        _save(maker, "distribution/hist.png")

    def test_boxplot(self) -> None:
        maker = _maker()
        rng = np.random.default_rng(0)
        maker.boxplot(
            data=[rng.normal(loc, 1.0, 100) for loc in (0.0, 1.0, 0.5)],
            index=_index(maker),
            tick_labels=["A", "B", "C"],
            subparams=BoxplotParameters(showmeans=True),
        )
        _save(maker, "distribution/boxplot.png")

    def test_violinplot(self) -> None:
        maker = _maker()
        rng = np.random.default_rng(0)
        maker.violinplot(
            data=[rng.normal(loc, 1.0, 100) for loc in (0.0, 1.0, 0.5)],
            index=_index(maker),
            subparams=ViolinplotParameters(showmedians=True),
        )
        _save(maker, "distribution/violinplot.png")

    def test_hexbin(self) -> None:
        maker = _maker()
        rng = np.random.default_rng(0)
        maker.hexbin(
            x=rng.standard_normal(2000),
            y=rng.standard_normal(2000),
            index=_index(maker),
            subparams=HexbinParameters(gridsize=20, mincnt=1, cmap=ColorMap.VIRIDIS),
        )
        _save(maker, "distribution/hexbin.png")

    def test_hist2d(self) -> None:
        maker = _maker()
        rng = np.random.default_rng(0)
        maker.hist2d(
            x=rng.standard_normal(2000),
            y=rng.standard_normal(2000),
            index=_index(maker),
            subparams=Hist2dParameters(bins=20, cmap=ColorMap.VIRIDIS),
        )
        _save(maker, "distribution/hist2d.png")

    def test_contour(self) -> None:
        maker = _maker()
        xx, yy = np.meshgrid(np.linspace(-2, 2, 50), np.linspace(-2, 2, 50))
        maker.contour(
            z=np.exp(-(xx**2) - yy**2),
            x=xx,
            y=yy,
            index=_index(maker),
            is_labeled=True,
            subparams=ContourParameters(levels=5, cmap=ColorMap.VIRIDIS),
        )
        _save(maker, "image/contour.png")

    def test_contourf(self) -> None:
        maker = _maker()
        xx, yy = np.meshgrid(np.linspace(-2, 2, 50), np.linspace(-2, 2, 50))
        z = np.exp(-(xx**2) - yy**2)
        idx = _index(maker)
        bands = maker.contourf(z=z, x=xx, y=yy, index=idx, subparams=ContourfParameters(levels=8, cmap=ColorMap.VIRIDIS))
        _ = maker.set_colorbar(index=idx, mappable=bands)
        _save(maker, "image/contourf.png")

    def test_pcolormesh(self) -> None:
        maker = _maker()
        x = np.array([0.0, 1.0, 3.0, 6.0, 10.0])
        y = np.array([0.0, 1.0, 2.0, 4.0])
        maker.pcolormesh(
            z=np.arange(12.0).reshape(3, 4),
            x=x,
            y=y,
            index=_index(maker),
            subparams=PcolormeshParameters(shading=Shading.FLAT, edgecolors="white", cmap=ColorMap.VIRIDIS),
        )
        _save(maker, "image/pcolormesh.png")

    def test_imscatter(self) -> None:
        maker = _maker()
        icon = np.linspace(0, 1, 16 * 16).reshape(16, 16)
        maker.imscatter(
            x=np.array([0.0, 1.0, 2.0, 3.0]),
            y=np.array([0.0, 2.0, 1.0, 3.0]),
            images=[icon],
            index=_index(maker),
            subparams=ImscatterParameters(zoom=1.0, cmap=ColorMap.VIRIDIS),
        )
        _save(maker, "image/imscatter.png")

    def test_streamplot(self) -> None:
        maker = _maker()
        x = np.linspace(-2, 2, 30)
        y = np.linspace(-2, 2, 30)
        xx, yy = np.meshgrid(x, y)
        maker.streamplot(
            x=x,
            y=y,
            u=-yy,
            v=xx,
            color_values=np.hypot(xx, yy),
            index=_index(maker),
            subparams=StreamplotParameters(cmap=ColorMap.VIRIDIS),
        )
        _save(maker, "vector/streamplot.png")
