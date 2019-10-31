from libsbml import readSBML
import logging
import os

logger = logging.getLogger(__name__)


def read_sbml(mn_file):
    """
    Read a SBML file and yield ASP atoms
    """

    def make_reaction(reaction):
        yield f'reaction("{reaction.getId()}").'
        if reaction.getReversible() == True:
            yield f'reversible("{reaction.getId()}").'
        for reactant in reaction.getListOfReactants():
            yield f'reactant("{reactant.getSpecies()}","{reaction.getId()}").'
        for product in reaction.getListOfProducts():
            yield f'product("{product.getSpecies()}","{reaction.getId()}").'

    document = readSBML(mn_file)

    if document.getNumErrors() > 0:
        logger.critical("Encountered the following SBML errors:")
        logger.critical(document.printErrors())
        return 1

    # level = document.getLevel()
    # version = document.getVersion()

    model = document.getModel()

    for rxn in model.getListOfReactions():
        yield from make_reaction(rxn)
