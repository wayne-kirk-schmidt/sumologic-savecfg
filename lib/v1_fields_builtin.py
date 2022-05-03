"""
Retrieval for v1_fields_builtin
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/fields/builtin
    """
    urlpath="/v1/fields/builtin"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "id,name,type,status"
    myresults = f'{myheader}\n'
    for myapp in results['data']:
        myuid = myapp['fieldId']
        mytype = myapp['dataType']
        myname = myapp['fieldName']
        mystate = myapp['state']
        myresults = myresults + f'{myuid},{myname},{mytype},{mystate}\n'
    return myresults
