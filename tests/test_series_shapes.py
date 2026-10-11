"""Step, error bar, filled-area and stacked-area plots."""

from __future__ import annotations

from collections.abc import Callable, Iterator

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.axes import Axes

from matplotlib_utilities import (
    ErrorbarParameters,
    FillBetweenParameters,
    GraphLayout,
    GraphParameters,
    MatplotGraphMaker,
    StackBaseline,
    StackplotParameters,
    StepParameters,
    StepWhere,
    SubplotIndex,
)


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


def test_step_sets_the_drawstyle_from_where(maker: MatplotGraphMaker) -> None:
    maker.step(
        x=np.arange(3.0),
        y=np.arange(3.0),
        index=_index(maker),
        subparams=StepParameters(where=StepWhere.POST),
    )
    assert _subplot(maker).lines[0].get_drawstyle() == "steps-post"


def test_step_rejects_mismatched_data(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="x and y must hold the same number of entries"):
        maker.step(x=np.arange(3.0), y=np.arange(2.0), index=_index(maker))


def test_step_parameters_have_no_drawstyle() -> None:
    with pytest.raises(TypeError, match="drawstyle"):
        _ = StepParameters(**{"drawstyle": "default"})


def test_errorbar_draws_one_bar_per_point(maker: MatplotGraphMaker) -> None:
    maker.errorbar(
        x=np.arange(4.0),
        y=np.arange(4.0),
        yerr=np.full(4, 0.5),
        index=_index(maker),
        subparams=ErrorbarParameters(capsize=3.0),
    )
    error_lines = _subplot(maker).collections[0]
    assert len(error_lines.get_paths()) == 4


def test_errorbar_accepts_asymmetric_errors(maker: MatplotGraphMaker) -> None:
    maker.errorbar(
        x=np.arange(3.0),
        y=np.zeros(3),
        yerr=np.array([[0.1, 0.2, 0.3], [1.0, 1.0, 1.0]]),
        index=_index(maker),
    )
    lower_end = np.asarray(_subplot(maker).collections[0].get_paths()[2].vertices)[:, 1].min()
    assert lower_end == pytest.approx(-0.3)


@pytest.mark.parametrize(
    ("yerr", "message"),
    [
        (None, "at least one of yerr and xerr"),
        (np.ones(2), "yerr must hold one entry per point"),
        (np.array([-1.0, 1.0, 1.0]), "yerr must be non-negative"),
    ],
)
def test_errorbar_rejects_invalid_errors(
    maker: MatplotGraphMaker,
    yerr: np.ndarray | None,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        maker.errorbar(x=np.arange(3.0), y=np.arange(3.0), yerr=yerr, index=_index(maker))


def test_fill_between_fills_the_band(maker: MatplotGraphMaker) -> None:
    maker.fill_between(
        x=np.arange(3.0),
        y1=np.zeros(3),
        y2=np.ones(3),
        index=_index(maker),
        subparams=FillBetweenParameters(alpha=0.3, label="band"),
    )
    band = _subplot(maker).collections[0]
    vertices = np.asarray(band.get_paths()[0].vertices)
    assert vertices[:, 1].min() == pytest.approx(0.0)
    assert vertices[:, 1].max() == pytest.approx(1.0)
    assert band.get_label() == "band"


def test_fill_between_rejects_a_mask_of_the_wrong_length(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="where must hold one entry per x value"):
        maker.fill_between(
            x=np.arange(3.0),
            y1=np.zeros(3),
            where=np.array([True, False]),
            index=_index(maker),
        )


def test_stackplot_stacks_each_layer_on_the_previous(maker: MatplotGraphMaker) -> None:
    maker.stackplot(
        x=np.arange(3.0),
        ys=[np.ones(3), np.full(3, 2.0)],
        index=_index(maker),
        labels=["a", "b"],
        subparams=StackplotParameters(baseline=StackBaseline.ZERO),
    )
    layers = _subplot(maker).collections
    assert len(layers) == 2
    assert np.asarray(layers[1].get_paths()[0].vertices)[:, 1].max() == pytest.approx(3.0)
    assert [layer.get_label() for layer in layers] == ["a", "b"]


@pytest.mark.parametrize(
    ("ys", "labels", "message"),
    [
        ([], None, "ys must hold at least one series"),
        ([np.ones(2)], None, r"ys\[0\] must hold one entry per x value"),
        ([np.ones(3)], ["a", "b"], "labels must hold one entry per series"),
    ],
)
def test_stackplot_rejects_invalid_series(
    maker: MatplotGraphMaker,
    ys: list[np.ndarray],
    labels: list[str] | None,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        maker.stackplot(x=np.arange(3.0), ys=ys, index=_index(maker), labels=labels)


@pytest.mark.parametrize(
    "build",
    [
        lambda: ErrorbarParameters(capsize=-1.0),
        lambda: ErrorbarParameters(errorevery=0),
        lambda: FillBetweenParameters(linewidth=-1.0),
        lambda: FillBetweenParameters(alpha=2.0),
        lambda: StackplotParameters(linewidth=-1.0),
    ],
)
def test_parameters_reject_invalid_settings(build: Callable[[], object]) -> None:
    with pytest.raises(ValueError):
        build()
