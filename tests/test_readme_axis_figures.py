"""README figures under mixin/axis/readme_figures/.

Default pytest skips regeneration. Refresh assets:

    UPDATE_README_FIGURES=1 pytest tests/test_readme_axis_figures.py -k update
"""

from __future__ import annotations

import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import numpy as np
import pytest

from matplotlib_utilities import (
    GraphAxis,
    GraphLayout,
    GraphParameters,
    MatplotGraphMaker,
    TableAxis,
)
from matplotlib_utilities.mixin.axis.parameters import GridParameters, TickParamsParameters

AXIS_README = Path(__file__).resolve().parents[1] / "src/matplotlib_utilities/mixin/axis"
FIGURES_ROOT = AXIS_README / "readme_figures"

UPDATE = os.environ.get("UPDATE_README_FIGURES") == "1"

README_GRAPH_PARAMETERS = GraphParameters(figsize=(2.8, 1.8), dpi=100, font_size=8)

FIGURE_PATHS = [
    "set_label.png",
    "set_lim.png",
    "set_title.png",
    "set_grid.png",
    "delete_axis_label.png",
]


def _maker() -> MatplotGraphMaker:
    layout = GraphLayout.from_number(number=1, axis=TableAxis.COLUMN, axis_value=1)
    return MatplotGraphMaker(layout=layout, parameters=README_GRAPH_PARAMETERS)


def _index(maker: MatplotGraphMaker):
    return maker.get_subplot_index_from_number(number=0)


def _save(maker: MatplotGraphMaker, rel_path: str) -> Path:
    out = FIGURES_ROOT / rel_path
    out.parent.mkdir(parents=True, exist_ok=True)
    maker.finalize(save_path=str(out), is_showing_result_enabled=False)
    return out


def _base_plot(maker: MatplotGraphMaker, idx) -> None:
    x = np.linspace(0, 2 * np.pi, 40)
    maker.plot(x=x, y=np.sin(x), index=idx)


@pytest.mark.parametrize("rel_path", FIGURE_PATHS)
def test_readme_axis_figure_committed(rel_path: str) -> None:
    path = FIGURES_ROOT / rel_path
    assert path.is_file(), f"missing {path}; run UPDATE_README_FIGURES=1 pytest -k update"
    assert path.stat().st_size > 0


@pytest.mark.skipif(not UPDATE, reason="set UPDATE_README_FIGURES=1 to regenerate PNGs")
class TestUpdateReadmeAxisFigures:
    def test_set_label(self) -> None:
        maker = _maker()
        idx = _index(maker)
        _base_plot(maker, idx)
        maker.set_label(label="x", index=idx, axis=GraphAxis.X)
        maker.set_label(label="y", index=idx, axis=GraphAxis.Y)
        _save(maker, "set_label.png")

    def test_set_lim(self) -> None:
        maker = _maker()
        idx = _index(maker)
        _base_plot(maker, idx)
        maker.set_lim(lower=-1.0, upper=1.0, index=idx, axis=GraphAxis.Y)
        _save(maker, "set_lim.png")

    def test_set_title(self) -> None:
        maker = _maker()
        idx = _index(maker)
        _base_plot(maker, idx)
        maker.set_title(title="sin(x)", index=idx)
        _save(maker, "set_title.png")

    def test_set_grid(self) -> None:
        maker = _maker()
        idx = _index(maker)
        _base_plot(maker, idx)
        maker.set_grid(index=idx, subparams=GridParameters(alpha=0.4))
        _save(maker, "set_grid.png")

    def test_delete_axis_label(self) -> None:
        maker = _maker()
        idx = _index(maker)
        _base_plot(maker, idx)
        maker.delete_axis_label(
            index=idx,
            subparams=TickParamsParameters(labelbottom=False, labelleft=False),
        )
        _save(maker, "delete_axis_label.png")
