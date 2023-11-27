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
age['young'] = fuzz.trapmf(age.universe, [0, 0, 10, 10])
age['adolescent'] = fuzz.trapmf(age.universe, [10, 11, 17, 19])
age['adult'] = fuzz.trapmf(age.universe, [18, 19, 55, 65])
age['elderly'] = fuzz.trapmf(age.universe, [60, 65, 130, 130])

age.view()

temperature['very low'] = fuzz.trapmf(temperature.universe, [20.0, 20.0, 34.3, 34.3])
temperature['low'] = fuzz.trapmf(temperature.universe, [34.3, 34.4, 35.4, 35.4])
temperature['slightly low'] = fuzz.trapmf(temperature.universe, [35.4, 35.5, 36.0, 36.0])
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

urgency['none'] = fuzz.trapmf(urgency.universe, [0, 0, 5, 10])
urgency['delayed'] = fuzz.gaussmf(urgency.universe, 25, 10)
urgency['urgent'] = fuzz.gaussmf(urgency.universe, 50, 10)
urgency['immediate'] = fuzz.trapmf(urgency.universe, [65, 75, 100, 100])

urgency.view()
# print(urgency.defuzzify_method)

""" Define Fuzzy Ruleset """

# Solely based on Temperature

"""Immediate Care (Standard Rule)"""
# Temperature = very high or very low - indicative of high-grade fever or hypothermia
rule0 = ctrl.Rule(antecedent=(temperature['very high'] | temperature['very low']),
                  consequent=urgency['immediate'], label='extreme temperature - immediate')
# Headache = Severe (8-10)
rule1 = ctrl.Rule(antecedent=(headache['severe']),
                  consequent=urgency['immediate'], label='severe headache - immediate')

"""No Hospital Needed (Age-Specific)"""
# Adults
rule2 = ctrl.Rule(antecedent=(age['adult'] &
                              temperature['normal'] &
                              (headache['none'] | headache['mild'] | headache['moderate'])),
                  consequent=urgency['none'], label='adult normal - none')
# Elderly
rule3 = ctrl.Rule(antecedent=(age['elderly'] &
                              (temperature['low'] | temperature['slightly low'] | temperature['normal'] |
                               temperature['slightly high']) &
                              (headache['none'] | headache['mild'])),
                  consequent=urgency['none'], label='elderly normal - none')
# Young and Adolescent Children
rule4 = ctrl.Rule(antecedent=((age['young'] | age['adolescent']) &
                              (temperature['normal'] | temperature['slightly high'] & temperature['slightly low']) &
                              (headache['none'] | headache['mild'])),
                  consequent=urgency['none'], label='children normal - none')

"""Delayed Admittance - Minor Urgency (Age-Specific)"""
# Elderly with normal temperature but moderate headache
rule5 = ctrl.Rule(antecedent=(age['elderly'] &
                              (temperature['low'] | temperature['slightly low'] | temperature['normal'] |
                               temperature['slightly high']) &
                              headache['moderate']),
                  consequent=urgency['delayed'], label='elderly moderate headache - delayed')

# Adults with delayed admittance - temp: low: possible hypothermia, high: possible fever, with a headache.
# Can be remedied at home in the worst case too (moderate headache and high temp)
rule6 = ctrl.Rule(antecedent=(age['adult'] &
                              (temperature['slightly low'] | temperature['slightly high'] | temperature['high']) &
                              (headache['none'] | headache['mild'] | headache['moderate'])),
                  consequent=urgency['delayed'], label='adult slight temp - delayed')

# Children with slight fever
rule7 = ctrl.Rule(antecedent=((age['young'] | age['adolescent']) &
                              temperature['high'] &
                              (headache['none'] | headache['mild'])),
                  consequent=urgency['delayed'], label='children slight fever - delayed')

"""Urgent Admittance - Major but not life threatening"""
# Children with fever
rule8 = ctrl.Rule(antecedent=((age['young'] | age['adolescent']) &
                              temperature['high'] &
                              (headache['moderate'])),
                  consequent=urgency['urgent'], label='children fever - urgent')

# Elderly - Outside the temperature range
rule10 = ctrl.Rule(antecedent=(age['elderly'] &
                               temperature['high'] &
                               (headache['none'] | headache['mild'])),
                   consequent=urgency['urgent'], label='elderly high temp - urgent')

"""Immediate Admittance"""
rule11 = ctrl.Rule(antecedent=(age['elderly'] &
                               temperature['high'] &
                               headache['moderate']),
                   consequent=urgency['immediate'], label='elderly high temp and moderate headache - immediate')

# Get user input for age, temperature, and severity of headache
while True:
    age = int(input("Enter Age (0-130): "))
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
    headache = int(input("Enter severity of headache (0 - 10, where 0 is None and 10 is extremely severe): "))
    if 0 <= headache <= 10:
        break
    else:
        print("Severity of headache should be between 0 and 10. Please try again.")

# Creating the Control System
urgency_ctrl = ctrl.ControlSystem(rules=[rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
urgency_simulation = ctrl.ControlSystemSimulation(urgency_ctrl)

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
print(f"Urgency Level: {urgency_level}")

urgency.view(sim=urgency_simulation)

# TODO: Control Surface
