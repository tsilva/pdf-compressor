"""Compression strategy implementations."""

from pdf_compressor.core.strategies.base import CompressionStrategy, CompressionResult
from pdf_compressor.core.strategies.pikepdf_strategy import PikepdfStrategy
from pdf_compressor.core.strategies.ghostscript_strategy import GhostscriptStrategy
from pdf_compressor.core.strategies.combined_strategy import CombinedStrategy

__all__ = [
    "CompressionStrategy",
    "CompressionResult",
    "PikepdfStrategy",
    "GhostscriptStrategy",
    "CombinedStrategy",
]
