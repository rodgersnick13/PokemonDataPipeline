import PipelineSetup as pData
import pandas as pd
import requests

path = 'pokemon.csv'
test = pd.read_csv(path)
testdf = pd.DataFrame(test)

df = pData.pokeData().df
print(df.head())
df.head()

response = requests.get('http://localhost:5000')
tasks = response.json()
print(tasks)