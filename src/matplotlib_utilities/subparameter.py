from __future__ import annotations
from abc import ABC
from dataclasses import dataclass, replace, Field, fields
from typing import Any, TypeVar


_SubparametersT = TypeVar("_SubparametersT", bound="Subparameters")


@dataclass
class Subparameters(ABC):
    """
    Base class for matplotlib kwarg dataclasses.

    Subclasses inherit to_dict by iterating dataclass fields. Override
    _to_dict_skip_field only when omit rules differ from the default (omit None).
    Enum-like values with a .value attribute are unwrapped in to_dict, and
    nested Subparameters become nested dicts (for example wedgeprops).
    """

    def _to_dict_skip_field(self, field: Field[Any], value: Any) -> bool:
        """When True, the field is omitted from the dict returned by to_dict."""
        return value is None

    def rebuild(self: _SubparametersT, **changes: Any) -> _SubparametersT:
        """
        Return a new instance with selected field values replaced.

        This method is non-destructive: the current instance is unchanged.

        Parameters
        ----------
        **changes: Any
            The field values to replace. You can build these values in a dict
            and pass them with rebuild(**changes_dict).

        Examples
        --------
        >>> p = ScatterParameters(label="base")
        >>> p2 = p.rebuild(label="label")
        >>> p3 = p.rebuild(**{"label": "label"})
        """
        return replace(self, **changes)

    @property
    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for f in fields(self):
            val = getattr(self, f.name)
            if self._to_dict_skip_field(f, val):
                continue
            if isinstance(val, Subparameters):
                out[f.name] = val.to_dict
            elif hasattr(val, "value"):
                out[f.name] = val.value
            else:
                out[f.name] = val
        return out
