# list data structure
my_list = ["Mercurials", "Hypervenom", "Phantom gx", "Predator", "x", "Future"]
my_list.append("Ultra")
print(my_list)
my_list[0] = "Puma Eclipse"
print(my_list[0])
print(my_list[0], "is manufactured by Puma")

dalist = ["21", "11", "31", "17", "10"]
dalist.insert(1, "7")
print(dalist)
print(type(dalist))

# tuple data structure
my_tuple = ("Cafu", "Maldini", "Marcelo", "Carlos", "Pique", "Stam", "Ramos")
print(my_tuple)
print(f"I wish I played with {my_tuple[1]}")

# set data structure
my_set = {"Van de Sar", "Courtois", "Buffon", "Cech", "Donnaruma", "A.Becker", "Ter Stegen"}
print(my_set)

# dictionaries
my_dict = {"name": "Peter", "Age": 17, "Gender": "Male"}
print(my_dict)
print(my_dict["name"])
print(my_dict["Gender"], "this nigga a dude")
