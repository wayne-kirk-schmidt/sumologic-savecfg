"""
Retrieval for v1_tracing_serviceMap
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/tracing/serviceMap
    """
    urlpath="/v1/tracing/serviceMap"
    body = self.get(urlpath).text
    results = json.loads(body)
    return results
