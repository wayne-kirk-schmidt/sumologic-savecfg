"""
Retrieval for v1_apps
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/apps
    """
    urlpath="/v1/apps"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "date,id,name,uuid"
    myresults = f'{myheader}\n'
    for myapp in results['apps']:
        myuid = myapp['appDefinition']['uuid']
        mycontentid = myapp['appDefinition']['contentId']
        myname = myapp['appDefinition']['name']
        myresults = myresults + f'{DATESTAMP},{mycontentid},{myname},{myuid}\n'
    return myresults
