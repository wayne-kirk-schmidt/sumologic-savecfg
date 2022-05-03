"""
Retrieval for v1_partitions
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/partitions
    """
    urlpath="/v1/partitions"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "id,name,retention,tier"
    myresults = f'{myheader}\n'
    for myapp in results['data']:
        myuid = myapp['id']
        myretention = myapp['retentionPeriod']
        myname = myapp['name']
        mytier = myapp['analyticsTier']
        myresults = myresults + f'{myuid},{myname},{myretention},{mytier}\n'
    return myresults
