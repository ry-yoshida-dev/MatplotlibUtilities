from .keyword_enum import KeywordEnum


class Origin(KeywordEnum):
    """
    Origin position options for matplotlib imshow.
    
    Controls where the [0, 0] index of the array is placed:
    - 'upper': Place [0, 0] in the upper left corner
    - 'lower': Place [0, 0] in the lower left corner
    """
    UPPER = "upper"
    LOWER = "lower"
