"""
Retrieval for v1_tracing_tracequery_fields
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/tracing/tracequery/fields
    """
    urlpath="/v1/tracing/tracequery/fields"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "date,name,valuelisting"
    myresults = f'{myheader}\n'
    for myapp in results['fields']:
        myname = myapp['field']
        myvaluelisting = myapp['valueListing']
        myresults = myresults + f'{DATESTAMP},{myname},{myvaluelisting}\n'
    return myresults
