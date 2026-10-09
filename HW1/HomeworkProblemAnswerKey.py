#Making the Baseball Thriple Slash in Python
hits = 201
at_bats = 540
walks = 60
hit_by_pitches = 3
sacrifice_flies = 30
singles = 126
doubles = 25
triples = 10
homeruns = 40

batting_average = hits / at_bats
on_base_percentage = (hits + walks + hit_by_pitches) / (at_bats + hit_by_pitches + walks + sacrifice_flies)
slugging_percentage = (singles + 2 * doubles + 3 * triples + 4 * homeruns) / at_bats

batting_average1 = round(batting_average, 3)
on_base_percentage1 = round(on_base_percentage, 3)
slugging_percentage1 = round(slugging_percentage, 3)




print(str(batting_average1) + "/" + str(on_base_percentage1) + "/" + str(slugging_percentage1))
