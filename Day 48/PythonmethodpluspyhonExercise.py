#clear() = Removes all the elements from the dictionary
#copy () = Returns a copy of the dictionary
#fromkyes() = Returns a dictionary with the specified keys and value
#get() = Returns the value of the specified kye
#items() = Returns a list containing a tuple for each key value pair
#keys () = Returns a list containing the dictionary's keys
#pop  () = Removes the element with the specified key
#popitem() = Removes the last inserted kye-value pair
#setdefault() = Returns the value of the specified key.If the key does not exist: insert the kye,with the specified value
#update() = Updates the dictionary with the specified key-value pairs
#values() = Returns a list of all the values in the dictionary

#Exercise
car =  {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(car)

car.get("model")
print(car.get("model"))

car["year"] = 2020
print(car)