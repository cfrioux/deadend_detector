# -*- coding: utf-8 -*-
"""Allow deadend_detector to be executable through `python -m deadend_detector`."""

from __future__ import absolute_import

import sys
import logging
from shutil import which
from .cli import main
from .deadend_detector import deadenddetector

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
logging.basicConfig(
    format="%(message)s", level=logging.INFO
)  #%(name)s:%(message)s
logger = logging.getLogger(__name__)

# Check ASP binaries.
if not which("clingo"):
    logger.critical("clingo is not in the Path, m2m can not work without it.")
    logger.critical("You can install with: pip install clyngor-with-clingo")
    sys.exit(1)

if __name__ == "__main__":  # pragma: no cover
    args = main()
    deadenddetector(args.metabo, args.output)
