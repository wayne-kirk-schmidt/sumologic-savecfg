"""
Retrieval for v1_scheduledViews
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/scheduledViews
    """
    urlpath="/v1/scheduledViews"
    body = self.get(urlpath).text
    results = json.loads(body)
    return results
