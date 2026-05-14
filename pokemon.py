import yaml
import pandas as pd

with open("pokemon-forms.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

rows = []

for name, info in data.items():
    row = {
        "name": name,
        "pokemonid": info.get("pokemonid"),
        "formid": info.get("formid"),
        "formname": info.get("formname"),
        "gen": info.get("gen"),
        "release": info.get("release"),
        "type1": info.get("type1"),
        "type2": info.get("type2"),
        "species": info.get("species"),
        "height": info.get("height"),
        "weight": info.get("weight"),
        "gender": info.get("gender"),
        "catch_rate": info.get("catch-rate"),
        "base_exp": info.get("base-exp"),
        "egg_cycles": info.get("egg-cycles"),
        "friendship": info.get("friendship"),
        "growth_rate": info.get("growth-rate"),
    }

    stats = info.get("stats", {})
    row["hp"] = stats.get("hp")
    row["attack"] = stats.get("attack")
    row["defense"] = stats.get("defense")
    row["spatk"] = stats.get("spatk")
    row["spdef"] = stats.get("spdef")
    row["speed"] = stats.get("speed")

    ev = info.get("ev-yield", {})
    row["ev_hp"] = ev.get("hp")
    row["ev_attack"] = ev.get("attack")
    row["ev_defense"] = ev.get("defense")
    row["ev_spatk"] = ev.get("spatk")
    row["ev_spdef"] = ev.get("spdef")
    row["ev_speed"] = ev.get("speed")

    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("pokemon.csv", index=False, encoding="utf-8")

print("Zapisano pokemon.csv")