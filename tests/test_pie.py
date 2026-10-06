"""Pie charts and the nested wedge styling."""

from __future__ import annotations

from collections.abc import Callable

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.patches import Wedge

from matplotlib_utilities import (
    GraphLayout,
    GraphParameters,
    MatplotGraphMaker,
    PieParameters,
    WedgeStyle,
)


def _maker() -> MatplotGraphMaker:
    return MatplotGraphMaker(
        layout=GraphLayout.from_row_column(row=1, column=1),
        parameters=GraphParameters(),
    )


def _wedges(maker: MatplotGraphMaker) -> list[Wedge]:
    subplot = maker.access_subplot(index=maker.get_subplot_index_from_number(number=0))
    return [patch for patch in subplot.patches if isinstance(patch, Wedge)]


def test_pie_draws_one_wedge_per_value() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.pie(values=np.array([1.0, 2.0, 3.0]), index=index)
    assert len(_wedges(maker)) == 3
    plt.close(maker.fig)


def test_pie_wedge_angles_follow_the_shares() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.pie(values=np.array([1.0, 3.0]), index=index, subparams=PieParameters(startangle=0.0))
    spans = [wedge.theta2 - wedge.theta1 for wedge in _wedges(maker)]
    assert spans == pytest.approx([90.0, 270.0])
    plt.close(maker.fig)


def test_pie_draws_labels_and_percentages() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.pie(
        values=np.array([1.0, 1.0]),
        index=index,
        labels=["a", "b"],
        subparams=PieParameters(autopct="%1.0f%%"),
    )
    texts = {text.get_text() for text in maker.access_subplot(index=index).texts}
    assert {"a", "b", "50%"} <= texts
    plt.close(maker.fig)


def test_wedge_style_reaches_matplotlib_as_wedgeprops() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.pie(
        values=np.array([1.0, 1.0]),
        index=index,
        subparams=PieParameters(
            wedgeprops=WedgeStyle(edgecolor="white", linewidth=2.0, width=0.4, alpha=0.5, zorder=3.0)
        ),
    )
    wedge = _wedges(maker)[0]
    assert wedge.get_linewidth() == pytest.approx(2.0)
    assert wedge.width == pytest.approx(0.4)
    assert wedge.get_alpha() == pytest.approx(0.5)
    assert wedge.get_zorder() == pytest.approx(3.0)
    plt.close(maker.fig)


def test_wedge_style_nests_in_to_dict() -> None:
    parameters = PieParameters(wedgeprops=WedgeStyle(edgecolor="white"))
    assert parameters.to_dict == {"wedgeprops": {"edgecolor": "white"}}


@pytest.mark.parametrize(
    "values",
    [np.array([1.0, -1.0]), np.array([0.0, 0.0]), np.array([1.0, np.nan]), np.ones((2, 2))],
)
def test_pie_rejects_invalid_values(values: np.ndarray) -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    with pytest.raises(ValueError, match="values"):
        maker.pie(values=values, index=index)
    plt.close(maker.fig)


def test_pie_rejects_labels_that_do_not_match_the_values() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    with pytest.raises(ValueError, match="labels must hold one entry per value"):
        maker.pie(values=np.array([1.0, 2.0]), index=index, labels=["only one"])
    plt.close(maker.fig)


def test_pie_rejects_colors_that_do_not_match_the_values() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    with pytest.raises(ValueError, match="colors must hold one entry per value"):
        maker.pie(values=np.array([1.0, 2.0]), index=index, subparams=PieParameters(colors=["red"]))
    plt.close(maker.fig)


@pytest.mark.parametrize(
    "build",
    [
        lambda: PieParameters(radius=0.0),
        lambda: PieParameters(explode=[0.1, -0.1]),
        lambda: WedgeStyle(width=0.0),
        lambda: WedgeStyle(linewidth=-1.0),
        lambda: WedgeStyle(alpha=1.5),
        lambda: WedgeStyle(zorder=-1.0),
    ],
)
def test_parameters_reject_invalid_settings(build: Callable[[], object]) -> None:
    with pytest.raises(ValueError):
        build()
