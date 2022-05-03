"""
Retrieval for v1_monitors_usageInfo
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/monitors/usageInfo
    """
    urlpath="/v1/monitors/usageInfo"
    body = self.get(urlpath).text
    results = json.loads(body)
    return results
