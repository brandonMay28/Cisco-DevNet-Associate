import json

jsonstr = """{
    "Users": {
        "User": [
            {
                "Id": "1",
                "Firstname": "Brandon",
                "Lastname": "Romero",
                "Email": "bromero@json.com"
            },
            {
                "Id": "2",
                "Firstname": "Maxwell",
                "Lastname": "Rain",
                "Email": "mrain@json.com"
            },
            {
                "Id": "3",
                "Firstname": "Emily",
                "Lastname": "Jean",
                "Email": "ejean@json.com"
            }
        ]
    }
}"""

jsonObj = json.loads(jsonstr)

for user in jsonObj["Users"]["User"]:
    print(f'User: {user["Firstname"]} {user["Lastname"]} - Email: {user["Email"]}')
