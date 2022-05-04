"""
Retrieval for v2_content_folders_global
"""
import sys
import json
import time
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v2/content/folders/global
    """
    urlpath="/v2/content/folders/global"
    body = self.get(urlpath).text
    jobid = json.loads(body)['id']
    jobstatusurl = f'/v2/content/folders/global/{jobid}/status'
    jobresulturl = f'/v2/content/folders/global/{jobid}/result'
    jobstatus = json.loads(self.get(jobstatusurl).text)['status']
    while jobstatus != 'Success':
        time.sleep(1)
        jobstatus = json.loads(self.get(jobstatusurl).text)['status']
        print(jobstatus)
    jobresult = json.loads(self.get(jobresulturl).text)
    myheader = "id,parentid,type,name"
    myresults = f'{myheader}\n'
    for result in jobresult['data']:
        myname = result['name']
        myuid = result['id']
        mytype = result['itemType']
        myparentid = result['parentId']
        myresults = myresults + f'{myuid},{myparentid},{myname},{mytype}\n'
    return myresults
