"""
Retrieval for v1_policies_audit
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/policies/audit
    """
    urlpath="/v1/policies/audit"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "date,policykey,policyvalue"
    myresults = f'{myheader}\n'
    for mykey, myvalue in results.items():
        myresults = myresults + f'{DATESTAMP},{mykey},{myvalue}\n'
    return myresults
