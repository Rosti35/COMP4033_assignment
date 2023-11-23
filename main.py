import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Step 1: Create the universe of variables and fuzzy variables
temperature = ctrl.Antecedent(np.arange(30, 42, 1), 'temperature')
headache = ctrl.Antecedent(np.arange(0, 11, 1), 'headache')
age = ctrl.Antecedent(np.arange(0, 131, 1), 'age')
urgency = ctrl.Consequent(np.arange(0, 101, 1), 'urgency')

# Step 2: Generate fuzzy membership functions
temperature.automf(3)  # Simple three-point scale
headache.automf(3)     # Simple three-point scale
age.automf(3)          # Simple three-point scale
urgency.automf(3)      # Simple three-point scale

# Step 3: Define fuzzy rules
rule1 = ctrl.Rule(temperature['poor'] | headache['poor'] | age['poor'], urgency['poor'])
rule2 = ctrl.Rule(temperature['average'] | headache['average'], urgency['average'])
rule3 = ctrl.Rule(temperature['good'] | headache['good'] | age['good'], urgency['good'])

# Step 4: Control system and simulation
urgency_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
urgency_simulation = ctrl.ControlSystemSimulation(urgency_ctrl)

# Example usage
urgency_simulation.input['temperature'] = 39  # Example temperature
urgency_simulation.input['headache'] = 5      # Example headache severity
urgency_simulation.input['age'] = 40          # Example age

# Step 5: Compute the result
urgency_simulation.compute()
print(f"Urgency Level: {urgency_simulation.output['urgency']}")

