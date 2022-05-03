"""
Retrieval for v1_apps
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/apps
    """
    urlpath="/v1/apps"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "uuid,contentid,appname"
    myresults = f'{myheader}\n'
    for myapp in results['apps']:
        myuid = myapp['appDefinition']['uuid']
        mycontentid = myapp['appDefinition']['contentId']
        myname = myapp['appDefinition']['name']
        myresults = myresults + f'{myuid},{mycontentid},{myname}\n'
    return myresults
