import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

'''
Utilising Gee & Ramirez 1994:
Gee, DA and Ramirez, WF (1988), Optimal temperature control for batch beer fermentation. Biotechnol. Bioeng., 31: 224-234.
https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/bit.260310308

Altering Code from "Batch Beer Fermentation Modelling, Github"
https://runjaj-github-io.translate.goog/blog/Gee%20MT.html?_x_tr_sl=es&_x_tr_tl=en&_x_tr_hl=es&_x_tr_pto=wapp
Coded in Julia w/ModellingToolkit.jl library 
'''

# 1. Model Parameters & Constants (Sam) ---------------------------------------------------------------

R = 8.314   # Ideal gas constant,J/mol/K

# Yeast growth parameters
A_mu = 1.0e8    # Growth frequency factor, 1/h
Ea_mu = 10  # Activation energy for growth, J/mol
Ks = 1  # Sugar saturation constant (g/L)

# 2. Reaction Rate Equations (Josh) -------------------------------------------------------------------

# 3. ODE System (Kostas) ------------------------------------------------------------------------------

# 4. Sensitivity Analysis (Bintang) -------------------------------------------------------------------

# 5. Simulation & Plots (Group) -----------------------------------------------------------------------

