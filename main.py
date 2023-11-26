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

#age.view()

temperature['very low'] = fuzz.trapmf(temperature.universe,[20.0,20.0,34.3,34.3])
temperature['low'] = fuzz.trapmf(temperature.universe, [34.3, 34.4, 35.4, 35.4])
temperature['slightly low'] = fuzz.trapmf(temperature.universe,[35.4, 35.5, 36.0, 36.0])
temperature['normal'] = fuzz.trapmf(temperature.universe, [36.0, 36.1, 37.2, 37.2])
temperature['slightly high'] = fuzz.trapmf(temperature.universe, [37.2, 37.3, 38.0, 38.0])
temperature['high'] = fuzz.trapmf(temperature.universe, [38.0, 38.1, 39.9, 39.9])
temperature['very high'] = fuzz.trapmf(temperature.universe, [39.9, 40, 50, 50])

#temperature.view()

headache['none'] = fuzz.trimf(headache.universe, [0, 0, 0.5])
headache['mild'] = fuzz.trimf(headache.universe, [1, 3, 3])
headache['moderate'] = fuzz.trimf(headache.universe, [4, 6, 6])
headache['severe'] = fuzz.trimf(headache.universe, [7, 10, 10])

#headache.view()
"""
urgency['none'] = fuzz.trapmf(urgency.universe, [0,0, 5, 10])
urgency['minor'] = fuzz.trapmf(urgency.universe, [5, 10, 30, 35])
urgency['moderate'] = fuzz.trapmf(urgency.universe, [30, 35, 65, 70])
urgency['urgent'] = fuzz.trapmf(urgency.universe, [65, 70, 100, 100])
"""
urgency['none'] = fuzz.trapmf(urgency.universe, [0, 0, 5, 10])
urgency['minor'] = fuzz.gaussmf(urgency.universe, 25, 10)
urgency['moderate'] = fuzz.gaussmf(urgency.universe, 50, 10)
urgency['urgent'] = fuzz.trapmf(urgency.universe, [65, 75, 100, 100])

urgency.view()
# define fuzzy rules

