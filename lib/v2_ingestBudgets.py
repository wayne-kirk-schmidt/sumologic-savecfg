"""
Retrieval for v2_ingestBudgets
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(source):
    """
    wrapper for HTTP get for: /v2/ingestBudgets
    """
    urlpath="/v2/ingestBudgets"
    body = source.get(urlpath).text
    results = json.loads(body)
    return results
