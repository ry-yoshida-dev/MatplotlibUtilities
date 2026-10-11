"""Histograms, box and violin plots, and 2-D binning."""

from __future__ import annotations

from collections.abc import Callable, Iterator

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.axes import Axes
from matplotlib.collections import PolyCollection, QuadMesh
from matplotlib.colors import LogNorm
from matplotlib.patches import Rectangle

from matplotlib_utilities import (
    BoxplotParameters,
    GraphLayout,
    GraphParameters,
    HexbinParameters,
    Hist2dParameters,
    HistParameters,
    HistType,
    MatplotGraphMaker,
    Orientation,
    SubplotIndex,
    ViolinplotParameters,
)

RNG = np.random.default_rng(0)


@pytest.fixture
def maker() -> Iterator[MatplotGraphMaker]:
    graph_maker = MatplotGraphMaker(
        layout=GraphLayout.from_row_column(row=1, column=1),
        parameters=GraphParameters(),
    )
    yield graph_maker
    plt.close(graph_maker.fig)


def _index(maker: MatplotGraphMaker) -> SubplotIndex:
    return maker.get_subplot_index_from_number(number=0)


def _subplot(maker: MatplotGraphMaker) -> Axes:
    return maker.access_subplot(index=_index(maker))


def test_hist_draws_one_bar_per_bin(maker: MatplotGraphMaker) -> None:
    maker.hist(x=RNG.normal(size=100), index=_index(maker), subparams=HistParameters(bins=7))
    bars = [patch for patch in _subplot(maker).patches if isinstance(patch, Rectangle)]
    assert len(bars) == 7


def test_hist_counts_sum_to_the_sample_size(maker: MatplotGraphMaker) -> None:
    maker.hist(x=RNG.normal(size=100), index=_index(maker), subparams=HistParameters(bins=5))
    heights = [patch.get_height() for patch in _subplot(maker).patches if isinstance(patch, Rectangle)]
    assert sum(heights) == pytest.approx(100.0)


def test_hist_accepts_several_datasets(maker: MatplotGraphMaker) -> None:
    maker.hist(
        x=[RNG.normal(size=50), RNG.normal(size=50)],
        index=_index(maker),
        subparams=HistParameters(bins=4, stacked=True, color=["C0", "C1"], histtype=HistType.BAR_STACKED),
    )
    assert len(_subplot(maker).patches) == 8


def test_hist_treats_each_column_of_a_2d_array_as_a_dataset(maker: MatplotGraphMaker) -> None:
    maker.hist(
        x=RNG.normal(size=(50, 2)),
        index=_index(maker),
        subparams=HistParameters(bins=4, color=["C0", "C1"]),
    )
    assert len(_subplot(maker).patches) == 8


def test_hist_rejects_an_array_with_more_than_two_dimensions(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="x must be a 1-D or 2-D array"):
        maker.hist(x=np.zeros((2, 2, 2)), index=_index(maker))


def test_hist_rejects_an_empty_dataset(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="empty dataset"):
        maker.hist(x=np.array([]), index=_index(maker))


def test_hist_rejects_colors_that_do_not_match_the_datasets(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="color must hold one entry per dataset"):
        maker.hist(
            x=[RNG.normal(size=10), RNG.normal(size=10)],
            index=_index(maker),
            subparams=HistParameters(color=["C0"]),
        )


def test_boxplot_labels_each_box(maker: MatplotGraphMaker) -> None:
    maker.boxplot(
        data=[RNG.normal(size=20) for _ in range(3)],
        index=_index(maker),
        tick_labels=["a", "b", "c"],
    )
    labels = [label.get_text() for label in _subplot(maker).get_xticklabels()]
    assert labels == ["a", "b", "c"]


def test_boxplot_horizontal_puts_labels_on_the_y_axis(maker: MatplotGraphMaker) -> None:
    maker.boxplot(
        data=[RNG.normal(size=20) for _ in range(2)],
        index=_index(maker),
        tick_labels=["a", "b"],
        subparams=BoxplotParameters(orientation=Orientation.HORIZONTAL),
    )
    labels = [label.get_text() for label in _subplot(maker).get_yticklabels()]
    assert labels == ["a", "b"]


def test_boxplot_treats_each_column_of_a_2d_array_as_a_dataset(maker: MatplotGraphMaker) -> None:
    maker.boxplot(data=RNG.normal(size=(20, 3)), index=_index(maker), tick_labels=["a", "b", "c"])
    labels = [label.get_text() for label in _subplot(maker).get_xticklabels()]
    assert labels == ["a", "b", "c"]


