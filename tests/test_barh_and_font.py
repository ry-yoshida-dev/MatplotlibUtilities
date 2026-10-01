"""Horizontal bars, tick control and the Japanese font family."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pytest

from matplotlib_utilities import (
    BarhParameters,
    FontFamily,
    GraphAxis,
    GraphLayout,
    GraphParameters,
    MatplotGraphMaker,
)

JAPANESE_LABELS = ["市区町村道", "主要地方道・都道府県道", "一般国道"]


def _maker(font_family: FontFamily = FontFamily.DEFAULT) -> MatplotGraphMaker:
    return MatplotGraphMaker(
        layout=GraphLayout.from_row_column(row=1, column=1),
        parameters=GraphParameters(font_family=font_family),
    )


def _close(maker: MatplotGraphMaker) -> None:
    plt.close(maker.fig)


def test_barh_draws_one_bar_per_value() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.barh(y=np.arange(3), width=np.array([1.0, 2.0, 3.0]), index=index)
    assert len(maker.access_subplot(index=index).patches) == 3
    _close(maker)


def test_barh_bars_run_along_the_x_axis() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.barh(y=np.arange(2), width=np.array([4.0, 8.0]), index=index)
    widths = [patch.get_width() for patch in maker.access_subplot(index=index).patches]
    assert widths == [4.0, 8.0]
    _close(maker)


def test_barh_applies_its_subparameters() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.barh(
        y=np.arange(2),
        width=np.array([1.0, 2.0]),
        index=index,
        subparams=BarhParameters(height=0.25, facecolor="#2a78d6"),
    )
    patch = maker.access_subplot(index=index).patches[0]
    assert patch.get_height() == pytest.approx(0.25)
    _close(maker)


def test_barh_rejects_mismatched_lengths() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    with pytest.raises(ValueError, match="same number of entries"):
        maker.barh(y=np.arange(3), width=np.array([1.0, 2.0]), index=index)
    _close(maker)


def test_set_ticks_places_labels_at_the_given_positions() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.set_ticks(
        positions=[0.0, 1.0, 2.0], index=index, axis=GraphAxis.Y, labels=JAPANESE_LABELS
    )
    drawn = [text.get_text() for text in maker.access_subplot(index=index).get_yticklabels()]
    assert drawn == JAPANESE_LABELS
    _close(maker)


def test_set_ticks_without_labels_keeps_numeric_ones() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.set_ticks(positions=[0.0, 1.0], index=index, axis=GraphAxis.X)
    assert list(maker.access_subplot(index=index).get_xticks()) == [0.0, 1.0]
    _close(maker)


def test_set_ticks_rejects_a_label_count_that_does_not_match() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    with pytest.raises(ValueError, match="one entry per position"):
        maker.set_ticks(positions=[0.0, 1.0], index=index, axis=GraphAxis.Y, labels=["only one"])
    _close(maker)


def test_invert_turns_the_axis_around() -> None:
    maker = _maker()
    index = maker.get_subplot_index_from_number(number=0)
    subplot = maker.access_subplot(index=index)
    before = subplot.get_ylim()
    maker.invert(index=index, axis=GraphAxis.Y)
    assert subplot.get_ylim() == (before[1], before[0])
    _close(maker)


def test_the_japanese_family_registers_a_font_holding_japanese_glyphs() -> None:
    maker = _maker(font_family=FontFamily.JAPANESE)
    family = plt.rcParams["font.family"]
    assert family != ["sans-serif"]
    _close(maker)


def test_japanese_labels_are_drawn_rather_than_dropped() -> None:
    maker = _maker(font_family=FontFamily.JAPANESE)
    index = maker.get_subplot_index_from_number(number=0)
    maker.barh(y=np.arange(3), width=np.array([3.0, 2.0, 1.0]), index=index)
    maker.set_ticks(
        positions=[0.0, 1.0, 2.0], index=index, axis=GraphAxis.Y, labels=JAPANESE_LABELS
    )
    maker.fig.canvas.draw()
    drawn = [text.get_text() for text in maker.access_subplot(index=index).get_yticklabels()]
    assert drawn == JAPANESE_LABELS
    _close(maker)


def test_the_default_family_leaves_matplotlib_alone() -> None:
    before = list(plt.rcParams["font.family"])
    maker = _maker(font_family=FontFamily.DEFAULT)
    assert list(plt.rcParams["font.family"]) == before
    _close(maker)
