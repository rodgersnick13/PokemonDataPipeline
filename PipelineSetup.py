import pandas as pd

url = 'https://raw.githubusercontent.com/rodgersnick13/PokemonDataPipeline/refs/heads/main/pokemon.csv'
df = pd.read_csv(url)
print(df.head(10))
print(df.describe())