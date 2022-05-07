"""
Retrieval for v2_ingestBudgets
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(source):
    """
    wrapper for HTTP get for: /v2/ingestBudgets
    """
    urlpath="/v2/ingestBudgets"
    body = source.get(urlpath).text
    myheader = "date,results"
    myresults = f'{myheader}\n'
    myresults = myresults + f'{DATESTAMP},{body}\n'
    return myresults
