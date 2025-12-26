from prettytable import PrettyTable
table = PrettyTable()
from pokemons import pokemon


pokemon_list = []
for name, stats in pokemon.items():
    # We combine the name and stats into one list
    row = [name, stats["Type"], stats["HP"], stats["Attack"]]
    pokemon_list.append(row)


list_name=[]
j=0
for i in pokemon_list:
    list_name.append(pokemon_list[j][0])
    j+=1

list_type=[]
j=0
for i in pokemon_list:
    list_type.append(pokemon_list[j][1])
    j+=1

list_hp=[]
j=0
for i in pokemon_list:
    list_hp.append(pokemon_list[j][2])
    j+=1


list_attack=[]
j=0
for i in pokemon_list:
    list_attack.append(pokemon_list[j][3])
    j+=1





print(list_name) 
table.add_column("Name",list_name)
table.add_column("Type",list_type)
table.add_column("HP",list_hp)
table.add_column("Attack",list_attack)

print(table)
