"""
Retrieval for v1_fields
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/fields
    """
    urlpath="/v1/fields"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "date,id,name,type,status"
    myresults = f'{myheader}\n'
    for myapp in results['data']:
        myuid = myapp['fieldId']
        mytype = myapp['dataType']
        myname = myapp['fieldName']
        mystate = myapp['state']
        myresults = myresults + f'{DATESTAMP},{myuid},{myname},{mytype},{mystate}\n'
    return myresults
