"""
Retrieval for v1_fields_builtin
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/fields/builtin
    """
    urlpath="/v1/fields/builtin"
    body = self.get(urlpath).text
    results = json.loads(body)
    return results
