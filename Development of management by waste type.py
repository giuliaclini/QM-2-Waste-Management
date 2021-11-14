#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 14:46:22 2021

@author: giulia
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
plt.style.use('ggplot')

df = pd.read_csv("~/Downloads/archive/2003_2017_waste.csv")
df1 = pd.read_csv("~/Downloads/archive/2018_2020_waste.csv")

data = pd.concat([df, df1])

#Remove irrelevant columns from dataset

data.drop("Total Generated ('000 tonnes)", axis = 1, inplace = True)
data.drop("Total Recycled ('000 tonnes)", axis = 1, inplace = True)
data.drop("waste_disposed_of_tonne", axis = 1, inplace = True)

#Sort dataset by waste type and then by year
data.sort_values(by=["waste_type", 'year'], inplace = True)
#print(data.head())

#Divide dataset into multiple datasets (one for each type of waste)
as0 = data[data["waste_type"] == "Ash & Sludge"]
as1 = data[data["waste_type"] == "Ash and sludge"]
as2 = data[data["waste_type"] == "Sludge"]
as3 = data[data["waste_type"] == "Ash & sludge"]
a_s = pd.concat([as0,as1,as2,as3])
a_s.sort_values(by=["year"], inplace = True)
print(a_s)

food0 = data[data["waste_type"] == "Food"]
food1 = data[data["waste_type"] == "Food waste"]
food = pd.concat([food0,food1])
food.sort_values(by=["year"], inplace = True)
#print(food)

paper = data[data["waste_type"] == "Paper/Cardboard"]
paper.sort_values(by=["year"], inplace = True)
#print(paper)

glass = data[data["waste_type"] == "Glass"]
glass.sort_values(by=["year"], inplace = True)
#print(glass)

fm0 = data[data["waste_type"] == "Ferrous Metal"]
fm1 = data[data["waste_type"] == "Ferrous Metals"]
fm2 = data[data["waste_type"] == "Ferrous metal"]
f_metal = pd.concat([fm0,fm1,fm2])
f_metal.sort_values(by=["year"], inplace = True)
#print(f_metal)

nf0 = data[data["waste_type"] == "Non-ferrous Metal"]
nf1 = data[data["waste_type"] == "Non-ferrous metal"]
nf2 = data[data["waste_type"] == "Non-ferrous Metals"]
nf3 = data[data["waste_type"] == "Non-ferrous metals"]
nf4 = data[data["waste_type"] == "Non-Ferrous Metal"]
nf_metal = pd.concat([nf0,nf1,nf2,nf3,nf4])
nf_metal.sort_values(by=["year"], inplace = True)
#print(nf_metal)

st0 = data[data["waste_type"] == "Scrap Tyres"]
st1 = data[data["waste_type"] == "Scrap tyres"]
tyres = pd.concat([st0,st1])
tyres.sort_values(by=["year"], inplace = True)
#print(tyres)

o0 = data[data["waste_type"] == "Others (stones, ceramics, etc.)"]
o1 = data[data["waste_type"] == "Others (stones, ceramics & rubber etc.)"]
o2 = data[data["waste_type"] == "Others (stones, ceramic, rubber, etc.)"]
o3 = data[data["waste_type"] == "Others (stones, ceramics & rubber etc)"]
o4 = data[data["waste_type"] == "Others"]
o5 = data[data["waste_type"] == "Others (stones, ceramic, rubber, ect)"]
others = pd.concat([o0,o1,o2,o3,o4,o5])
others.sort_values(by=["year"], inplace = True)
#print(others)

us0 = data[data["waste_type"] == "Used Slag"]
us1 = data[data["waste_type"] == "Used slag"]
used_slag = pd.concat([us0,us1])
used_slag.sort_values(by=["year"], inplace = True)
#print(used_slag)

w0 = data[data["waste_type"] == "Wood/Timber"]
w1 = data[data["waste_type"] == "Wood"]
wood = pd.concat([w0,w1])
wood.sort_values(by=["year"], inplace = True)
#print(wood)

pl0 = data[data["waste_type"] == "Plastic"]
pl1= data[data["waste_type"] == "Plastics"]
plastic = pd.concat([pl0,pl1])
plastic.sort_values(by=["year"], inplace = True)
#print(plastic)

hw0 = data[data["waste_type"] == "Horticultural Waste"]
hw1 = data[data["waste_type"] == "Horticultural"]
hw2 = data[data["waste_type"] == "Horticultural waste"]
horticultural_waste = pd.concat([hw0,hw1,hw2])
horticultural_waste.sort_values(by=["year"], inplace = True)
#print(horticultural_waste)

