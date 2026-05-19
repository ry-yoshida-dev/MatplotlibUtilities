# mixin

## Overview

Mixins add methods to [`MatplotGraphMaker`](../maker.py) without growing a single giant class file. `MatplotGraphMaker` inherits [`DrawMixin`](./draw/mixin.py) and [`AxisMixin`](./axis/mixin.py); callers use flat methods on the maker (`maker.scatter`, `maker.set_label`, …).

| Mixin | Role |
| ----- | ---- |
| [`DrawMixin`](./draw/mixin.py) | Plot data and decorations on subplots |
| [`AxisMixin`](./axis/mixin.py) | Labels, limits, title, grid, tick visibility |

Detailed examples and API maps: [`draw/README.md`](./draw/README.md), [`axis/README.md`](./axis/README.md).

## Components

| Path | Contents |
| ---- | -------- |
| [`draw/`](./draw/) | [`DrawMixin`](./draw/mixin.py), [`draw/mixins/`](./draw/mixins/) (image / series / vector), [`draw/parameters/`](./draw/parameters/) (`*Parameters` → `to_dict`) |
| [`axis/`](./axis/) | [`AxisMixin`](./axis/mixin.py); [`axis/parameters/`](./axis/parameters/) (`GridParameters`, `TickParamsParameters`) |
