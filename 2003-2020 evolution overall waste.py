#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:16:54 2021

@author: giulia
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import random
plt.style.use('ggplot')

df = pd.read_csv("~/Downloads/archive/2003_2017_waste.csv")
df1 = pd.read_csv("~/Downloads/archive/2018_2020_waste.csv")

data = pd.concat([df, df1])

# Remove irrelevant columns
data.drop("Total Generated ('000 tonnes)", axis = 1, inplace = True)
data.drop("Total Recycled ('000 tonnes)", axis = 1, inplace = True)
#data.drop("waste_disposed_of_tonne", axis = 1, inplace = True)

# Isolate total of all waste types for each year

tot0 = data[data["waste_type"] == "Total"]
tot1= data[data["waste_type"] == "Overall"]
total = pd.concat([tot0,tot1])
total.sort_values(by=["year"], inplace = True)



# Draw graph of evolution of total recycling rate 2003-2020

total.plot(x="year", y="recycling_rate", kind = "line", legend = None, figsize = (8, 5))
plt.title("Total recycling rate 2003-2020")
plt.xlabel("Year")
plt.xticks(range(2003,2020,2))
plt.ylabel("recycling rate")
plt.yticks(range(0,2,1))

total.plot(x="year", y="recycling_rate", kind = "line", legend = None, figsize = (8, 5))
plt.title("Total recycling rate 2003-2020")
plt.xlabel("Year")
plt.xticks(range(2003,2020,2))
plt.ylabel("recycling rate")

# Create histogram showing waste recycled and waste not recycled
hist_data = total.copy()
hist_data.drop("recycling_rate", axis = 1, inplace = True)
hist_data.drop("total_waste_generated_tonne", axis = 1, inplace = True)
th0 = hist_data[hist_data["waste_type"] == "Total"]
th1 = hist_data[hist_data["waste_type"] == "Overall"]
total_hist = pd.concat([th0, th1])
total_hist.sort_values(by=["year"], inplace = True)
total_hist.set_index("year", inplace = True)
ax = total_hist.plot.bar(figsize = (10, 5))
plt.ticklabel_format(style='plain', axis='y')
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
plt.ylabel("Tonnes")
plt.xlabel("Year")
plt.title("Total unrecycled vs recycled waste 2003-2020")
ax.legend(["Unrecycled", "Recycled"])