from collections.abc import Sized


class ArgumentValidator:
    """
    Shape checks shared by the draw mixins before data reaches Matplotlib.
    """

    @staticmethod
    def require_equal_length(first_name: str, first: Sized, second_name: str, second: Sized) -> None:
        """
        Require two arguments to hold the same number of entries.

        Raises
        ------
        ValueError
            If the lengths differ.
        """
        if len(first) != len(second):
            raise ValueError(
                f"{first_name} and {second_name} must hold the same number of entries, "
                + f"given {len(first)} and {len(second)}"
            )

    @staticmethod
    def require_both_or_neither(x: object | None, y: object | None) -> None:
        """
        Require x and y to be given together or omitted together.

        Raises
        ------
        ValueError
            If exactly one of x and y is given.
        """
        if (x is None) != (y is None):
            raise ValueError("x and y must both be provided or both omitted")
