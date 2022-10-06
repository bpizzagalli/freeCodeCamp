import numpy as np
import pandas as pd
import requests

api_url = "https://swapi.co/api/people/?format=json"

req = requests.get(api_url)

json_dict = req.json()

starwars_people_df = pd.DataFrame.from_dict(json_dict['results'])

blue_eyed_people_df = starwars_people_df.loc[starwars_people_df['eye_color'] == 'blue']

