from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Self


@dataclass(frozen=True)
class Subparameters:
    """
    Immutable base class for per-plot parameter dataclasses.

    Instances are frozen so that a default instance shared between calls can
    never be changed in place; use rebuild to derive a modified copy.
    """

    def rebuild(self, **changes: object) -> Self:
        """
        Return a new instance with selected field values replaced.

        This method is non-destructive: the current instance is unchanged.

        Parameters
        ----------
        **changes: object
            The field values to replace. You can build these values in a dict
            and pass them with rebuild(**changes_dict).

        Raises
        ------
        TypeError
            If a name in changes is not a field of the dataclass.

        Examples
        --------
        >>> p = ScatterParameters(label="base")
        >>> p2 = p.rebuild(label="label")
        >>> p3 = p.rebuild(**{"label": "label"})
        """
        return replace(self, **changes)
