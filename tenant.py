import json
import requests
import urllib3
from login import login
# above imports login def from login script


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def tenant(APIC, username, password, tenantName, tenantAlias, tenantDescription):

    cookie = login(APIC, username, password)
    # this is executing the def login, and the return value is the token. Which is used now as the cookie

    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    url_prepend = 'node/mo/uni/tn-{tenantName}.json'.format(tenantName=tenantName)
    url = base_url + url_prepend

    headers = { 
        'Content-Type': 'application/json',
        'connection': 'keep-alive'
    }

    prepayload = {
        "fvTenant": {
            "attributes": {
            "dn": "uni/tn-{tenantName}".format(tenantName=tenantName),
            "name": "{tenantName}".format(tenantName=tenantName),
            "nameAlias": "{tenantAlias}".format(tenantAlias=tenantAlias),
            "descr": "{tenantDescr}".format(tenantDescr=tenantDescription),
            "rn": "tn-{tenantName}".format(tenantName=tenantName),
            "status": "created"
            },
            "children": []
        }
    }


    payload = json.dumps(prepayload)

    response = requests.request(
        'POST',
        url,
        cookies=cookie,
        data=payload,
        headers=headers,
        verify=False
    )

    json_response = json.loads(response.text)
    print(json_response)
    return response.status_code

if __name__ == '__main__':
    url = 'sandboxapicdc.cisco.com'
    username = 'admin'
    password = '!v3G@!4@Y'
    tenantName = 'PythonTenant'
    tenantAlias = 'PythonTenant_Alias'
    tenantDescr = 'PythonTenant_Desc'
    print(tenant(url, username, password, tenantName, tenantAlias, tenantDescr))
    # calls in login function, passing in variables above



"""

https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-TestTenant123.json

{
  "fvTenant": {
    "attributes": {
      "dn": "uni/tn-TestTenant123",
      "name": "TestTenant123",
      "nameAlias": "Test_Alias",
      "descr": "Test_Description",
      "rn": "tn-TestTenant123",
      "status": "created"
    },
    "children": []
  }
}

"""