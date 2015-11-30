import json

data='''{
"name":"jaifar",
"phone":{
    "type":"intl",
    "number":"+33695740483"
},
"email":{
"hide": "yes"
}
}
'''

info = json.loads(data)
print 'Name:', info["name"]
print 'Hide:', info["email"]["hide"]