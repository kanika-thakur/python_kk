#make a dictonaries
dict={
    "name":"KANIKA THAKUR",
    "age": 21,
    "merital":"single"

}
print(dict)
print(dict["age"])


#length of dictonaires
print(len(dict))

#type of dictonaires
print(type(dict))

#using dict() constructo 
#thisdict=dict(name="kanika",age=56,maritalstatus="single")
##print(thisdict)

#print(x)

#add the elements in the ductionry 
x=dict.keys()
print(x)

dict["color"]="white"
print(x)

#remove the elmemts from dictonaries 
dict.pop("merital")
print(dict)

#update the dictonaries
dict.update({"color": "red"})

#change the values 
dict["age"]=22
print(dict)

#add the elements
dict["skincolor"]="brown"
print(dict)

#loop in dictionaries
for x in dict:
    print("it exists")

#copy in dictonaries
mydict=dict.copy()
print(mydict)

#nested dictonaries
myFamily={
    "child1":{
        "name":"kanika",
        "year":2004
    },
    "child2":{
        "name":"shyam",
        "year":2006
    },
    "child3":{
        "name":"zaid",
        "year":2008
    }

}
print(myFamily)
print(myFamily["child1"]["name"])