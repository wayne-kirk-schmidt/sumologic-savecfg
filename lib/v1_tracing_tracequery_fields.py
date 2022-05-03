"""
Retrieval for v1_tracing_tracequery_fields
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/tracing/tracequery/fields
    """
    urlpath="/v1/tracing/tracequery/fields"
    body = self.get(urlpath).text
    results = json.loads(body)
    return results
