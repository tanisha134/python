#Change Dictionary Items
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
studentInfo['year'] = 2012
print(studentInfo)

studentInfo.update({"Soha":"Soha read in class 7"})
print(studentInfo["Soha"])


