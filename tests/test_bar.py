"""Vertical bars, and the label and opacity shared with horizontal bars."""

from __future__ import annotations

from collections.abc import Callable

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.container import BarContainer

from matplotlib_utilities import (
    BarhParameters,
    BarParameters,
    GraphLayout,
    MatplotGraphMaker,
)


def _maker() -> MatplotGraphMaker:
    return MatplotGraphMaker(layout=GraphLayout.from_row_column(row=1, column=1))


def test_bar_draws_one_bar_per_height() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.bar(x=np.arange(3), height=np.array([3.0, 1.0, 2.0]), index=index)
    container = maker.access_subplot(index=index).containers[0]
    assert isinstance(container, BarContainer)
    heights = [patch.get_height() for patch in container.patches]
    assert heights == [3.0, 1.0, 2.0]
    plt.close(maker.fig)


def test_bar_rejects_mismatched_lengths() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    with pytest.raises(ValueError, match="same number"):
        maker.bar(x=np.arange(3), height=np.array([1.0, 2.0]), index=index)
    plt.close(maker.fig)


def test_bar_label_and_opacity_reach_the_bars() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.bar(
        x=np.arange(2),
        height=np.array([1.0, 2.0]),
        index=index,
        subparams=BarParameters(width=0.4, label="2024", alpha=0.5),
    )
    subplot = maker.access_subplot(index=index)
    assert subplot.containers[0].get_label() == "2024"
    assert all(patch.get_alpha() == 0.5 for patch in subplot.patches)
    container = subplot.containers[0]
    assert isinstance(container, BarContainer)
    assert container.patches[0].get_width() == pytest.approx(0.4)
    plt.close(maker.fig)


def test_barh_opacity_reaches_the_bars() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.barh(
        y=np.arange(2),
        width=np.array([1.0, 2.0]),
        index=index,
        subparams=BarhParameters(alpha=0.3, label="2024"),
    )
    subplot = maker.access_subplot(index=index)
    assert all(patch.get_alpha() == 0.3 for patch in subplot.patches)
    assert subplot.containers[0].get_label() == "2024"
    plt.close(maker.fig)


@pytest.mark.parametrize(
    "build",
    [
        lambda: BarParameters(width=0.0),
        lambda: BarParameters(alpha=1.5),
        lambda: BarhParameters(height=-1.0),
        lambda: BarhParameters(alpha=-0.1),
    ],
)
def test_invalid_bar_parameters_are_rejected(build: Callable[[], object]) -> None:
    with pytest.raises(ValueError):
        build()
