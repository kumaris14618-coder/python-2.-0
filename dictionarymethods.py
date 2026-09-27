person = {"name":"alice", "age":30 ,"city": "banglore"}
#how to get keys,values or items
print(person.keys())
print(person.values())
print(person.items())

#check if key exists
if "name" in person:
    print("name found")
else:
    print("not found")

#update multiple values
person.update({"age":31,"job":"engineer"})        