import pandas

staty = pandas.read_json("staty.json")
staty = staty.set_index("name")

# přidat si sloupec do df, spočítat ho / počítané sloupce
staty["population_density"] = staty["population"]/staty["area"]
# řazení od nejmenší hodnoty:
staty = staty.sort_values("population_density")
# řazení sestupně:
staty = staty.sort_values("population_density", ascending = False)
# řazení podle více sloupců:
staty = staty.sort_values(["population_density", "area"], ascending=(False, True))

