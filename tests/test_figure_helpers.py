"""Figure title, unused subplots and grid placement."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from matplotlib_utilities import GraphLayout, MatplotGraphMaker


def test_set_figure_title_sets_the_suptitle() -> None:
    maker = MatplotGraphMaker()
    maker.set_figure_title(title="Overview")
    assert maker.fig.get_suptitle() == "Overview"
    plt.close(maker.fig)


def test_hide_unused_subplots_hides_only_empty_cells() -> None:
    maker = MatplotGraphMaker(layout=GraphLayout(number=5, column=3, row=2))
    maker.hide_unused_subplots()
    visibility = [axes.axison for axes in maker.ax.flat]
    assert visibility == [True, True, True, True, True, False]
    plt.close(maker.fig)


def test_set_grid_below_places_the_grid_under_the_data() -> None:
    maker = MatplotGraphMaker()
    index = maker.get_subplot_index_from_number(number=0)
    maker.set_grid_below(index=index)
    assert maker.access_subplot(index=index).get_axisbelow() is True
    maker.set_grid_below(index=index, is_below=False)
    assert maker.access_subplot(index=index).get_axisbelow() is False
    plt.close(maker.fig)
