student = [
    {"name" : "ice", "id": "68130500105", "age" : 18},
    {"name" : "Gai", "id": "68130500205", "age" : 19},
    {"name" : "Mark", "id": "68130500305", "age" : 13}
]

def check_age(age) :
    return age > 20

def get_data(ds, index, key) :
    return ds[index][key]

print(get_data(student, 2, "name"))

# print(type(student))
   
# for s in student

