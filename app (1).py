#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Industrial Solar PV Optimization Demo")

# Simulate data
np.random.seed(42)
days = pd.date_range(start='2025-01-01', periods=365)
solar_irradiance = np.random.normal(5, 1.2, size=365)
energy_demand = np.random.normal(1000, 200, size=365)
df = pd.DataFrame({'date': days, 'solar_irradiance': solar_irradiance, 'energy_demand': energy_demand})

# Energy generation calculation
PV_capacity = 200
PV_efficiency = 0.18
df['energy_generated'] = df['solar_irradiance'] * PV_capacity * PV_efficiency
grid_emission_factor = 0.7
df['carbon_reduction'] = df['energy_generated'] * grid_emission_factor

# Plots
st.subheader("Solar Irradiance vs Energy Demand")
st.line_chart(df[['solar_irradiance','energy_demand']])

st.subheader("Energy Generated vs Demand")
st.line_chart(df[['energy_generated','energy_demand']])

st.subheader("Daily Carbon Reduction (kg CO2)")
st.line_chart(df['carbon_reduction'])

