"""
Retrieval for v1_users
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/users
    """
    urlpath="/v1/users"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "id,name,email,active,usemfa"
    myresults = f'{myheader}\n'
    for myapp in results['data']:
        myuid = myapp['id']
        myname = myapp['firstName'] + ' ' + myapp['lastName']
        mymail = myapp['email']
        myactive = myapp['isActive']
        myusemfa = myapp['isMfaEnabled']
        myresults = myresults + f'{myuid},{myname},{mymail},{myactive},{myusemfa}\n'
    return myresults
