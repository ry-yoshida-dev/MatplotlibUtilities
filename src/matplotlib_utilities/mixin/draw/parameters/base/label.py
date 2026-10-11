from dataclasses import dataclass


@dataclass(frozen=True)
class LabelParameters:
    """
    Common label keyword argument for matplotlib artists and related API.
    """

    label: str | None = None
