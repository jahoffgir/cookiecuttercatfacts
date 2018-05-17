"""Class for handling showing catfacts"""
# import statements
import json
import logging
import random
from cookiecuttercatfacts.handlers.facts import all_facts
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def handler(event, contexts):
    """
    Show handler to show the catfacts
    """
    log.debug("Received event {}".format(json.dumps(event)))
    fact = random.choice(all_facts())

    return {
        'statusCode': 200,
        'body': json.dumps({'random_fact': fact})
    }
