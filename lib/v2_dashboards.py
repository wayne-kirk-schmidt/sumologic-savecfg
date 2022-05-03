"""
Retrieval for v2_dashboards
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v2/dashboards
    """
    urlpath="/v2/dashboards"
    body = self.get(urlpath).text
    results = json.loads(body)
    return results
