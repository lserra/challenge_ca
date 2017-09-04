#!/usr/bin/python
# -*- coding: utf-8 -*-


# =======================================================================================================
# Author: laercio.serra@gmail.com
# Challenge from ContaAzul
# Exercise 1
# =======================================================================================================
import pandas as pd


def merge_files(start, end):
    """
    Merging the all files extracted to just one file called <accidents_brasil.csv>
    :param start: 2003
    :param end: 2007
    :return: no returns
    """
    # Defining the variables
    path = '/home/df/ContaAzul/Ex1/data/'
    ystart = int(start) + 1
    yend = int(end) + 1

    print(">> Merging files:")
    print("-" * 100)

    print("Filename: " + 'accidents_' + str(start) + '.csv')
    df_acidentes = pd.read_csv(path + 'accidents_' + str(start) + '.csv', encoding='latin1')
    df_acidentes.to_csv(path + 'accidents_brasil.csv', index=False)

    for y in list(range(ystart, yend, 1)):
        print("Filename: " + 'accidents_' + str(y) + '.csv')
        df_acidentes = pd.read_csv(path + 'accidents_' + str(y) + '.csv', encoding='latin1')
        df_merge = pd.read_csv(path + 'accidents_brasil.csv', encoding='latin1')
        df_acidentes_brasil = df_merge.append(df_acidentes, ignore_index=True)
        df_acidentes_brasil.to_csv(path + 'accidents_brasil.csv', index=False)
        # delete the DataFrames
        del df_acidentes, df_merge, df_acidentes_brasil

    print("-" * 100)


if __name__ == '__main__':
    merge_files('2003', '2007')
