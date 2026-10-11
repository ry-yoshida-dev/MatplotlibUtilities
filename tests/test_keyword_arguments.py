"""Consistency between parameter dataclasses and the TypedDicts their to_dict returns."""

from __future__ import annotations

import dataclasses
import types
import typing
from collections.abc import Iterator

import pytest

import matplotlib_utilities.mixin.axis.parameters as axis_parameters
import matplotlib_utilities.mixin.draw.parameters as draw_parameters
from matplotlib_utilities import (
    AnnotateParameters,
    ArrowProperties,
    ContourfParameters,
    CoordinateSystem,
    Hatch,
    KeywordEnum,
    KeywordSubparameters,
    LineParameters,
    Linestyle,
    PlotParameters,
)


def _keyword_parameter_classes() -> list[type]:
    classes: list[type] = []
    for module in (draw_parameters, axis_parameters):
        for name in module.__all__:
            candidate: object = getattr(module, name)
            if isinstance(candidate, type) and issubclass(candidate, KeywordSubparameters):
                classes.append(candidate)
    return classes


def _typed_dict_of(parameters_class: type) -> type:
    for base in types.get_original_bases(parameters_class):
        if typing.get_origin(base) is KeywordSubparameters:
            typed_dict: type = typing.get_args(base)[0]
            return typed_dict
    raise TypeError(f"{parameters_class.__name__} does not parametrize KeywordSubparameters directly")


def _union_members(annotation: object) -> Iterator[object]:
    if typing.get_origin(annotation) in (typing.Union, types.UnionType):
        for member in typing.get_args(annotation):
            yield from _union_members(member)
    else:
        yield annotation


KEYWORD_PARAMETER_CLASSES = _keyword_parameter_classes()


def test_every_keyword_parameter_class_is_collected() -> None:
    assert len(KEYWORD_PARAMETER_CLASSES) == 29


@pytest.mark.parametrize("parameters_class", KEYWORD_PARAMETER_CLASSES, ids=lambda cls: cls.__name__)
def test_typed_dict_keys_match_dataclass_fields(parameters_class: type) -> None:
    typed_dict = _typed_dict_of(parameters_class)
    keys: frozenset[str] = typed_dict.__required_keys__ | typed_dict.__optional_keys__
    assert keys == {field.name for field in dataclasses.fields(parameters_class)}


@pytest.mark.parametrize("parameters_class", KEYWORD_PARAMETER_CLASSES, ids=lambda cls: cls.__name__)
def test_typed_dict_literals_cover_enum_values(parameters_class: type) -> None:
    field_types = typing.get_type_hints(parameters_class)
    keyword_types = typing.get_type_hints(_typed_dict_of(parameters_class))
    for name, field_type in field_types.items():
        enum_classes = [
            member
            for member in _union_members(field_type)
            if isinstance(member, type) and issubclass(member, KeywordEnum)
        ]
        literal_values = {
            value
            for member in _union_members(keyword_types[name])
            if typing.get_origin(member) is typing.Literal
            for value in typing.get_args(member)
        }
        if not enum_classes or not literal_values:
            continue
        for enum_class in enum_classes:
            assert {member.value for member in enum_class} <= literal_values, f"{parameters_class.__name__}.{name}"


def test_parameters_are_immutable() -> None:
    parameters = PlotParameters(label="base")
    field_name = "label"
    with pytest.raises(dataclasses.FrozenInstanceError):
        setattr(parameters, field_name, "changed")
    assert parameters.rebuild(label="changed").label == "changed"
    assert parameters.label == "base"


def test_nested_arrow_properties_become_a_dict() -> None:
    parameters = AnnotateParameters(arrowprops=ArrowProperties())
    assert parameters.to_dict == {"arrowprops": {"arrowstyle": "->"}}


def test_enums_inside_a_sequence_are_unwrapped() -> None:
    parameters = ContourfParameters(hatches=[Hatch.DOT, None])
    assert parameters.to_dict["hatches"] == [".", None]


def test_dash_pattern_linestyle_is_passed_as_a_tuple() -> None:
    parameters = LineParameters(linestyle=Linestyle.LOOSELY_DOTTED)
    assert parameters.to_dict["linestyle"] == (0, (1, 10))


def test_annotation_point_rejects_an_offset_system() -> None:
    with pytest.raises(ValueError, match="xycoords"):
        _ = AnnotateParameters(xycoords=CoordinateSystem.OFFSET_POINTS)
