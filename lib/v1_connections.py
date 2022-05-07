"""
Retrieval for v1_connections
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/connections
    """
    urlpath="/v1/connections"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "date,id,name,type"
    myresults = f'{myheader}\n'
    for myapp in results['data']:
        myuid = myapp['id']
        mytype = myapp['type']
        myname = myapp['name']
        myresults = myresults + f'{DATESTAMP},{myuid},{myname},{mytype}\n'
    return myresults
