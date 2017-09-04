#!/usr/bin/python
# -*- coding: utf-8 -*-


# =======================================================================================================
# Author: laercio.serra@gmail.com
# Challenge from ContaAzul
# Exercise 1
# =======================================================================================================


"""
Description: CLI - extracting/downloading the files from Public Brazilian Social Security API
-The user calls it from the command line (that is, shell prompt)
-If the -s flag is null, the output is a warning message
-If the -e flag is null, the output is a warning message
Ex.: python ext_files.py -s <year_start> -e <year_end>
"""
import optparse
import sys
import pandas as pd


# =======================================================================================================
# Part 1 - Command-Line
# The arguments for sys.argv that would be required are:
# -s year start
# -e year end
# =======================================================================================================
# Create the object
opt = optparse.OptionParser()

# Usage: add arguments
# object.add_option (
# 						"-[short flag option]",
# 						"--[long flag option]",
# 						action="store",
# 						type="string",
# 						dest="[variable name under which to store the option]" )
opt.add_option("-s", "--start", action="store", type="string", dest="year_start")
opt.add_option("-e", "--end", action="store", type="string", dest="year_end")

# All the options are assigned. The first of the two values, opt , is an
# object containing the values of all the options passed to the program.
# The second value, args , is a list of any remaining arguments.
opt, args = opt.parse_args()

if opt.year_start is None or opt.year_end is None:
    print('-' * 100)
    print('This is a CLI extracting/downloading files utility. Usage:')
    print('>> The user calls it from the command line (that is, shell prompt)')
    print('>> The year start and year end are defined at the time of calling')
    print('>> The -s flag is necessary and indicates the year start')
    print('>> The -e flag is necessary and indicates the year end')
    print('Ex.: python ext_files.py -s 2003 -e 2007')
    print('-' * 100)
    sys.exit(1)


# Defining the parameters of the statement
ystart = int(opt.year_start)
yend = int(opt.year_end) + 1


# Defining the API url template ( http://api.dataprev.gov.br/previdencia/anuario/2009/acidentes-do-trabalho.csv )
url_template = "http://api.dataprev.gov.br/previdencia/anuario/{year}/acidentes-do-trabalho.csv"


# Defining the path
path = '/home/df/ContaAzul/Ex1/data/'


print(">> Downloading files:")
print("-" * 100)

for y in list(range(ystart, yend, 1)):
    print(url_template.format(year=y))
    df_acidentes = pd.read_csv(url_template.format(year=y), encoding='latin1')
    df_acidentes.to_csv(path + 'accidents_' + str(y) + '.csv', index=False)

print("-" * 100)
