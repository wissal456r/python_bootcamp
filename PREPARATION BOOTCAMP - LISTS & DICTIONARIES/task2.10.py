superheroes = {
    "Batman": {"aliases": ["Bruce Wayne", "Dark Knight"]},
    "Superman": {"aliases": ["Clark Kent", "Kal-El"]},
    "Wolverine": {"aliases": []}
}

for name, details in superheroes.items():
    if details["aliases"]:
        print(name, details["aliases"])
    else:
        print(name, "No aliases found.")
