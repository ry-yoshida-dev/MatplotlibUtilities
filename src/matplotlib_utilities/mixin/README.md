# mixin

## Overview

Methods of `MatplotGraphMaker`, split into mixins it inherits; callers use them as flat methods on the maker (`maker.scatter`, `maker.set_label`).

## Components

| Component | Description |
| --------- | ----------- |
| [`draw/`](./draw/README.md) | `DrawMixin`, which plots data and decorations on subplots |
| [`axis/`](./axis/README.md) | `AxisMixin`, which sets labels, limits, ticks, titles and grids |
