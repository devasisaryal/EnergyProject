############################################################################################################
# Author: Devasis Aryal
# Date: 4 April 2022
# This program will calculate the amount of power a wind turbine can generate
# Input: Average wind speed, radius of a cross-section of the turbine, operational effiency of the turbine
# Output: Amount of actual power a wind turbine can generate
###########################################################################################################

# Constants
import math

PI = math.pi
RHO = 1.2 # kg/m^(3)

radius_of_turbine_blades = 3.0 #m, radius of a cross section of a turbine
average_wind_speed = 12.29 #m/s
operational_efficiency = .10 #percent
cross_sectional_area= PI*(radius_of_turbine_blades**2) #m^(2)
print(cross_sectional_area)
max_power= 0.5*RHO*cross_sectional_area*(average_wind_speed**3) #W, max power of a turbine
print(max_power)
actual_power= operational_efficiency*max_power #watts
print(actual_power)



