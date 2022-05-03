"""
Retrieval for v2_content_folders_adminRecommended
"""
import sys
import json
sys.dont_write_bytecode = 1
def get_and_format_output(self):
    """
    wrapper for HTTP get for: /v2/content/folders/adminRecommended
    """
    urlpath="/v2/content/folders/adminRecommended"
    body = self.get(urlpath).text
    results = json.loads(body)
    return results