def test_boxplot_treats_a_1d_array_as_one_dataset(maker: MatplotGraphMaker) -> None:
    maker.boxplot(data=RNG.normal(size=20), index=_index(maker), tick_labels=["a"])
    labels = [label.get_text() for label in _subplot(maker).get_xticklabels()]
    assert labels == ["a"]


def test_boxplot_rejects_labels_that_do_not_match_the_data(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="tick_labels must hold one entry per dataset"):
        maker.boxplot(data=[RNG.normal(size=5)], index=_index(maker), tick_labels=["a", "b"])


def test_violinplot_draws_one_body_per_dataset(maker: MatplotGraphMaker) -> None:
    maker.violinplot(
        data=[RNG.normal(size=30) for _ in range(3)],
        index=_index(maker),
        subparams=ViolinplotParameters(showmedians=True),
    )
    bodies = [collection for collection in _subplot(maker).collections if isinstance(collection, PolyCollection)]
    assert len(bodies) == 3


def test_violinplot_treats_each_column_of_a_2d_array_as_a_dataset(maker: MatplotGraphMaker) -> None:
    maker.violinplot(data=RNG.normal(size=(30, 3)), index=_index(maker))
    bodies = [collection for collection in _subplot(maker).collections if isinstance(collection, PolyCollection)]
    assert len(bodies) == 3


def test_violinplot_rejects_an_empty_sequence(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="data must hold at least one dataset"):
        maker.violinplot(data=[], index=_index(maker))


def test_violinplot_rejects_positions_that_do_not_match_the_data(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="positions must hold one entry per dataset"):
        maker.violinplot(data=[RNG.normal(size=5)], index=_index(maker), positions=[1.0, 2.0])


def test_hexbin_hides_empty_hexagons_with_mincnt(maker: MatplotGraphMaker) -> None:
    maker.hexbin(
        x=np.array([0.0, 0.0, 1.0]),
        y=np.array([0.0, 0.0, 1.0]),
        index=_index(maker),
        subparams=HexbinParameters(gridsize=3, mincnt=1),
    )
    counts = _subplot(maker).collections[0].get_array()
    assert counts is not None
    assert sorted(np.asarray(counts).tolist()) == [1.0, 2.0]


def test_hexbin_rejects_c_that_does_not_match_the_points(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="c must hold one entry per point"):
        maker.hexbin(x=np.zeros(3), y=np.zeros(3), c=np.zeros(2), index=_index(maker))


def test_hist2d_draws_a_mesh_with_the_requested_bins(maker: MatplotGraphMaker) -> None:
    maker.hist2d(
        x=RNG.normal(size=200),
        y=RNG.normal(size=200),
        index=_index(maker),
        subparams=Hist2dParameters(bins=(4, 6), norm=LogNorm()),
    )
    mesh = _subplot(maker).collections[0]
    assert isinstance(mesh, QuadMesh)
    y_edge_count, x_edge_count = np.asarray(mesh.get_coordinates()).shape[:2]
    assert (x_edge_count, y_edge_count) == (5, 7)


def test_hist2d_rejects_mismatched_points(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="x and y must hold the same number of entries"):
        maker.hist2d(x=np.zeros(3), y=np.zeros(2), index=_index(maker))


@pytest.mark.parametrize(
    "build",
    [
        lambda: HistParameters(bins=0),
        lambda: HistParameters(bins=[1.0]),
        lambda: HistParameters(range=(1.0, 0.0)),
        lambda: HistParameters(rwidth=1.5),
        lambda: BoxplotParameters(whis=(90.0, 10.0)),
        lambda: BoxplotParameters(widths=0.0),
        lambda: ViolinplotParameters(points=1),
        lambda: ViolinplotParameters(bw_method=0.0),
        lambda: HexbinParameters(gridsize=(0, 3)),
        lambda: HexbinParameters(norm=LogNorm(), vmin=1.0),
        lambda: Hist2dParameters(cmin=2.0, cmax=1.0),
        lambda: Hist2dParameters(range=((1.0, 0.0), (0.0, 1.0))),
    ],
)
def test_parameters_reject_invalid_settings(build: Callable[[], object]) -> None:
    with pytest.raises(ValueError):
        build()
