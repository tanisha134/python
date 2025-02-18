#Acessing Items of Dictionaries
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
print(studentInfo['year'])
t = (studentInfo.get("Soha"))
print(t)

d = studentInfo.keys()
print(d)

w = studentInfo.values()
print(w)