textile = data[data["waste_type"] == "Textile/Leather"]
textile.sort_values(by=["year"], inplace = True)
#print(textile)

cd0 = data[data["waste_type"] == "Construction Debris"]
cd1 = data[data["waste_type"] == "Construction & Demolition"]
cd2 = data[data["waste_type"] == "C&D"]
cd3 = data[data["waste_type"] == "Construction debris"]
cd4 = data[data["waste_type"] == "Construction& Demolition"]
construction = pd.concat([cd0,cd1,cd2,cd3,cd4])
construction.sort_values(by=["year"], inplace = True)
#print(construction)

# For each waste type, create a graph of recycling rate over time

ax = a_s.plot(x="year", y="recycling_rate", kind = "line", label = "Ash and sludge", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of ash and sludge 2003-2020")

food.plot(x="year", y="recycling_rate", kind = "line", label = "Food", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of food 2003-2020")

paper.plot(x="year", y="recycling_rate", kind = "line", label = "Paper", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of paper 2003-2020")

glass.plot(x="year", y="recycling_rate", kind = "line", label = "Glass", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of glass 2003-2020")

f_metal.plot(x="year", y="recycling_rate", kind = "line", label = "Ferrous metal", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of ferrous metal 2003-2020")

nf_metal.plot(x="year", y="recycling_rate", kind = "line", label = "Non-ferrous metal", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of non-ferrous metal 2003-2020")

tyres.plot(x="year", y="recycling_rate", kind = "line", label = "Scrap tyres", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of scrap tyres 2003-2020")

others.plot(x="year", y="recycling_rate", kind = "line", label = "Others (stones, ceramics, etc.)", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of others (stones, ceramics, etc.) 2003-2020")


used_slag.plot(x="year", y="recycling_rate", kind = "line", label = "Used slag", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of used slag 2003-2020")


wood.plot(x="year", y="recycling_rate", kind = "line", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of wood 2003-2020")

plastic.plot(x="year", y="recycling_rate", kind = "line", label = "Plastic", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of plastic 2003-2020")


horticultural_waste.plot(x="year", y="recycling_rate", kind = "line", label = "Horticultural waste", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of horticultural waste 2003-2020")


textile.plot(x="year", y="recycling_rate", kind = "line", label = "Textiles and leather", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of textiles and leather 2003-2020")


construction.plot(x="year", y="recycling_rate", kind = "line", label = "Construction and demolition", marker = "o", figsize = (8, 5), legend = None)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))
plt.title("Recycling rate of construction and demolition 2003-2020")

#Create one graph displaying all waste types

ax = a_s.plot(x="year", y="recycling_rate", kind = "line", label = "Ash and sludge", figsize = (16, 10))
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))

food.plot(x="year", y="recycling_rate", kind = "line", label = "Food", ax=ax, style = "--")
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))

paper.plot(x="year", y="recycling_rate", kind = "line", label = "Paper", ax=ax, style = "--")
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))


glass.plot(x="year", y="recycling_rate", kind = "line", label = "Glass", ax=ax, style = "--")
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))


f_metal.plot(x="year", y="recycling_rate", kind = "line", label = "Ferrous metal", ax=ax, style = "--")
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))


nf_metal.plot(x="year", y="recycling_rate", kind = "line", label = "Non-ferrous metal", ax=ax, style = "--")
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))


tyres.plot(x="year", y="recycling_rate", kind = "line", label = "Scrap tyres", ax=ax, style = "--")
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))


others.plot(x="year", y="recycling_rate", kind = "line", label = "Others", ax=ax, style = "--")
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))


used_slag.plot(x="year", y="recycling_rate", kind = "line", label = "Used slag", ax=ax)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))


wood.plot(x="year", y="recycling_rate", kind = "line", label = "Wood", ax=ax)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))

plastic.plot(x="year", y="recycling_rate", kind = "line", label = "Plastic", ax=ax)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))


horticultural_waste.plot(x="year", y="recycling_rate", kind = "line", label = "Horticultural", ax=ax)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))


textile.plot(x="year", y="recycling_rate", kind = "line", label = "Textiles", ax=ax)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))


construction.plot(x="year", y="recycling_rate", kind = "line", label = "Construction", ax=ax)
plt.xlabel("Year")
plt.ylabel("Recycling Rate")
plt.xticks(range(2003,2020, 2))

plt.title("Recycling rate of all waste types 2003-2020")


