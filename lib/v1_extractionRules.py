"""
Retrieval for v1_extractionRules
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/extractionRules
    """
    urlpath="/v1/extractionRules"
    body = self.get(urlpath).text
    ### results = json.loads(body)
    ### return results
    return body
