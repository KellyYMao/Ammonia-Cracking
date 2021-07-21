# Overview
Ammonia-Cracking is a process in which gaseous ammonia (NH3) dissociates into nitrogen gas (N2) and hydrogen gas (H2). Ammonia-cracking is a cost-effective process way to produce hydrogen gas. The hydrogen gas obtained from ammonia-cracking can have many uses in oil refineries and thus finding ways to streamline ammonia-cracking is important. 

# Ammonia-Cracking Reaction
The reaction for gaseous ammonia decomposition is 2NH3(g) = N2(g) + 3H2(g). 

# Project Purpose
This project uses Python in order to calculate the partial pressures of ammonia gas, nitrogen gas, and hydrogen gas (product and reactants of gaseous ammonia decomposition) at various temperatures and pressures. Graphs demonstrating the effect of temperature and pressure on the respective mole fractions of ammonia gas, nitrogen gas, and hydrogen gas were plotted in Python using matplotlib. From these graphs the effects of increased temperature and increased pressure on ammonia decomposition were analyzed and conclusions were made on how to potentially increase the yield and efficiency of ammonia cracking. 

# Temperature Effect On Gaseous Ammonia Decomposition
![Image](/Ammonia_Cracking_Graphs/The_Effect_Of_Temperature(K)_On_Mole_Fraction_Version.png)

The decomposition of  gaseous ammonia is an endothermic reaction.  Increasing the temperature adds heat. According to LeChatelier’s principle, increasing the temperature will cause the equilibrium to shift to favor the endothermic reaction (the reaction which absorbs heat). In this case, that means the production of products (N2 & H2) is favored. Predictably, the graph demonstrates that the mole fraction of NH3 decreases with increasing temperature, the mole fraction of N2 increases with increasing temperature, and the mole fraction of H2 increases with increasing temperature. This indicates increased presence of N2 and H2 demonstrating a shift in equilibrium to favor the production of the products. 

# Pressure Effect On Gaseous Ammonia Decomposition
![Image](/Ammonia_Cracking_Graphs/The_Effect_Of_Temperature(K)_On_Mole_Fraction_Version_Pressure_Variation.png)

There are more moles of gas in the products (N2 & 3H2 =1+3= 4 moles) than there are moles of gas in the reactants (2NH3 = 2 moles)
According to LeChatelier’s principle, increasing the pressure will cause equilibrium to shift to favor the side of the reaction with fewer moles of gas in order to alleviate the additional pressure. In this case, that means the production of reactants (NH3) is initially favored. Predictably, the graph demonstrates that the mole fraction of NH3 decreases more slowly (flatter slope) with increasing temperature when pressure increased from 1 atm to 100 atm since the production of NH3 is initially favored. The mole fraction of N2 and H2 increases more slowly with increased temperature (flatter slope) at higher pressure, demonstrating that equilibrium shifted to favor the production of NH3.

# Conclusions
Increasing temperature can increase the production of nitrogen gas and hydrogen gas from ammonia.  
Decreasing pressure can also increase the production of nitrogen gas and hydrogen gas from ammonia.  
Though seemingly simple and straightforward in theory, these changes can help increase the efficiency and yield of hydrogen gas production via ammonia cracking
