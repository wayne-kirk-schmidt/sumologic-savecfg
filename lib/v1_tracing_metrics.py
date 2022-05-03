"""
Retrieval for v1_tracing_metrics
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/tracing/metrics
    """
    urlpath="/v1/tracing/metrics"
    body = self.get(urlpath).text
    results = json.loads(body)
    return results
