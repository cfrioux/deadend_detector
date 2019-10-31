# -*- coding: utf-8 -*-
import os
import logging
import clyngor
from clyngor import opt_models_from_clyngor_answers
from pkg_resources import resource_filename
from . import sbml
from .utils import solve


logger = logging.getLogger(__name__)

ASP_DED = resource_filename(__name__, "asp/deadends.lp")
assert os.path.exists(ASP_DED)


def deadenddetector(metabolicnetwork, output_file=None):
    """
    identify dead ends in a metabolic network
    """
    asp_atoms = "\n".join(sbml.read_sbml(metabolicnetwork))
    with open("plop.txt", "w") as f:
        f.write(asp_atoms)
    # models = solve(ASP_DED, inline=asp_atoms)
    models = clyngor.solve(ASP_DED, inline=asp_atoms)
    for model in models.discard_quotes.by_arity:
        best_model = model
    non_consumed = []
    non_produced = []
    for pred in best_model:
        if pred == "deadend_np":
            [non_produced.append(a[0]) for a in best_model[pred, 1]]
        elif pred == "deadend_nc":
            [non_consumed.append(a[0]) for a in best_model[pred, 1]]
    logger.info(
        f"{len(non_consumed)} non-consumed metabolites: \n {', '.join(non_consumed)}"
    )
    logger.info(
        f"{len(non_produced)} non-produced metabolites: \n {', '.join(non_produced)}"
    )

    if output_file:
        try:
            with open(output_file, "w") as f:
                for i in non_produced:
                    f.write(f"{i}\tnon produced\n")
                for i in non_consumed:
                    f.write(f"{i}\tnon consumed\n")
            logger.info(f"Results written in {output_file}")
        except:
            logger.critical(f"Could not write results in {output_file}")
            return 1
    return 0
