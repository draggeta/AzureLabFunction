import json
import logging
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    params = {"health": "ok"}

    return func.HttpResponse(json.dumps(params), mimetype='application/json')
