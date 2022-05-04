"""
Retrieval for v1_saml_allowlistedUsers
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v1/saml/allowlistedUsers
    """
    urlpath="/v1/saml/allowlistedUsers"
    body = self.get(urlpath).text
    ### results = json.loads(body)
    ### return results
    return body
