"""Default subplot index, layout validation, and finalize cleanup."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pytest

from matplotlib_utilities import (
    FontFamily,
    GraphLayout,
    GraphParameters,
    MatplotGraphMaker,
    RowColumnIndex,
)
from matplotlib_utilities.utils import TableAxis


@pytest.mark.parametrize(
    ("number", "axis", "axis_value", "expected_row", "expected_column"),
    [
        (4, TableAxis.COLUMN, 3, 2, 3),
        (5, TableAxis.COLUMN, 4, 2, 4),
        (4, TableAxis.ROW, 3, 3, 2),
        (7, TableAxis.COLUMN, 3, 3, 3),
    ],
)
def test_from_number_accepts_a_partly_filled_last_row(
    number: int, axis: TableAxis, axis_value: int, expected_row: int, expected_column: int
) -> None:
    layout = GraphLayout.from_number(number=number, axis=axis, axis_value=axis_value)
    assert (layout.row, layout.column) == (expected_row, expected_column)


def test_layout_rejects_more_subplots_than_cells() -> None:
    with pytest.raises(ValueError, match="fit in the grid"):
        _ = GraphLayout(number=7, column=3, row=2)


def test_drawing_without_index_uses_the_first_subplot() -> None:
    maker = MatplotGraphMaker(layout=GraphLayout.from_row_column(row=1, column=2))
    maker.plot(x=np.arange(3), y=np.arange(3))
    assert len(maker.ax[0][0].get_lines()) == 1
    assert len(maker.ax[0][1].get_lines()) == 0
    plt.close(maker.fig)


def test_an_integer_index_selects_the_subplot_in_row_major_order() -> None:
    maker = MatplotGraphMaker(layout=GraphLayout.from_row_column(row=2, column=2))
    assert maker.access_subplot(index=3) is maker.ax[1][1]
    assert maker.access_subplot(index=RowColumnIndex(row_index=1, column_index=0)) is maker.ax[1][0]
    plt.close(maker.fig)


@pytest.mark.parametrize("index", [4, RowColumnIndex(row_index=0, column_index=2)])
def test_an_index_outside_the_layout_is_rejected(index: int | RowColumnIndex) -> None:
    maker = MatplotGraphMaker(layout=GraphLayout.from_row_column(row=2, column=2))
    with pytest.raises(ValueError, match="out of range"):
        _ = maker.access_subplot(index=index)
    plt.close(maker.fig)


@pytest.mark.filterwarnings("ignore:FigureCanvasAgg is non-interactive")
def test_finalize_hides_unused_cells_and_closes_the_figure() -> None:
    maker = MatplotGraphMaker(layout=GraphLayout(number=3, column=2, row=2))
    maker.finalize(is_showing_result_enabled=True)
    assert maker.ax[1][1].axison is False
    assert not plt.fignum_exists(maker.fig.number)


def test_finalize_restores_the_global_font_settings() -> None:
    with plt.rc_context({"font.family": ["sans-serif"], "font.size": 10.0}):
        maker = MatplotGraphMaker(
            parameters=GraphParameters(font_family=FontFamily.JAPANESE, font_size=15.0)
        )
        assert list(plt.rcParams["font.family"]) != ["sans-serif"]
        maker.finalize(is_showing_result_enabled=False)
        assert list(plt.rcParams["font.family"]) == ["sans-serif"]
        assert plt.rcParams["font.size"] == 10.0


def test_zero_is_rejected_for_sizes() -> None:
    with pytest.raises(ValueError, match="dpi"):
        _ = GraphParameters(dpi=0)
    with pytest.raises(ValueError, match="font_size"):
        _ = GraphParameters(font_size=0)
