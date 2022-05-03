"""
Retrieval for v1_account_status
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/account/status
    """
    urlpath="/v1/account/status"
    body = self.get(urlpath).text
    results = json.loads(body)
    return results
