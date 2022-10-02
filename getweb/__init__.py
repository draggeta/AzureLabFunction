import logging
import re

import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    url = req.params.get("url")
    logging.info(f"url: {url}")
    req_url, target_url = req.url.split("=", 1)
    logging.info(f"target_url: {target_url}")

    if url:
        resp = requests.get(url=url)
        m_type = resp.headers["Content-Type"].split(";")[0]
        try:
            content = bytes.decode(resp.content, "utf-8")
            content = re.sub(r'src="(?!http)(.*?)"', f'src="{target_url}\\1"', content)
            content = re.sub(r'src="(.*?)"', f'src="{req_url}=\\1"', content)
            content = re.sub(
                r'href="(?!http)(.*?)"', f'href="{target_url}\\1"', content
            )
            content = re.sub(r'href="(.*?)"', f'href="{req_url}=\\1"', content)
        except Exception:
            content = resp.content

        return func.HttpResponse(content, mimetype=m_type)

    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a url in the query string to access the website via the url.",
            status_code=200,
        )
