# -*- coding: utf-8 -*-

"""Console script for deadend_detector."""
import argparse
import sys
import pkg_resources

VERSION = pkg_resources.get_distribution("deadend_detector").version
LICENSE = """
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
metage2metabo is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.\n
"""
MESSAGE = """
Identification of dead-end reactions (reactions whose reactants are never consumed or whose reactants are never produced) in metabolic networks.
"""
REQUIRES = """
Requires: Clyngor and/or Clyngor-with-clingo
"""


def main():
    """Console script for deadend_detector."""
    parser = argparse.ArgumentParser(
        "Deadend_detector",
        description=f"DeadEnd Detector {VERSION} {MESSAGE}",
        epilog=REQUIRES,
    )
    parser.add_argument(
        "-m",
        "--metabo",
        required=True,
        help="metabolic network in SBML format",
    )
    parser.add_argument(
        "-o", "--output", required=False, help="output file", default=None
    )
    args = parser.parse_args()

    return args


# if __name__ == "__main__":
#     main()  # pragma: no cover
