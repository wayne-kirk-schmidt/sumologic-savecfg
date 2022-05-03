"""
Retrieval for v1_serviceAllowlist_addresses
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/serviceAllowlist/addresses
    """
    urlpath="/v1/serviceAllowlist/addresses"
    body = self.get(urlpath).text
    results = json.loads(body)
    return results
