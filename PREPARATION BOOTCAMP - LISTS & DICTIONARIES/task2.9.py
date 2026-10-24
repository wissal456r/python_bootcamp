superheroes = {
    "Batman": {
        "id": 1,
        "aliases": ["Bruce Wayne", "Dark Knight"],
        "location": {
            "number": 1007,
            "street": "Mountain Drive",
            "city": "Gotham"
        }
    },
    "Superman": {
        "id": 2,
        "aliases": ["Kal-El", "Clark Kent", "The Man of Steel"],
        "location": {
            "number": 344,
            "street": "Clinton Street",
            "city": "Metropolis"
        }
    }
}

superheroes["Batman"]["aliases"].append("Caped Crusader")

superheroes["Wolverine"] = {
    "id": 3,
    "aliases": [],
    "location": {}
}

print(superheroes)
