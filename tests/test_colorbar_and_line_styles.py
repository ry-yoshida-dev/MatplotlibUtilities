"""Colorbars built from drawn artists, line-style kwargs and level validation."""

from __future__ import annotations

from collections.abc import Iterator

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.colors import LogNorm
from matplotlib.offsetbox import AnnotationBbox

from matplotlib_utilities import (
    ColorbarExtend,
    ColorbarParameters,
    ColorMap,
    ContourfParameters,
    ContourParameters,
    GraphLayout,
    GraphParameters,
    HexbinParameters,
    HistParameters,
    ImscatterParameters,
    LineParameters,
    Location,
    MatplotGraphMaker,
    PlotParameters,
    QuiverParameters,
    StepParameters,
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


def _grid_values() -> np.ndarray:
    xx, yy = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
    values: np.ndarray = np.exp(-(xx**2) - yy**2)
    return values


def test_colorbar_shares_the_colormap_and_levels_of_the_mappable(maker: MatplotGraphMaker) -> None:
    levels = [0.0, 0.25, 0.5, 1.0]
    bands = maker.contourf(
        z=_grid_values(),
        index=_index(maker),
        subparams=ContourfParameters(levels=levels, cmap=ColorMap.MAGMA),
    )
    colorbar = maker.set_colorbar(index=_index(maker), mappable=bands)
    assert colorbar.mappable is bands
    assert colorbar.cmap.name == "magma"
    assert list(colorbar.get_ticks()) == levels


def test_colorbar_keeps_the_norm_of_the_mappable(maker: MatplotGraphMaker) -> None:
    rng = np.random.default_rng(0)
    hexagons = maker.hexbin(
        x=rng.normal(size=200),
        y=rng.normal(size=200),
        index=_index(maker),
        subparams=HexbinParameters(norm=LogNorm()),
    )
    colorbar = maker.set_colorbar(index=_index(maker), mappable=hexagons)
    assert isinstance(colorbar.norm, LogNorm)


def test_colorbar_passes_its_options_to_matplotlib(maker: MatplotGraphMaker) -> None:
    colorbar = maker.set_colorbar(
        index=_index(maker),
        image=_grid_values(),
        subparams=ColorbarParameters(
            location=Location.BOTTOM,
            extend=ColorbarExtend.BOTH,
            ticks=[0.0, 0.5, 1.0],
            label="value",
        ),
    )
    assert colorbar.orientation == "horizontal"
    assert colorbar.extend == "both"
    assert list(colorbar.get_ticks()) == [0.0, 0.5, 1.0]
    assert colorbar.ax.get_xlabel() == "value"


def test_colorbar_rejects_both_image_and_mappable(maker: MatplotGraphMaker) -> None:
    image = maker.imshow(image=_grid_values(), index=_index(maker))
    with pytest.raises(ValueError, match="cannot both be given"):
        _ = maker.set_colorbar(index=_index(maker), image=_grid_values(), mappable=image)


def test_colorbar_rejects_a_scale_that_would_be_ignored(maker: MatplotGraphMaker) -> None:
    image = maker.imshow(image=_grid_values(), index=_index(maker))
    with pytest.raises(ValueError, match="cannot be set when a mappable is given"):
        _ = maker.set_colorbar(
            index=_index(maker),
            mappable=image,
            subparams=ColorbarParameters(cmap=ColorMap.VIRIDIS),
        )


@pytest.mark.parametrize("parameters_class", [LineParameters, PlotParameters, StepParameters])
def test_line_parameters_have_no_face_or_edge_color(parameters_class: type) -> None:
    with pytest.raises(TypeError):
        _ = parameters_class(facecolor="red")


def test_quiver_parameters_keep_face_and_edge_color() -> None:
    keyword_arguments = QuiverParameters(facecolor="red", edgecolor="blue").to_dict
    assert keyword_arguments["facecolor"] == "red"
    assert keyword_arguments["edgecolor"] == "blue"


@pytest.mark.parametrize("parameters_class", [ContourParameters, ContourfParameters])
def test_contour_levels_given_as_an_array_must_increase(parameters_class: type) -> None:
    with pytest.raises(ValueError, match="strictly increasing"):
        _ = parameters_class(levels=np.array([3.0, 2.0, 1.0]))


def test_contour_levels_accept_an_increasing_array() -> None:
    parameters = ContourParameters(levels=np.array([1.0, 2.0, 3.0]))
    assert parameters.levels is not None


def test_hist_rejects_extra_colors_for_a_single_dataset(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="one entry per dataset"):
        maker.hist(x=np.arange(10.0), index=_index(maker), subparams=HistParameters(color=["r", "g", "b"]))


def test_imscatter_draws_a_frame_when_requested(maker: MatplotGraphMaker) -> None:
    maker.imscatter(
        x=np.array([0.0]),
        y=np.array([0.0]),
        images=[np.zeros((2, 2))],
        index=_index(maker),
        subparams=ImscatterParameters(is_framed=True),
    )
    image_box = maker.access_subplot(index=_index(maker)).artists[0]
    assert isinstance(image_box, AnnotationBbox)
    assert image_box.patch.get_visible()
