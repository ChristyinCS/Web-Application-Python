from subprocess import call
import hashlib
import json
import requests
 
domain = 'example.com' # change this lane to a URL of a site you want to check
 
uuid = hashlib.md5(domain.encode('utf-8')).hexdigest()
 
result = requests.get('http://' + domain)
 
ssl_result = requests.get('https://' + domain).status_code
 
if(ssl_result == 200):
  uses_ssl = True
else:
  uses_ssl = False
 
uses_css = (result.text.find('<link rel="stylesheet"') > -1)
 
uses_js = (result.text.find('<script language="JavaScript"') > -1)    
 
profile = { 'uuid': uuid, 'name': domain, 'uses_css': uses_css, 'uses_js': uses_js }
 
print(json.dumps(profile))
 