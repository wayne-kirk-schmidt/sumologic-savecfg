"""
Retrieval for v2_content_folders_personal
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v2/content/folders/personal
    """
    urlpath="/v2/content/folders/personal"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "date,id,parentid,type,name"
    myresults = f'{myheader}\n'
    myuid = results['id']
    myparentid = results['parentId']
    mytype = results['itemType']
    myname = results['name']
    myresults = myresults + f'{DATESTAMP},{myuid},{myparentid},{myname},{mytype}\n'
    return myresults
