#!/usr/bin/env python
# coding: utf-8

# In[194]:


# Partial Pressure Solver For cracking of gaseous ammonia
# 2NH3 = N2 + 3H2

# Imports
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy.optimize import brentq
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

# Get the Gibbs Free Energy & Kp from input temperature 
e = 2.718
R = 8.3144
Temp = float(input("Please input a temperature (K): "))
P = float(input("Please input a pressure value (atm): "))

# Making Functions
def Gibbs (Temp):
    answer_Gibbs = 87030 - 25.8*(Temp)*np.log((Temp))-31.7*(Temp)
    return answer_Gibbs

def Kp (Temp):
    answer_Kp = e**(Gibbs(Temp)/(-R*Temp))
    return answer_Kp

def partial_pressure_solver(z):
    x = z[0]
    F = np.empty((1))
    F[0] = (5.196*x**2)*P - ((Kp(Temp))**(0.5))*(1-4*x**2)
    return F

z0 = np.array([1])
z = fsolve(partial_pressure_solver,z0)
PH2 = ((3*z / (1+2*z)))*P
PN2 = ((z / (1+2*z)))*P
PNH3 = ((1-2*z)/(1+2*z))*P

# Print The Partial Pressures
print("{:.4f}".format(float(PH2)) + " atm" + " is the partial pressure of H2")
print("{:.4f}".format(float(PN2))+ " atm" + " is the partial pressure of N2")
print("{:.4f}".format(float(PNH3))+ " atm" + " is the partial pressure of NH3")


# In[193]:


# Graphs Using Individual Points

# NH3 Graph
def partial_pressure_solver_1atm_NH3(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+5.196))**(0.5) / (2*(4*((answer_Kp)**(0.5))+5.196))

    return (1-2*z)/(1+2*z)
x_axis_2NH3 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150]
y_axis_2NH3 = [partial_pressure_solver_1atm_NH3(50),
               partial_pressure_solver_1atm_NH3(100),
               partial_pressure_solver_1atm_NH3(150),
               partial_pressure_solver_1atm_NH3(200),
               partial_pressure_solver_1atm_NH3(250), 
               partial_pressure_solver_1atm_NH3(300),
               partial_pressure_solver_1atm_NH3(350),
               partial_pressure_solver_1atm_NH3(400),
               partial_pressure_solver_1atm_NH3(450),
               partial_pressure_solver_1atm_NH3(500),
               partial_pressure_solver_1atm_NH3(550),
               partial_pressure_solver_1atm_NH3(600),
               partial_pressure_solver_1atm_NH3(650),
               partial_pressure_solver_1atm_NH3(700),
               partial_pressure_solver_1atm_NH3(750),
               partial_pressure_solver_1atm_NH3(800),
               partial_pressure_solver_1atm_NH3(850),
               partial_pressure_solver_1atm_NH3(900),
               partial_pressure_solver_1atm_NH3(950),
               partial_pressure_solver_1atm_NH3(1000),
               partial_pressure_solver_1atm_NH3(1050),
               partial_pressure_solver_1atm_NH3(1100),
               partial_pressure_solver_1atm_NH3(1150)]
plt.plot(x_axis_2NH3, y_axis_2NH3, label = "NH3", color = "blue")

# Titles & Labels
plt.ylim(0, 1.0)
plt.xlim(300, 1250)
plt.xlabel("Temperature (K)")
plt.ylabel("mole fraction")
plt.title("The Effect of Temperature (K) on Mole Fraction")
plt.legend()

# N2 Graph
def partial_pressure_solver_1atm_N2(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+5.196))**(0.5) / (2*(4*((answer_Kp)**(0.5))+5.196))

    return (z / (1+2*z))

x_axis_N2 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150]
y_axis_N2 = [partial_pressure_solver_1atm_N2(50),
               partial_pressure_solver_1atm_N2(100),
               partial_pressure_solver_1atm_N2(150),
               partial_pressure_solver_1atm_N2(200),
               partial_pressure_solver_1atm_N2(250), 
               partial_pressure_solver_1atm_N2(300),
               partial_pressure_solver_1atm_N2(350),
               partial_pressure_solver_1atm_N2(400),
               partial_pressure_solver_1atm_N2(450),
               partial_pressure_solver_1atm_N2(500),
               partial_pressure_solver_1atm_N2(550),
               partial_pressure_solver_1atm_N2(600),
               partial_pressure_solver_1atm_N2(650),
               partial_pressure_solver_1atm_N2(700),
               partial_pressure_solver_1atm_N2(750),
               partial_pressure_solver_1atm_N2(800),
               partial_pressure_solver_1atm_N2(850),
               partial_pressure_solver_1atm_N2(900),
               partial_pressure_solver_1atm_N2(950),
               partial_pressure_solver_1atm_N2(1000),
               partial_pressure_solver_1atm_N2(1050),
               partial_pressure_solver_1atm_N2(1100),
               partial_pressure_solver_1atm_N2(1150)]
