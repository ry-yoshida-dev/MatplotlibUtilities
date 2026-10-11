"""Contours, pseudocolor meshes, streamlines, image scatter and spans."""

from __future__ import annotations

from collections.abc import Callable, Iterator

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.axes import Axes
from matplotlib.collections import QuadMesh
from matplotlib.contour import ContourSet
from matplotlib.offsetbox import AnnotationBbox
from matplotlib.patches import Rectangle
from PIL import Image

from matplotlib_utilities import (
    ColorMap,
    ContourfParameters,
    ContourParameters,
    GraphLayout,
    GraphParameters,
    ImscatterParameters,
    MatplotGraphMaker,
    Orientation,
    PcolormeshParameters,
    Shading,
    SpanParameters,
    StreamplotParameters,
    SubplotIndex,
)

GRID_X, GRID_Y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 8))
GRID_Z = GRID_X**2 + GRID_Y**2


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


def _contour_set(maker: MatplotGraphMaker) -> ContourSet:
    contour_sets = [artist for artist in _subplot(maker).collections if isinstance(artist, ContourSet)]
    assert len(contour_sets) == 1
    return contour_sets[0]


def test_contour_uses_the_given_levels(maker: MatplotGraphMaker) -> None:
    maker.contour(
        z=GRID_Z,
        x=GRID_X,
        y=GRID_Y,
        index=_index(maker),
        subparams=ContourParameters(levels=[0.25, 0.5, 1.0], colors="black"),
    )
    assert np.asarray(_contour_set(maker).levels).tolist() == [0.25, 0.5, 1.0]


def test_contour_labels_the_lines_on_request(maker: MatplotGraphMaker) -> None:
    maker.contour(z=GRID_Z, index=_index(maker), is_labeled=True, subparams=ContourParameters(levels=[0.5]))
    assert len(_subplot(maker).texts) > 0


def test_contourf_fills_between_levels(maker: MatplotGraphMaker) -> None:
    maker.contourf(z=GRID_Z, index=_index(maker), subparams=ContourfParameters(levels=[0.0, 1.0, 2.0]))
    assert _contour_set(maker).filled


