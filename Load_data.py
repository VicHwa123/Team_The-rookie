# -*- coding: utf-8 -*-
"""
@author: ouj070
Project 1
@Date: May 11th 2016
@Team: Team_Rookie
"""

# libraries / packages
import os
import json
import pandas as pd

# constants
BASE_DIR = "C://Users/ouj070/Documents/GitHub/ct16_cap1_ds5/project_1/data"
MOJO_DIR = os.path.join(BASE_DIR, 'boxofficemojo')
META_DIR = os.path.join(BASE_DIR, 'metacritic')

# Create DataFrame

movies = []

NameList = [name for name in os.listdir(MOJO_DIR) if ".json" in name] 
# to avoid any non json file related failure

for i in NameList:
    target_file_path = os.path.join(MOJO_DIR, i)
    with open(target_file_path, 'r') as target_file:
        movie = json.load(target_file)
        movies.append(movie)

mojo_movies_df = pd.DataFrame(movies)

NameList = [name for name in os.listdir(META_DIR) if ".json" in name] 
movies = []

for i in NameList:
    target_file_path = os.path.join(META_DIR, i)
    with open(target_file_path, 'r') as target_file:
        movie = json.load(target_file)
        if type(movie) is not dict:
            continue
        else:
            movies.append(movie)

meta_movies_df = pd.DataFrame(movies)