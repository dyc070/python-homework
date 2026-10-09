"""
This code calculates the slash line used in Major League Baseball. 
"""

def batting_average_calc(hits, at_bats):
    #This function calculates batting average by dividing # of hits by # of at bats. All values must be greater than zero and less than 780. 
    return float(hits / at_bats)
def on_base_percentage_calc(hits, walks, hit_by_pitches, at_bats, sacrifice_flies):
    #This function calculates on-base percentage by adding # of hits, walks, and hit by pitches and dividing # of at-bats + # of hit-by-pitches + # of walks + # of sacrifice flies
    return float((hits + walks + hit_by_pitches) / (at_bats + hit_by_pitches + walks + sacrifice_flies))
def slugging_percentage_calc(singles, doubles, triples, homeruns, at_bats):
    #This function calculates slugging percentage by standardizing each type of base hit and dividing by # of at-bats. 
    return float((singles + 2 * doubles + 3 * triples + 4 * homeruns) / at_bats)
def on_base_plus_slugging_calc(on_base_percentage, slugging_percentage):
    #This function calculates on-base plus slugging by adding on-base and slugging percentage.  
    return float((on_base_percentage + slugging_percentage))

if __name__ == "__main__":
    singles = int(input('How many singles has the player had this season?'))
    doubles = int(input('How many doubles has the player had this season?'))
    triples = int(input('How many triples has the player had this season?'))
    homeruns = int(input('How many homeruns has the player had this season?'))
    hits = int(input('How many hits in total has the player had this season?'))
    walks = int(input('How many walks has the player had this season?')) 
    at_bats = int(input('How many at-bats has the player had this season?')) 
    hit_by_pitches = int(input('How many hit-by-pitches has the player had this season?'))
    sacrifice_flies = int(input('How many sacrifice flies has the player had this season?')) 

if singles < 0 or doubles < 0 or triples < 0 or homeruns < 0 or hits < 0 or walks < 0 or at_bats < 0 or hit_by_pitches < 0 or sacrifice_flies < 0: 
    print('Invalid parameters, all values must be greater than 0.')
if singles > 1000 or doubles > 1000 or triples > 1000 or homeruns > 1000 or hits > 1000 or walks > 1000 or at_bats > 1000 or hit_by_pitches > 1000 or sacrifice_flies > 1000:
    print('Invalid parameters, all values must be less than 1000.')
else:
    batting_average = batting_average_calc(hits, at_bats)
    on_base_percentage = on_base_percentage_calc(hits, walks, hit_by_pitches, at_bats, sacrifice_flies)
    slugging_percentage = slugging_percentage_calc(singles, doubles, triples, homeruns, at_bats)
    on_base_plus_slugging = on_base_plus_slugging_calc(on_base_percentage, slugging_percentage)
    print(f'The slash line of this player is: {batting_average:.3f}/{on_base_percentage:.3f}/{slugging_percentage:.3f}/{on_base_plus_slugging:.3f}')


