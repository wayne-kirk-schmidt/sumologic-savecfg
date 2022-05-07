"""
Retrieval for v1_saml_allowlistedUsers
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/saml/allowlistedUsers
    """
    urlpath="/v1/saml/allowlistedUsers"
    body = self.get(urlpath).text
    myheader = "date,emailaddress"
    myresults = f'{myheader}\n'
    for result in body:
        myresults = myresults + f'{DATESTAMP},{str(result)}\n'
    return myresults
