# Azure Labs Function

A function for my [Azure Lab](https://github.com/draggeta/AzureLab) for use from exercise 7 onwards.

## Endpoints

This function contains three endpoints:

* `api/health`: always returns
```json
{"health": "ok"}
```
* `api/info`: returns
```json
{"service": "Finance API", "resourceGroup": "<name>", "server": "<server>"}
```
* `api/getweb?url=<url>` returns the requested content. It's a poor man's proxy.
