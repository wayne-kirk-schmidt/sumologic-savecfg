"""
Retrieval for v1_scheduledViews
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/scheduledViews
    """
    urlpath="/v1/scheduledViews"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "date,id,name,retention"
    myresults = f'{myheader}\n'
    for myapp in results['data']:
        myuid = myapp['id']
        myretention = myapp['retentionPeriod']
        myname = myapp['indexName']
        myresults = myresults + f'{DATESTAMP},{myuid},{myname},{myretention}\n'
    return myresults
