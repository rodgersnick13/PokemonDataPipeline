import pandas as pd

# Will grab data from github in "production", but I'm on metered internet
#url = 'https://raw.githubusercontent.com/rodgersnick13/PokemonDataPipeline/refs/heads/main/pokemon.csv'
class pokeData:
    df = pd.DataFrame()

    def __init__(self):
        path = 'pokemon.csv'
        csv = pd.read_csv(path)
        self.df = pd.DataFrame(csv)

    def head(self):
        return self.df.head()
    
    def dropTypeComparisons(self):
        df = self.df.drop(['against_bug', 'against_bug', 'against_dark', 'against_dragon',
                           'against_electric', 'against_fairy', 'against_fight', 'against_fire',
                           'against_flying', 'against_ghost', 'against_grass', 'against_ground',
                           'against_ice', 'against_normal', 'against_poison', 'against_psychic',
                           'against_rock', 'against_steel', 'against_water'])
        return df



#path = 'pokemon.csv'
#df = pd.read_csv(path)

#print(df.head(10))
#print(df.describe())

#def validateColPresent():

#def dropUnneededCols():