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
#------------------------------------------------------------------------------------------------------
# 1. Model Parameters & Constants (Josh)---------------------------------------------------------------

# 1.1 Constants
R = 8.314   # Ideal gas constant, J/mol/K

# 1.2 Kinetic parameters
# Arrhenius, k = A * exp(-Ea/(R*T))
# A = frequency factor, 1/hr; Ea = activation energy, J/mol

# Yeast growth (mu) & death (kd):
A_mu = 
Ea_mu = 
A_kd = 
Ea_kd = 

# Flavour kinetics:
#Formation step (k1) sugar -> VDK (flavour); Reduction step (k2) VDK = yeast -> flavourless compounds
A_k1 = 
Ea_k1 =
A_k2 =
Ea_k2 = 

# 1.3 Stoichiometry
Ks = # MONOD saturation constant, Ks, g/L
Y_xs = # Biomass Yield, Y_xs, biomass(g)/sugar(g)
Y_ps = # Ethanol Yield, Y_ps, ethanol(g)/sugar(g)
E_maax = # Toxiicity limit, E_max, g/L - [Ethanol] that stops yeast growth 

# 1.4 Temperature profile

#------------------------------------------------------------------------------------------------------
# 2. Reaction Rate Equations (Josh) -------------------------------------------------------------------

# Growth rate, mu, 1/hr:
mu = A_mu * np.exp(-Ea_mu/(R*T))

# Death rate, kd, 1/hr:
kd = A_kd * np.exp(-Ea_kd/(R*T))

# VDK formation rate, k1, 1/hr:
k1 = A_k1 * np.exp(-Ea_k1/(R*T))

# VDK reduction rate, k2, 1/hr:
k2 = A_k2 * np.exp(-Ea_k2/(R*T))

#------------------------------------------------------------------------------------------------------
# 3. ODE System (Kostas) ------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
# 4. Sensitivity Analysis (Bintang) -------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
# 5. Simulation & Plots (Group) -----------------------------------------------------------------------

