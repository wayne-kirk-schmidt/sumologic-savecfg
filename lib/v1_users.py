"""
Retrieval for v1_users
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/users
    """
    urlpath="/v1/users"
    body = self.get(urlpath).text
    results = json.loads(body)
    return results