plt.plot(x_axis_N2, y_axis_N2, label = "N2", color = "green")
plt.legend()

# H2 Graph
def partial_pressure_solver_1atm_H2(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+5.196))**(0.5) / (2*(4*((answer_Kp)**(0.5))+5.196))

    return (3*z / (1+2*z))

x_axis_H2 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150]
y_axis_H2 = [partial_pressure_solver_1atm_H2(50),
               partial_pressure_solver_1atm_H2(100),
               partial_pressure_solver_1atm_H2(150),
               partial_pressure_solver_1atm_H2(200),
               partial_pressure_solver_1atm_H2(250), 
               partial_pressure_solver_1atm_H2(300),
               partial_pressure_solver_1atm_H2(350),
               partial_pressure_solver_1atm_H2(400),
               partial_pressure_solver_1atm_H2(450),
               partial_pressure_solver_1atm_H2(500),
               partial_pressure_solver_1atm_H2(550),
               partial_pressure_solver_1atm_H2(600),
               partial_pressure_solver_1atm_H2(650),
               partial_pressure_solver_1atm_H2(700),
               partial_pressure_solver_1atm_H2(750),
               partial_pressure_solver_1atm_H2(800),
               partial_pressure_solver_1atm_H2(850),
               partial_pressure_solver_1atm_H2(900),
               partial_pressure_solver_1atm_H2(950),
               partial_pressure_solver_1atm_H2(1000),
               partial_pressure_solver_1atm_H2(1050),
               partial_pressure_solver_1atm_H2(1100),
               partial_pressure_solver_1atm_H2(1150)]
plt.plot(x_axis_H2, y_axis_H2, label = "H2", color = "orange")
plt.legend()

# Saving
plt.savefig("Graphs/The_Effect_Of_Temperature(K)_On_Mole_Fraction.png")


# In[184]:


# Graphs with higher density of points

np.linspace

# NH3 graph
def partial_pressure_solver_1atm_NH3(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+5.196))**(0.5) / (2*(4*((answer_Kp)**(0.5))+5.196))

    return (1-2*z)/(1+2*z)

x_axis_temperature_NH3=[]
y_axis_mole_fraction_NH3=[]

for temp in np.linspace(0,800,10000):
    P_NH3 = partial_pressure_solver_1atm_NH3(temp)
    y_axis_mole_fraction_NH3.append(P_NH3)
    x_axis_temperature_NH3.append(temp)
    
plt.plot(x_axis_temperature_NH3,y_axis_mole_fraction_NH3, color = "blue", label = "NH3")
plt.legend()

# N2 graph
def partial_pressure_solver_1atm_N2(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+5.196))**(0.5) / (2*(4*((answer_Kp)**(0.5))+5.196))

    return (z / (1+2*z))

x_axis_temperature_N2=[]
y_axis_mole_fraction_N2=[]

for temp in np.linspace(0,800,10000):
    P_N2 = partial_pressure_solver_1atm_N2(temp)
    y_axis_mole_fraction_N2.append(P_N2)
    x_axis_temperature_N2.append(temp)
    
plt.plot(x_axis_temperature_N2, y_axis_mole_fraction_N2, color = "green", label = "N2")
plt.legend()

# H2 Graph
def partial_pressure_solver_1atm_H2(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+5.196))**(0.5) / (2*(4*((answer_Kp)**(0.5))+5.196))

    return (3*z / (1+2*z))

x_axis_temperature_H2=[]
y_axis_mole_fraction_H2=[]

for temp in np.linspace(0,800,10000):
    P_H2 = partial_pressure_solver_1atm_H2(temp)
    y_axis_mole_fraction_H2.append(P_H2)
    x_axis_temperature_H2.append(temp)
    
plt.plot(x_axis_temperature_H2, y_axis_mole_fraction_H2, color = "orange", label = "H2")
plt.legend()

# Titles & Labels 
plt.xlabel("Temperature (K)")
plt.ylabel("mole fraction")
plt.title("The Effect of Temperature (K) on Mole Fraction")

# Saving
plt.savefig("Graphs/The_Effect_Of_Temperature(K)_On_Mole_Fraction_Version.png")


# In[201]:


# Graphs with P = 100 atm

np.linspace

# NH3, 1 atm graph
def partial_pressure_solver_1atm_NH3(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+5.196))**(0.5) / (2*(4*((answer_Kp)**(0.5))+5.196))

    return (1-2*z)/(1+2*z)

x_axis_temperature_NH3=[]
y_axis_mole_fraction_NH3=[]

