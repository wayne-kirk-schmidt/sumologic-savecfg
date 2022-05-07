"""
Retrieval for v1_roles
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/roles
    """
    urlpath="/v1/roles"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "date,id,name,capability"
    myresults = f'{myheader}\n'
    for myapp in results['data']:
        myuid = myapp['id']
        myname = myapp['name']
        for myability in myapp['capabilities']:
            myresults = myresults + f'{DATESTAMP},{myuid},{myname},{myability}\n'
    return myresults
