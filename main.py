import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

"""
Final Coursework for COMP4033 by Abinaya Maruthalingam and Rostislav Shepel
"""

# Defining the Antecedent objects for the inputs
age = ctrl.Antecedent(np.arange(0, 130, 1), 'age')
# TODO: Check temperature range (start and stop) using literature
temperature = ctrl.Antecedent(np.arange(30, 45, 0.1), 'temperature')
severity_of_headache = ctrl.Antecedent(np.arange(0, 10, 1), 'headache')

# Defining the Consequent object for the output
urgency = ctrl.Consequent(np.arange(0, 100, 1), 'urgency')

# Generate membership functions



