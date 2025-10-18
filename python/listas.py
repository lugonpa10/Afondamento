pokemons =["Pikachu", "Bulbasaur", "Charmander", "Squirtle", "Charizard"]
print(type(pokemons))
print("\nOriginal:",pokemons)

pokemons.append("Eevee") # añade al final
pokemons.insert(2,"Ratatta")
print("\nTras añadir:",pokemons)

pokemons.remove("Bulbasaur") # elimina elemento
del pokemons[5]
print("\nTras eliminar:",pokemons)
f=pokemons.pop() # extrae y elimina el último.
print("\nExtrae y elimina:",f)
print("\nQueda:",pokemons)

pokemons[0]="Ditto" # modificar
print("\nY tras modificar:",pokemons)