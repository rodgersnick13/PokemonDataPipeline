import PipelineSetup as pData
import pandas as pd
import requests

path = 'pokemon.csv'
test = pd.read_csv(path)
testdf = pd.DataFrame(data=test)

df = pData.pokeData().df
df = df.set_index('pokedex_number')
df = df.drop(columns=['japanese_name', 'percentage_male', 'experience_growth', 'classfication', 'base_egg_steps',
                      'base_happiness', 'base_total', 'abilities'])

df = df.drop(columns=['against_bug', 'against_bug', 'against_dark', 'against_dragon',
                           'against_electric', 'against_fairy', 'against_fight', 'against_fire',
                           'against_flying', 'against_ghost', 'against_grass', 'against_ground',
                           'against_ice', 'against_normal', 'against_poison', 'against_psychic',
                           'against_rock', 'against_steel', 'against_water'])

df = df.drop(columns=['sp_attack', 'sp_defense', 'height_m'])


print(df.head())


# Test API
#response = requests.get('http://localhost:5000')
#tasks = response.json()
#print(tasks)