StudentInfo = {
  "Shafa":{
        "name":"Shafa",
        "location": "",
        "Study":"7",
        "roll":"39",
        "number":2134567653
    }
}
studentInfo = {
    "Soha":{
        "name":"Soha",
        "Location": "Khulna",
        "Study":"1",
        "Roll":"20",
        "Number":213456765334
    },
    'year':1981
}

#Loop keys
for f in studentInfo:
    print(f)

#Loop values
for h in studentInfo.values():
    print(h)

#Loop Both Keys and Values
for k in studentInfo.items():
    print(k)