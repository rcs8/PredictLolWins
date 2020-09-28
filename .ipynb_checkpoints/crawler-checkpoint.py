import pandas as pd
import numpy as np
import requests as rq

API_KEY = "RGAPI-2c16311f-5cfc-4724-8180-b3f72c943c3e"
base_diamond = "https://br1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/"
base_challenger = "https://br1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5/"
base_master = "https://br1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5"
base_grand_master = "https://br1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5"


def getPlayerInfos(string):
    response = rq.get(string)
    return pd.DataFrame(response.json())
        

divisions = ["I","II","III","IV"]
tiers = ["DIAMOND","MASTER","GRANDMASTER","CHALLENGER"]
df = pd.DataFrame()
for i in tiers:
    if i == "DIAMOND":
        for j in divisions:
            string = base_diamond + i + "/" + j + "?api_key=" + API_KEY
            df_aux = getPlayerInfos(string)
            df = df.append(df_aux,ignore_index = True)
    
    elif i == "MASTER":
        string = base_master + "?api_key=" + API_KEY
        df_aux = getPlayerInfos(string)
        df = df.append(df_aux,ignore_index = True)
    
    
    elif i == "GRANDMASTER":
        string = base_grand_master + "?api_key=" + API_KEY
        df_aux = getPlayerInfos(string)
        df = df.append(df_aux,ignore_index = True)
    
    else:
        string = base_challenger + "?api_key=" + API_KEY
        df_aux = getPlayerInfos(string)
        df = df.append(df_aux,ignore_index = True)
        