"""
Retrieval for v1_transformationRules
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/transformationRules
    """
    urlpath="/v1/transformationRules"
    body = self.get(urlpath).text
    myheader = "date,results"
    myresults = f'{myheader}\n'
    myresults = myresults + f'{DATESTAMP},{body}\n'
    return myresults
