import pandas as pd

# Will grab data from github in production, but I'm on metered internet
#url = 'https://raw.githubusercontent.com/rodgersnick13/PokemonDataPipeline/refs/heads/main/pokemon.csv'
class pokeData:
    df = pd.DataFrame()

    def __init__(self):
        path = 'pokemon.csv'
        csv = pd.read_csv(path)
        self.df = pd.DataFrame(csv)

    def head(self):
        return self.df.head()
    
print(pokeData().df.head())


#path = 'pokemon.csv'
#df = pd.read_csv(path)

#print(df.head(10))
#print(df.describe())

#def validateColPresent():

#def dropUnneededCols():