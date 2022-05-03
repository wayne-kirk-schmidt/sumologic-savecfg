"""
Retrieval for v1_tokens
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/tokens
    """
    urlpath="/v1/tokens"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "id,name,type,status"
    myresults = f'{myheader}\n'
    for myapp in results['data']:
        myuid = myapp['id']
        mytype = myapp['type']
        myname = myapp['name']
        mystate = myapp['status']
        myresults = myresults + f'{myuid},{myname},{mytype},{mystate}\n'
    return myresults
