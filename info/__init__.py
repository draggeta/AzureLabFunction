import json
import logging
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    params = {
        "service": "Finance API",
        "resourceGroup": os.getenv("WEBSITE_RESOURCE_GROUP", ""),
        "server": os.getenv("WEBSITE_HOSTNAME", ""),
    }

    return func.HttpResponse(json.dumps(params))
