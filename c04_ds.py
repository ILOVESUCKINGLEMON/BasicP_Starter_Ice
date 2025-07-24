# ------ DATA STRUCTURE------
# LIST ----------------

# fr = ["Lay","Caramujo","Donut"]

# num_list = [10 , 20 , 30 , [1, 2, 3]]

# print[fr(1)]

#DICTIONARY --------------

# student = [
#     {"name" : "ice", "id": "68130500105", "age" : 18},
#     {"name" : "Gai", "id": "68130500205", "age" : 19},
#     {"name" : "Gai", "id": "68130500205", "age" : 19}
# ]
# print(student)
# for s in student :
#     print(s)
#     print(f"your name is {s['name']}")

# Basic Function Business logic ----------

student = [
    {"name" : "ice", "id": "68130500105", "age" : 18},
    {"name" : "Gai", "id": "68130500205", "age" : 19},
    {"name" : "Mark", "id": "68130500305", "age" : 20}
]

def get_data(ds, index, key) :
    return ds[index][key]

print(get_data(student, 2, "name"))


