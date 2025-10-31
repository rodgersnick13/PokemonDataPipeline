import pandas as pd

class Transform():
    df: pd.DateFrame
            
    def drop_unneeded_columns(self):
        self.df.drop(['against_bug', 'against_bug', 'against_dark', 'against_dragon',
                        'against_electric', 'against_fairy', 'against_fight', 'against_fire',
                        'against_flying', 'against_ghost', 'against_grass', 'against_ground',
                        'against_ice', 'against_normal', 'against_poison', 'against_psychic',
                        'against_rock', 'against_steel', 'against_water', 'japanese_name',
                        'generation', 'classfication', 'base_egg_steps', 'abilities',
                        'base_total', 'sp_attack', 'sp_defense', 'type2', 'percentage_male',
                        'experience_growth'], axis=1, inplace=True)
        
    def __init__(self, pokemon_csv):
        csv = pd.read_csv(pokemon_csv)
        self.df = pd.DataFrame(csv)
        
        self.df.drop_unneeded_columns()
        df = df.dropna(subset=['height_m'])
        df['is_legendary'] = df['is_legendary'].astype(bool)
        df = df[df['capture_rate'] != '30 (Meteorite)255 (Core)']
        df['capture_rate'] = df['capture_rate'].astype(int)
            
