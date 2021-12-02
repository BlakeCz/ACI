import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def login (url, username, password):
    base_url = 'https://{ApicURL}/api/'.format(ApicURL=url)

    # create credentials structure
    name_pwd = {
        'aaaUser':
            {'attributes': 
                {'name': '{username}'.format(username=username), 
                'pwd': '{password}'.format(password=password)
                }
            }
                }

    # json.dumps returns a string vlaue 
    json_credentials = json.dumps(name_pwd)
    # log in to API
    url = base_url + 'aaaLogin.json'

    headers = { 
        'content-type': 'application/json'
    }
    try:
        # requets module allows you to send http requests
        response = requests.request(
            'POST',
            url,
            headers=headers,
            data=json_credentials,
            timeout=2,
            verify=False
        )

        data = json.loads(response.text)
        # token must be dictionary, so blank one created
        token = {}
        token['APIC-Cookie']= data["imdata"][0]["aaaLogin"]["attributes"]["token"]
        return token

        # print(json.dumps(data, indent=4, sort_keys=True))



        # post_response = requests.post(login_url, data=json_credentials)
        # # get token from login response structure
        # auth = json.loads(post_response.text)
        # login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
        # auth_token = login_attributes['token']

    except:
        print('Error occured')

if __name__ == '__main__':
    url = 'sandboxapicdc.cisco.com'
    username = 'admin'
    password = '!v3G@!4@Y'
    print(login(url, username, password))
    # calls in login function, passing in variables above