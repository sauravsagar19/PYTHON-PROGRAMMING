import json
empid='''
[
{"id":"878787",
"name":"SAURAV",
"UID":"4444",
"rno":"5555",
"grade":"A+"
},
{"id":"323232",
"name":"DEVA",
"UID": "6666",
"rno":"7777",
"grade":"B+"
}
]'''
info=json.loads(empid)
print("count:",len(info))
for item in info:
    print(item["name"])
    print("Name:",item["name"])
    print("ID:",item["id"])
    print("roll number:",item["rno"])
    print("Grade:",item["grade"])
    print("\n")
