#Default Packages
import pandas as pd
import numpy as np
import io
from pathlib import Path
import os

#import plotly.express as px
#import plotly.io as pio
#pio.renderers.default = "plotly_mimetype+notebook"



#Load in game logs for AR15
bronny_game_logs_24 = Path('C:/Users/Alex/Desktop/Does Austin Reaves Suck//AR15SUCKS/data') / 'Bronny Game Stats.csv'
USC_game_logs_24 = Path('C:/Users/Alex/Desktop/Does Austin Reaves Suck//AR15SUCKS/data') / 'USC Game Stats.csv'
bronny_game_logs_24 = pd.read_csv(bronny_game_logs_24)
USC_game_logs_24 = pd.read_csv(USC_game_logs_24, encoding='windows-1252')
#print(game_logs_24)

def mean_stat(stat):
    return game_logs_24[stat].mean()

def sum_stat(stat):
    return game_logs_24[stat].sum()


USC_game_logs_24 = USC_game_logs_24.dropna
USC_game_logs_24['Point Diff'] = USC_game_logs_24['Tm'] #- USC_game_logs_24['Opp']

#print(bronny_game_logs_24)
print(USC_game_logs_24)



