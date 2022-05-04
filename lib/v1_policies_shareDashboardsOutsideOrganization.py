"""
Retrieval for v1_policies_shareDashboardsOutsideOrganization
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/policies/shareDashboardsOutsideOrganization
    """
    urlpath="/v1/policies/shareDashboardsOutsideOrganization"
    body = self.get(urlpath).text
    results = json.loads(body)
    myheader = "policykey,policyvalue"
    myresults = f'{myheader}\n'
    for mykey, myvalue in results.items():
        myresults = myresults + f'{mykey},{myvalue}\n'
    return myresults
