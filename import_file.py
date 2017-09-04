#!/usr/bin/python
# -*- coding: utf-8 -*-


# =======================================================================================================
# Author: laercio.serra@gmail.com
# Challenge from ContaAzul
# Exercise 1
# =======================================================================================================
import pandas as pd
from sqlalchemy import create_engine


path = '/home/df/ContaAzul/Ex1/data/'
engine = create_engine('postgresql://postgres:admin@localhost/postgres')
df = pd.read_csv(path + 'accidents_brasil.csv')
df.to_sql("conta_azul", engine)


print(">> Has been imported: ")
print("-" * 100)
print(str(df.count()))
print("-" * 100)
print(">> Importing concluded successfully!")
