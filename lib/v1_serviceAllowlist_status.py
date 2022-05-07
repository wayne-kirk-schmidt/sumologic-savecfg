"""
Retrieval for v1_serviceAllowlist_status
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/serviceAllowlist/status
    """
    urlpath="/v1/serviceAllowlist/status"
    body = self.get(urlpath).text
    myheader = "date,results"
    myresults = f'{myheader}\n'
    myresults = myresults + f'{DATESTAMP},{str(body)}\n'
    return myresults
