# filelink
A cross platform and file system module for linking files.

**Currently under development. No features are guaranteed to work.**

## Goal

To provide a simple module for linking files on disk to different locations.

## Usage

This module is as simple as

```python
import filelink
filelink.create(src, dst, filelink.HARDLINK)
```
