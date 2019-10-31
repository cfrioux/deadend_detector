import os
import clyngor
import logging

logger = logging.getLogger(__name__)


def solve(*args, **kwargs):
    "Wrapper around clyngor.solve"
    kwargs.setdefault("use_clingo_module", False)
    try:
        return clyngor.solve(*args, **kwargs)
    except FileNotFoundError as err:
        if "clingo" in err.filename:
            logger.critical(
                "ERROR binary file clingo is not accessible in the PATH."
            )
            exit(1)
        else:
            raise err
