from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from enum import Enum
from typing import cast

from .subparameter import Subparameters
from .utils import KeywordEnum, Linestyle


@dataclass(frozen=True)
class KeywordSubparameters[KeywordArgumentsT: Mapping[str, object]](Subparameters):
    """
    Parameters that are unpacked into a Matplotlib call as keyword arguments.

    KeywordArgumentsT is a TypedDict that lists every field under the
    keyword Matplotlib expects, so type checkers verify the unpacked
    arguments against the Matplotlib signature. Fields set to None are
    omitted, KeywordEnum and Linestyle members are replaced by their raw values, and
    nested KeywordSubparameters become nested dicts (for example wedgeprops).
    """

    @property
    def to_dict(self) -> KeywordArgumentsT:
        """
        Return the fields that are set as Matplotlib keyword arguments.

        Returns
        -------
        KeywordArgumentsT
            The keyword arguments, without the fields left as None.

        Raises
        ------
        TypeError
            If a field holds an Enum that is not a KeywordEnum, whose value
            Matplotlib would not understand.
        """
        attributes: dict[str, object] = vars(self)
        keyword_arguments: dict[str, object] = {
            name: _to_keyword_value(value) for name, value in attributes.items() if value is not None
        }
        return cast(KeywordArgumentsT, keyword_arguments)


def _to_keyword_value(value: object) -> object:
    match value:
        case KeywordEnum() | Linestyle():
            return value.value
        case Enum():
            raise TypeError(f"{type(value).__name__} must derive from KeywordEnum to be passed to Matplotlib")
        case KeywordSubparameters():
            nested_arguments: Mapping[str, object] = value.to_dict
            return nested_arguments
        case list():
            return [_to_keyword_value(item) for item in cast(list[object], value)]
        case tuple():
            return tuple(_to_keyword_value(member) for member in cast(tuple[object, ...], value))
        case _:
            return value