@pytest.mark.parametrize(
    ("z", "x", "y", "message"),
    [
        (np.zeros(5), None, None, "z must be a 2-D array"),
        (GRID_Z, GRID_X, None, "x and y must both be provided or both omitted"),
    ],
)
def test_contour_rejects_invalid_grids(
    maker: MatplotGraphMaker,
    z: np.ndarray,
    x: np.ndarray | None,
    y: np.ndarray | None,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        maker.contour(z=z, x=x, y=y, index=_index(maker))


def test_pcolormesh_draws_one_cell_per_value(maker: MatplotGraphMaker) -> None:
    maker.pcolormesh(
        z=GRID_Z,
        x=GRID_X,
        y=GRID_Y,
        index=_index(maker),
        subparams=PcolormeshParameters(shading=Shading.NEAREST, cmap=ColorMap.VIRIDIS),
    )
    mesh = _subplot(maker).collections[0]
    assert isinstance(mesh, QuadMesh)
    assert np.asarray(mesh.get_array()).size == GRID_Z.size


def test_streamplot_colors_by_data(maker: MatplotGraphMaker) -> None:
    maker.streamplot(
        x=np.linspace(-1, 1, 10),
        y=np.linspace(-1, 1, 8),
        u=-GRID_Y,
        v=GRID_X,
        color_values=GRID_Z,
        index=_index(maker),
        subparams=StreamplotParameters(cmap=ColorMap.PLASMA),
    )
    assert _subplot(maker).collections[0].get_array() is not None


def test_streamplot_rejects_color_values_with_a_fixed_color(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="color_values cannot be combined with a fixed color"):
        maker.streamplot(
            x=np.linspace(-1, 1, 10),
            y=np.linspace(-1, 1, 8),
            u=-GRID_Y,
            v=GRID_X,
            color_values=GRID_Z,
            index=_index(maker),
            subparams=StreamplotParameters(color="black"),
        )


def test_streamplot_rejects_mismatched_components(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="u and v must be 2-D arrays of the same shape"):
        maker.streamplot(
            x=np.linspace(-1, 1, 10),
            y=np.linspace(-1, 1, 8),
            u=GRID_X,
            v=GRID_X[:, :5],
            index=_index(maker),
        )


def _image_boxes(maker: MatplotGraphMaker) -> list[AnnotationBbox]:
    return [artist for artist in _subplot(maker).artists if isinstance(artist, AnnotationBbox)]


def test_imscatter_repeats_a_single_image_at_every_point(maker: MatplotGraphMaker) -> None:
    maker.imscatter(
        x=np.array([0.0, 5.0, 10.0]),
        y=np.array([0.0, 1.0, 2.0]),
        images=[np.zeros((4, 4))],
        index=_index(maker),
        subparams=ImscatterParameters(zoom=2.0, cmap=ColorMap.GRAY, zorder=3.0),
    )
    boxes = _image_boxes(maker)
    assert [box.xy for box in boxes] == [(0.0, 0.0), (5.0, 1.0), (10.0, 2.0)]
    assert all(box.get_zorder() == pytest.approx(3.0) for box in boxes)
    x_lower, x_upper = _subplot(maker).get_xlim()
    assert x_lower <= 0.0 and x_upper >= 10.0


def test_imscatter_accepts_pil_images(maker: MatplotGraphMaker) -> None:
    pil_image = Image.new("RGB", (4, 4), color="red")
    maker.imscatter(
        x=np.array([0.0, 1.0]),
        y=np.array([0.0, 1.0]),
        images=[pil_image, pil_image],
        index=_index(maker),
    )
    assert len(_image_boxes(maker)) == 2


def test_imscatter_rejects_images_that_do_not_match_the_points(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="images must hold one image or one image per point"):
        maker.imscatter(
            x=np.arange(3.0),
            y=np.arange(3.0),
            images=[np.zeros((2, 2)), np.zeros((2, 2))],
            index=_index(maker),
        )


@pytest.mark.parametrize(
    ("orientation", "expected_x", "expected_y"),
    [
        (Orientation.VERTICAL, (2.0, 4.0), (0.0, 1.0)),
        (Orientation.HORIZONTAL, (0.0, 1.0), (2.0, 4.0)),
    ],
)
def test_span_shades_the_selected_range(
    maker: MatplotGraphMaker,
    orientation: Orientation,
    expected_x: tuple[float, float],
    expected_y: tuple[float, float],
) -> None:
    maker.span(
        start=2.0,
        end=4.0,
        orientation=orientation,
        index=_index(maker),
        subparams=SpanParameters(color="orange", alpha=0.3),
    )
    band = _subplot(maker).patches[0]
    assert isinstance(band, Rectangle)
    x_values = (band.get_x(), band.get_x() + band.get_width())
    y_values = (band.get_y(), band.get_y() + band.get_height())
    assert x_values == pytest.approx(expected_x)
    assert y_values == pytest.approx(expected_y)


def test_span_rejects_an_empty_range(maker: MatplotGraphMaker) -> None:
    with pytest.raises(ValueError, match="start must be less than end"):
        maker.span(start=1.0, end=1.0, orientation=Orientation.VERTICAL, index=_index(maker))


@pytest.mark.parametrize(
    "build",
    [
        lambda: ContourParameters(levels=0),
        lambda: ContourParameters(levels=[1.0, 0.5]),
        lambda: ContourParameters(colors="black", cmap=ColorMap.VIRIDIS),
        lambda: ContourParameters(linewidths=0.0),
        lambda: PcolormeshParameters(linewidth=-1.0),
        lambda: StreamplotParameters(density=0.0),
        lambda: StreamplotParameters(minlength=2.0, maxlength=1.0),
        lambda: ImscatterParameters(zoom=0.0),
        lambda: SpanParameters(linewidth=-1.0),
    ],
)
def test_parameters_reject_invalid_settings(build: Callable[[], object]) -> None:
    with pytest.raises(ValueError):
        build()
