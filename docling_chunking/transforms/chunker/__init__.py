#
# Copyright IBM Corp. 2024 - 2024
# SPDX-License-Identifier: MIT
#

"""Define the chunker types."""

from docling_chunking.transforms.chunker.base import BaseChunk, BaseChunker, BaseMeta
from docling_chunking.transforms.chunker.hierarchical_chunker import (
    DocMeta,
    HierarchicalChunker,
)
