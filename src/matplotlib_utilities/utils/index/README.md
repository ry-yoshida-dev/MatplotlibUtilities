# index

## Overview

Types that address a subplot: a zero-based subplot number in row-major order, or a row and column pair. Every drawing and axis method defaults to subplot `0`.

## Components

| Component | Description |
| --------- | ----------- |
| [`row_column_index.py`](./row_column_index.py) | `RowColumnIndex`: zero-based row and column indices |
| [`subplot_index.py`](./subplot_index.py) | `SubplotIndex = RowColumnIndex \| int` type alias |
