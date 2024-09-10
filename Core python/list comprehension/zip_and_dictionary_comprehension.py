name = ["bruce", "cleck", "peter"]
hero = ["batman", "superman", "spiderman"]

# my_dict = {}
# for name, hero in zip(name, hero):
#     my_dict[name] = hero
# print(my_dict)

my_dict = {name: hero for name, hero in zip(name, hero)}
print(my_dict)
