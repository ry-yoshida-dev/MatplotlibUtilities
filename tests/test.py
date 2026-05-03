"""Smoke tests and the former maker module demo (non-interactive)."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import numpy as np
import pytest
from pathlib import Path

from matplotlib_utilities import (
    AnnotateParameters,
    GraphAxis,
    GraphLayout,
    GraphParameters,
    LineParameters,
    MatplotGraphMaker,
    Orientation,
    ScatterParameters,
    TableAxis,
)


def build_demo_graph_maker() -> MatplotGraphMaker:
    num_graph = 4
    layout = GraphLayout.from_number(
        number=num_graph,
        axis=TableAxis.COLUMN,
        axis_value=num_graph // 2,
    )
    params = GraphParameters()
    graph_maker = MatplotGraphMaker(layout=layout, parameters=params)

    x1 = np.random.default_rng(0).standard_normal(100)
    y1 = np.random.default_rng(1).standard_normal(100)
    confidences = np.random.default_rng(2).random(100)

    index = graph_maker.get_subplot_index_from_number(number=0)
    # Per-point marker area (matplotlib *s*); map e.g. confidences to visible sizes.
    sizes = 20.0 + confidences * 80.0
    graph_maker.scatter(
        index=index,
        x=x1,
        y=y1,
        subparams=ScatterParameters(s=sizes),
    )
    graph_maker.annotate(
        text="mean",
        xy=(float(np.mean(x1)), float(np.mean(y1))),
        index=index,
        xytext=(float(np.mean(x1)) + 0.5, float(np.mean(y1)) + 0.5),
        subparams=AnnotateParameters(
            arrowprops={"arrowstyle": "->"},
            fontsize=9,
        ),
    )
    graph_maker.set_label(
        label="x",
        index=graph_maker.get_subplot_index_from_number(number=0),
        axis=GraphAxis.X,
    )
    index = graph_maker.get_subplot_index_from_number(number=1)
    graph_maker.plot(
        index=index,
        x=x1,
        y=y1,
    )
    graph_maker.line(
        value=0.5,
        orientation=Orientation.VERTICAL,
        index=graph_maker.get_subplot_index_from_number(number=1),
        subparams=LineParameters(color="red"),
    )
    graph_maker.line(
        value=0.0,
        orientation=Orientation.HORIZONTAL,
        index=graph_maker.get_subplot_index_from_number(number=1),
        subparams=LineParameters(color="blue"),
    )
    return graph_maker


def test_import_package() -> None:
    import matplotlib_utilities as mu  # noqa: F401

    assert hasattr(mu, "MatplotGraphMaker")
    assert hasattr(mu, "AnnotateParameters")


def test_scatter_parameters_label_in_to_dict() -> None:
    """Scatter includes matplotlib ``label`` in ``to_dict`` like ``Axes.scatter``."""
    assert ScatterParameters(label="series A").to_dict["label"] == "series A"


def test_graph_maker_demo_smoke(tmp_path: Path) -> None:
    graph_maker = build_demo_graph_maker()
    out = tmp_path / "demo.png"
    graph_maker.finalize(save_path=str(out), is_showing_result_enabled=False)
    assert out.is_file()
    assert out.stat().st_size > 0


@pytest.mark.parametrize("num_graph", [1, 2, 4])
def test_graph_layout_from_number(num_graph: int) -> None:
    layout = GraphLayout.from_number(
        number=num_graph,
        axis=TableAxis.COLUMN,
        axis_value=max(1, num_graph // 2),
    )
    assert layout.row * layout.column >= num_graph