for temp in np.linspace(0,800,10000):
    P_NH3 = partial_pressure_solver_1atm_NH3(temp)
    y_axis_mole_fraction_NH3.append(P_NH3)
    x_axis_temperature_NH3.append(temp)
    
plt.plot(x_axis_temperature_NH3,y_axis_mole_fraction_NH3, color = "blue", label = "NH3 (1atm)")
plt.legend()

# NH3, 100 atm graph
def partial_pressure_solver_100atm_NH3(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+519.6))**(0.5) / (2*(4*((answer_Kp)**(0.5))+519.6))

    return ((1-2*z)/(1+2*z))

x_axis_temperature_NH3_100atm=[]
y_axis_mole_fraction_NH3_100atm=[]

for temp in np.linspace(0,800,10000):
    P_NH3_100atm = partial_pressure_solver_100atm_NH3(temp)
    y_axis_mole_fraction_NH3_100atm.append(P_NH3_100atm)
    x_axis_temperature_NH3_100atm.append(temp)
    
plt.plot(x_axis_temperature_NH3_100atm,y_axis_mole_fraction_NH3_100atm, color = "blue", label = "NH3 (100atm)", linestyle = "dashed")
plt.legend()

# N2, 1 atm graph
def partial_pressure_solver_1atm_N2(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+5.196))**(0.5) / (2*(4*((answer_Kp)**(0.5))+5.196))

    return (z / (1+2*z))

x_axis_temperature_N2=[]
y_axis_mole_fraction_N2=[]

for temp in np.linspace(0,800,10000):
    P_N2 = partial_pressure_solver_1atm_N2(temp)
    y_axis_mole_fraction_N2.append(P_N2)
    x_axis_temperature_N2.append(temp)
    
plt.plot(x_axis_temperature_N2, y_axis_mole_fraction_N2, color = "green", label = "N2")
plt.legend()

# N2, 100 atm graph
def partial_pressure_solver_100atm_N2(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+519.6))**(0.5) / (2*(4*((answer_Kp)**(0.5))+519.6))

    return (z / (1+2*z))

x_axis_temperature_N2_100atm=[]
y_axis_mole_fraction_N2_100atm=[]

for temp in np.linspace(0,800,10000):
    P_N2_100atm = partial_pressure_solver_100atm_N2(temp)
    y_axis_mole_fraction_N2_100atm.append(P_N2_100atm)
    x_axis_temperature_N2_100atm.append(temp)
    
plt.plot(x_axis_temperature_N2_100atm,y_axis_mole_fraction_N2_100atm, color = "green", label = "N2 (100atm)", linestyle = "dashed")
plt.legend()

# H2, 1 atm graph
def partial_pressure_solver_1atm_H2(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+5.196))**(0.5) / (2*(4*((answer_Kp)**(0.5))+5.196))

    return (3*z / (1+2*z))

x_axis_temperature_H2=[]
y_axis_mole_fraction_H2=[]

for temp in np.linspace(0,800,10000):
    P_H2 = partial_pressure_solver_1atm_H2(temp)
    y_axis_mole_fraction_H2.append(P_H2)
    x_axis_temperature_H2.append(temp)
    
plt.plot(x_axis_temperature_H2, y_axis_mole_fraction_H2, color = "orange", label = "H2")
plt.legend()

# H2, 100 atm graph
def partial_pressure_solver_100atm_H2(T):
    answer_Gibbs = 87030 - 25.8*(T)*np.log((T))-31.7*(T)
    answer_Kp = e**(Gibbs(T)/(-R*T))
    z = (4*((answer_Kp)**(0.5))*(4*((answer_Kp)**(0.5))+519.6))**(0.5) / (2*(4*((answer_Kp)**(0.5))+519.6))

    return (3*z / (1+2*z))

x_axis_temperature_H2_100atm=[]
y_axis_mole_fraction_H2_100atm=[]

for temp in np.linspace(0,800,10000):
    P_H2_100atm = partial_pressure_solver_100atm_H2(temp)
    y_axis_mole_fraction_H2_100atm.append(P_H2_100atm)
    x_axis_temperature_H2_100atm.append(temp)
    
plt.plot(x_axis_temperature_H2_100atm,y_axis_mole_fraction_H2_100atm, color = "orange", label = "H2 (100atm)", linestyle = "dashed")
plt.legend()

# Title & Labels
plt.xlim(0, 800)
plt.ylim(0, 1.5)
plt.xlabel("Temperature (K)")
plt.ylabel("mole fraction")
plt.title("The Effect of Temperature (K) on Mole Fraction")

# Saving
plt.savefig("Graphs/The_Effect_Of_Temperature(K)_On_Mole_Fraction_Version_Pressure_Variation.png")

