# %% Interactive Python Cell
import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

con = psycopg2.connect("dbname=asbuilt_trax user=postgres host=localhost port=5432")

# %%
