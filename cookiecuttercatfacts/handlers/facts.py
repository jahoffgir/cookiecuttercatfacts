"""Class for giving the facts for cats"""
# imports
import json
import os

here = os.path.dirname(os.path.realpath(__file__))

def all_facts():
    """
    Returns the cat facts from json file
    """
    with open(os.path.join(here, '../../catfacts.json')) as fact_file:
        facts = json.load(fact_file)
        return facts
