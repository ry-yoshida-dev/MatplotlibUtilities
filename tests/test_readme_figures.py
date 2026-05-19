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
    ArrowParameters,
    ColorbarParameters,
    GraphLayout,
    GraphParameters,
    ImshowParameters,
    LineParameters,
    MatplotGraphMaker,
    Orientation,
    PlotParameters,
    QuiverAngles,
    QuiverParameters,
    ScatterParameters,
    TableAxis,
)
from matplotlib_utilities.mixin.draw.parameters import BarParameters

DRAW_README = Path(__file__).resolve().parents[1] / "src/matplotlib_utilities/mixin/draw"
FIGURES_ROOT = DRAW_README / "readme_figures"

UPDATE = os.environ.get("UPDATE_README_FIGURES") == "1"

# Small figures for README embeds (default GraphParameters is 250 dpi / 5×3 in).
README_GRAPH_PARAMETERS = GraphParameters(figsize=(2.8, 1.8), dpi=100, font_size=8)
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
    "vector/quiver.png",
    "vector/arrow.png",
    "misc/legend.png",
    "misc/line.png",
    "misc/annotate.png",
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
        maker.set_colorbar(
            index=_index(maker),
            image=data,
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
            index=_index(maker),
            subparams=BarParameters(height=[3.0, 5.0, 2.0, 4.0], width=0.6),
        )
        _save(maker, "series/bar.png")

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
            subparams=AnnotateParameters(arrowprops={"arrowstyle": "->"}),
        )
        _save(maker, "misc/annotate.png")
