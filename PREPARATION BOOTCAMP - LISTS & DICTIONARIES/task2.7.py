types = {
    "Electric": ["Pikachu"],
    "Grass": ["Bulbasaur"],
    "Fire": ["Charmander"]
}

for pokemon_type, pokemons in types.items():
    if "Pikachu" in pokemons:
        print(pokemon_type)

pikachu_type = next(
    (kind for kind, pokemons in types.items() if "Pikachu" in pokemons),
    None
)
print(pikachu_type)
