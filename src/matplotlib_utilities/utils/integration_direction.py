from .keyword_enum import KeywordEnum


class IntegrationDirection(KeywordEnum):
    """
    Direction in which streamlines are traced from their seed points.

    Attributes:
    ----------
    FORWARD: Follow the vector field.
    BACKWARD: Trace against the vector field.
    BOTH: Trace in both directions.
    """
    FORWARD = "forward"
    BACKWARD = "backward"
    BOTH = "both"
