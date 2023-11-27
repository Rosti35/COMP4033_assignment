import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

"""
Final Coursework for COMP4033 by Abinaya Maruthalingam and Rostislav Shepel
"""

# Defining the Antecedent objects for the inputs
age = ctrl.Antecedent(np.arange(0, 130, 1), 'age')
# TODO: Check temperature range (start and stop) using literature
temperature = ctrl.Antecedent(np.arange(20, 50, 0.1), 'temperature')
headache = ctrl.Antecedent(np.arange(0, 11, 1), 'headache')

# Defining the Consequent object for the output
urgency = ctrl.Consequent(np.arange(0, 100, 1), 'urgency')

# Generate membership functions
age['young'] = fuzz.trapmf(age.universe, [0,0,10,10])
age['adolescent'] = fuzz.trapmf(age.universe, [10,11,17,19])
age['adult'] = fuzz.trapmf(age.universe,[18, 19, 55, 65])
age['elderly'] = fuzz.trapmf(age.universe, [60,65,130,130])

age.view()

temperature['very low'] = fuzz.trapmf(temperature.universe,[20.0,20.0,34.3,34.3])
temperature['low'] = fuzz.trapmf(temperature.universe, [34.3, 34.4, 35.4, 35.4])
temperature['slightly low'] = fuzz.trapmf(temperature.universe,[35.4, 35.5, 36.0, 36.0])
temperature['normal'] = fuzz.trapmf(temperature.universe, [36.0, 36.1, 37.2, 37.2])
temperature['slightly high'] = fuzz.trapmf(temperature.universe, [37.2, 37.3, 38.0, 38.0])
temperature['high'] = fuzz.trapmf(temperature.universe, [38.0, 38.1, 39.9, 39.9])
temperature['very high'] = fuzz.trapmf(temperature.universe, [39.9, 40, 50, 50])

temperature.view()

headache['none'] = fuzz.trimf(headache.universe, [0, 0, 0.5])
headache['mild'] = fuzz.trimf(headache.universe, [1, 3, 3])
headache['moderate'] = fuzz.trimf(headache.universe, [4, 6, 6])
headache['severe'] = fuzz.trimf(headache.universe, [7, 10, 10])

headache.view()
"""
urgency['none'] = fuzz.trapmf(urgency.universe, [0,0, 5, 10])
urgency['minor'] = fuzz.trapmf(urgency.universe, [5, 10, 30, 35])
urgency['moderate'] = fuzz.trapmf(urgency.universe, [30, 35, 65, 70])
urgency['urgent'] = fuzz.trapmf(urgency.universe, [65, 70, 100, 100])
"""
urgency['none'] = fuzz.trapmf(urgency.universe, [0, 0, 5, 10])
urgency['delayed'] = fuzz.gaussmf(urgency.universe, 25, 10)
urgency['urgent'] = fuzz.gaussmf(urgency.universe, 50, 10)
urgency['immediate'] = fuzz.trapmf(urgency.universe, [65, 75, 100, 100])

urgency.view()
# define fuzzy rules

# Solely based on Temperature

# Immediate Care (Life Threatening)
# General Extremes
rule1 = ctrl.Rule(temperature['very low'], urgency['immediate'])
rule2 = ctrl.Rule(temperature['very high'], urgency['immediate'])

# Immediate for Adults
rule3 = ctrl.Rule(temperature['low'] & age['adult'], urgency['immediate'])


# Urgent for Children
rule4 = ctrl.Rule(temperature['high'] & age['young'], urgency['urgent'])
rule5 = ctrl.Rule(temperature['high'] & age['adolescent'], urgency['urgent'])


# Temperature and Headache
rule6 = ctrl.Rule(temperature['high'] & headache['severe'], urgency['immediate'])

# Creating the Control System
urgency_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6])
urgency_simulation = ctrl.ControlSystemSimulation(urgency_ctrl)


# Get user input for distances
while True:
    age = float(input("Enter Age (0-130): "))
    if 0 <= age <= 130:
        break
    else:
        print("Age should be between 0 and 130. Please try again.")

while True:
    temperature = float(input("Enter Temperature in °C (20-50): "))
    if 0 <= temperature <= 50:
        break
    else:
        print("Temperature should be between 20 and 50. Please try again.")
while True:
    headache = float(input("Enter severity of headache (0 - 10, where 0 is None and 10 is extremely severe): "))
    if 0 <= headache <= 10:
        break
    else:
        print("Severity of headache should be between 0 and 10. Please try again.")

# Providing inputs to the system
urgency_simulation.input['age'] = age
urgency_simulation.input['temperature'] = temperature
urgency_simulation.input['headache'] = headache

urgency_simulation.compute()

if urgency_simulation.output['urgency'] <= 10:
    urgency_level = "None"
elif urgency_simulation.output['urgency'] <= 40:
    urgency_level = "Delayed"
elif urgency_simulation.output['urgency'] <= 70:
    urgency_level = "Urgent"
else:
    urgency_level = "Immediate"

print(f"Age: {age}")
print(f"Temperate /°C: {temperature}")
print(f"Severity of Headache: {headache}")

print(f"Output Urgency: {urgency_simulation.output['urgency']}")
#print(f"Defuzzified Steering: {defuzzified_steering}")
print(f"Urgency Level: {urgency_level}")

urgency.view(sim=urgency_simulation)

#TODO: Control Surface
