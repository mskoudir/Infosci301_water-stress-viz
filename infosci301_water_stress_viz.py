# -*- coding: utf-8 -*-
"""infosci301_water_stress_viz.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a4cLTshYler0ugfbKKjxOek0JH5LJ3rP
"""

import pandas as pd
import plotly.express as px

# Step 1: Load the dataset
df = pd.read_csv('API_ER.H2O.INTR.PC_DS2_en_csv_v2_13883.csv', skiprows=4)

# Step 2: Keep only necessary columns
years = [str(year) for year in range(1961, 2021)]
df = df[['Country Name', 'Country Code'] + years]

# Step 3: Transform data to long format
df_long = df.melt(id_vars=['Country Name', 'Country Code'],
                  var_name='Year', value_name='Freshwater_per_capita')
df_long.dropna(subset=['Freshwater_per_capita'], inplace=True)
df_long['Year'] = df_long['Year'].astype(int)

# Step 4: Create interactive choropleth
fig = px.choropleth(df_long,
                    locations='Country Code',
                    color='Freshwater_per_capita',
                    hover_name='Country Name',
                    animation_frame='Year',
                    color_continuous_scale='Blues',
                    title='Renewable Internal Freshwater Resources per Capita (1961–2020)')

fig.update_layout(
    geo=dict(showframe=False, showcoastlines=False),
    coloraxis_colorbar=dict(title='Cubic meters per capita'),
    margin={"r":0,"t":50,"l":0,"b":0}
)

fig.show()