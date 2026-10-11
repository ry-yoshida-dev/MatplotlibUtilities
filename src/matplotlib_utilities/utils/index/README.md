# utils.index

## Overview

Types for **addressing subplots** inside a flattened axes array. `MatplotGraphMaker` accepts a `SubplotIndex`, which is either a zero-based subplot number in row-major order (an `int`) or an explicit row/column pair. Every drawing and axis method defaults to subplot `0`. Import `SubplotIndex` from `matplotlib_utilities` (re-exported from `utils`).

## Components

| Component | Description |
| --------- | ----------- |
| [`row_column_index.py`](./row_column_index.py) | `RowColumnIndex`: zero-based row and column indices |
| [`subplot_index.py`](./subplot_index.py) | `SubplotIndex = RowColumnIndex \| int` type alias |
