import json

data = '''
{
"name":"saurav sagar",
"phone number":{
"type": "intl",
"number": "845545121562"
},
"email": {
"hide": "yes",
"value":"sauravsagar2296@gmail.com",
"email 1": {
"v1":"fsadgdsag@gmail.com",
"v2":"hgdgfcewcftrcew@gmail.com"
}
}
}'''
info=json.loads(data)
print('Name:',info['name'])
print('Hide:',info['email']['hide'])
print('email:',info['email']['email 1']['v2'])
