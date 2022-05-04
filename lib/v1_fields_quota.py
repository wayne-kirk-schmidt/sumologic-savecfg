"""
Retrieval for v1_fields_quota
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/fields/quota
    """
    urlpath="/v1/fields/quota"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "fieldkey,fieldvalue"
    myresults = f'{myheader}\n'
    for mykey, myvalue in results.items():
        myresults = myresults + f'{mykey},{myvalue}\n'
    return myresults
