"""
Retrieval for v1_monitors_usageInfo
"""
import sys
import json
import datetime
RIGHTNOW = datetime.datetime.now()
DATESTAMP = RIGHTNOW.strftime('%Y%m%d')
sys.dont_write_bytecode = 1

def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/monitors/usageInfo
    """
    urlpath="/v1/monitors/usageInfo"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "date,usagekey,usagevalue"
    myresults = f'{myheader}\n'
    for mytype in results:
        montype = mytype['monitorType']
        for mykey, myvalue in mytype.items():
            mykey = f'{montype}-{mykey}'
            myresults = myresults + f'{DATESTAMP},{mykey},{myvalue}\n'
    return myresults
