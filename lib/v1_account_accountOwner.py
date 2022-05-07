"""
Retrieval for v1_account_accountOwner
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/account/accountOwner
    """
    urlpath="/v1/account/accountOwner"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "date,userid"
    myresults = f'{myheader}\n'
    myresults = myresults + f'{DATESTAMP},{results}\n'
    return myresults
