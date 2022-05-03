"""
Retrieval for v1_accessKeys
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/accessKeys
    """
    urlpath="/v1/accessKeys"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "id,name,author"
    myresults = f'{myheader}\n'
    for myapp in results['data']:
        myuid = myapp['id']
        myname = myapp['label']
        myauthor = myapp['createdBy']
        myresults = myresults + f'{myuid},{myname},{myauthor}\n'
    return myresults
