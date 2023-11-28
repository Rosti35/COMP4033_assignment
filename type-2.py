# Import necessary libraries
import numpy as np
import math
from juzzyPython.generic.Tuple import Tuple
from juzzyPython.generic.Plot import Plot
from juzzyPython.intervalType2.sets.IntervalT2MF_Gaussian import IntervalT2MF_Gaussian
from juzzyPython.type1.sets.T1MF_Gaussian import T1MF_Gaussian
from juzzyPython.type1.sets.T1MF_Gauangle import T1MF_Gauangle
from juzzyPython.intervalType2.sets.IntervalT2MF_Trapezoidal import IntervalT2MF_Trapezoidal
from juzzyPython.intervalType2.sets.IntervalT2MF_Gauangle import IntervalT2MF_Gauangle
from juzzyPython.intervalType2.system.IT2_Antecedent import IT2_Antecedent
from juzzyPython.intervalType2.system.IT2_Consequent import IT2_Consequent
from juzzyPython.intervalType2.system.IT2_Rule import IT2_Rule
from juzzyPython.intervalType2.system.IT2_Rulebase import IT2_Rulebase
from juzzyPython.generic.Input import Input
from juzzyPython.generic.Output import Output
from juzzyPython.type1.sets.T1MF_Trapezoidal import T1MF_Trapezoidal

plot = Plot()

headache_imf = IntervalT2MF_Gauangle("inputmf",
    T1MF_Gauangle("inputumf", 2, 3, 4),
    T1MF_Gauangle("inputlmf", 2, 3, 4))

temp_imf = IntervalT2MF_Trapezoidal("inputmf",
    T1MF_Trapezoidal("inputumf", [0, 0, 1, 1]),
    T1MF_Trapezoidal("inputumf", [0, 0, 1, 1]))

age_imf = IntervalT2MF_Trapezoidal("inputmf",
    T1MF_Trapezoidal("inputumf", [0, 0, 0, 0]),
    T1MF_Trapezoidal("inputlmf", [0, 0, 0, 0]))

# Define Input and Output objects
temperature_input = Input('Temperature', Tuple(0, 45), inputMF=temp_imf)
headache_input = Input('Headache', Tuple(0, 10), inputMF=headache_imf)
age_input = Input('Age', Tuple(0, 130))
urgency_output = Output('Urgency', Tuple(0, 100))

# Define Type-2 Membership Functions for Temperature
# temperature['very low'] = fuzz.trapmf(temperature.universe,[20.0,20.0,34.3,34.3])
# temperature['low'] = fuzz.trapmf(temperature.universe, [34.3, 34.4, 35.4, 35.4])
# temperature['slightly low'] = fuzz.trapmf(temperature.universe,[35.4, 35.5, 36.0, 36.0])
# temperature['normal'] = fuzz.trapmf(temperature.universe, [36.0, 36.1, 37.2, 37.2])
# temperature['slightly high'] = fuzz.trapmf(temperature.universe, [37.2, 37.3, 38.0, 38.0])
# temperature['high'] = fuzz.trapmf(temperature.universe, [38.0, 38.1, 39.9, 39.9])
# temperature['very high'] = fuzz.trapmf(temperature.universe, [39.9, 40, 50, 50])

temperature_very_low_UMF = T1MF_Trapezoidal('Temperature very_Low UMF', [20.0,20.0,34.3,34.3])
temperature_very_low_LMF = T1MF_Trapezoidal('Temperature very_Low LMF', [20.0,20.0,34.3,34.3])
temperature_very_low = IntervalT2MF_Trapezoidal('Temperature very Low', temperature_very_low_UMF, temperature_very_low_LMF)

temperature_low_UMF = T1MF_Trapezoidal('Temperature Low UMF', [34.3, 34.4, 35.4, 35.4])
temperature_low_LMF = T1MF_Trapezoidal('Temperature Low LMF', [34.3, 34.4, 35.4, 35.4])
temperature_low = IntervalT2MF_Trapezoidal('Temperature Low', temperature_low_UMF, temperature_low_LMF)

temperature_normal_UMF = T1MF_Trapezoidal('Temperature Normal UMF', [35.4, 35.5, 38.0, 38.0])
temperature_normal_LMF = T1MF_Trapezoidal('Temperature Normal LMF', [36.0, 36.1, 37.2, 37.2])
temperature_normal = IntervalT2MF_Trapezoidal('Temperature Normal', temperature_normal_UMF, temperature_normal_LMF)

temperature_high_UMF =  T1MF_Trapezoidal('Temperature High UMF',[38.0, 38.1, 39.9, 39.9])
temperature_high_LMF =  T1MF_Trapezoidal('Temperature High LMF', [38.0, 38.1, 39.9, 39.9])
temperature_high = IntervalT2MF_Trapezoidal('Temperature High', temperature_high_UMF, temperature_high_LMF)

temperature_very_high_UMF =  T1MF_Trapezoidal('Temperature very_High UMF', [39.9, 40, 50, 50])
temperature_very_high_LMF =  T1MF_Trapezoidal('Temperature very_High LMF', [39.9, 40, 50, 50])
temperature_very_high = IntervalT2MF_Trapezoidal('Temperature very High', temperature_very_high_UMF, temperature_very_high_LMF)

# Define Type-2 Membership Functions for Headache

# headache['none'] = fuzz.trimf(headache.universe, [0, 0, 0.5])
# headache['mild'] = fuzz.trimf(headache.universe, [1, 3, 3])
# headache['moderate'] = fuzz.trimf(headache.universe, [4, 6, 6])
# headache['severe'] = fuzz.trimf(headache.universe, [7, 10, 10])

headache_none_UMF = T1MF_Gauangle('Headache none UMF', 0, 0, 2)
headache_none_LMF = T1MF_Gauangle('Headache none LMF', 0, 0, 1)
headache_none = IntervalT2MF_Gauangle('Headache None', headache_none_UMF, headache_none_LMF)

headache_mild_UMF = T1MF_Gauangle('Headache Mild UMF', 1, 3, 4)
headache_mild_LMF = T1MF_Gauangle('Headache Mild LMF', 1, 3, 3)
headache_mild = IntervalT2MF_Gauangle('Headache Mild', headache_mild_UMF, headache_mild_LMF)

headache_moderate_UMF = T1MF_Gauangle('Headache Moderate UMF', 3, 6, 7)
headache_moderate_LMF = T1MF_Gauangle('Headache Moderate LMF', 4, 6, 6)
headache_moderate = IntervalT2MF_Gauangle('Headache Moderate', headache_moderate_UMF, headache_moderate_LMF)

headache_severe_UMF = T1MF_Gauangle('Headache Severe UMF', 6, 10, 10)
headache_severe_LMF = T1MF_Gauangle('Headache Severe LMF', 7, 10, 10)
headache_severe = IntervalT2MF_Gauangle('Headache Severe', headache_severe_UMF, headache_severe_LMF)

# Define Type-2 Membership Functions for Age

age_young_UMF = T1MF_Trapezoidal('Age young UMF', [0, 0, 10, 10])
age_young_LMF = T1MF_Trapezoidal('Age young LMF', [0, 0, 10, 8])
age_young = IntervalT2MF_Trapezoidal('Age young', age_young_UMF, age_young_LMF)

age_adolescent_UMF = T1MF_Trapezoidal('Age adolescent UMF', [10, 11, 17, 19])
age_adolescent_LMF =  T1MF_Trapezoidal('Age adolescent LMF', [10, 11, 17, 19])
age_adolescent = IntervalT2MF_Trapezoidal('Age adolescent', age_adolescent_UMF, age_adolescent_LMF)

age_adult_UMF = T1MF_Trapezoidal('Age Adult UMF', [8, 19, 55, 65])
age_adult_LMF = T1MF_Trapezoidal('Age Adult LMF', [8, 19, 55, 65])
age_adult = IntervalT2MF_Trapezoidal('Age Adult', age_adult_UMF, age_adult_LMF)

age_elderly_UMF = T1MF_Trapezoidal('Age Elderly UMF', [60, 65, 130, 130])
age_elderly_LMF = T1MF_Trapezoidal('Age Elderly LMF', [60, 65, 130, 130])
age_elderly = IntervalT2MF_Trapezoidal('Age Elderly', age_elderly_UMF, age_elderly_LMF)

# Define Type-2 Membership Functions for Urgency

# urgency['none'] = fuzz.trapmf(urgency.universe, [0, 0, 5, 10])
# urgency['delayed'] = fuzz.gaussmf(urgency.universe, 25, 10)
# urgency['urgent'] = fuzz.gaussmf(urgency.universe, 50, 10)
# urgency['immediate'] = fuzz.trapmf(urgency.universe, [65, 75, 100, 100])

urgency_none_UMF =T1MF_Trapezoidal('Urgency none UMF', [0, 0, 5, 10])
urgency_none_LMF = T1MF_Trapezoidal('Urgency none LMF',[0, 0, 5, 10])
urgency_none = IntervalT2MF_Gauangle('Urgency none', urgency_none_UMF, urgency_none_LMF)

urgency_delayed_UMF = T1MF_Gaussian('Urgency delayed UMF', 25, 10)
urgency_delayed_LMF = T1MF_Gaussian('Urgency delayed LMF', 25, 10)
urgency_delayed = IntervalT2MF_Gaussian('Urgency delayed', urgency_delayed_UMF, urgency_delayed_LMF)

urgency_urgent_UMF = T1MF_Gaussian('Urgency urgent UMF',  50, 10)
urgency_urgent_LMF = T1MF_Gaussian('Urgency urgent LMF',  50, 10)
urgency_urgent = IntervalT2MF_Gaussian('Urgency urgent', urgency_urgent_UMF, urgency_urgent_LMF)

urgency_immediate_UMF =T1MF_Trapezoidal('Urgency immediate UMF', [65, 75, 100, 100])
urgency_immediate_LMF = T1MF_Trapezoidal('Urgency immediate LMF',[65, 75, 100, 100])
urgency_immediate = IntervalT2MF_Gauangle('Urgency immediate', urgency_immediate_UMF, urgency_immediate_LMF)

# Create Antecedents for temperature, headache, and age
temperature_very_low_antecedent = IT2_Antecedent(temperature_very_low, temperature_input, 'very low')
temperature_low_antecedent = IT2_Antecedent(temperature_low, temperature_input, 'low')
temperature_normal_antecedent = IT2_Antecedent(temperature_normal, temperature_input, 'normal')
temperature_high_antecedent = IT2_Antecedent(temperature_high, temperature_input, 'high')
temperature_very_high_antecedent = IT2_Antecedent(temperature_very_high, temperature_input, 'very high')

# Create similar antecedents for other temperature ranges, headache, and age
headache_none_antecedent = IT2_Antecedent(headache_none, headache_input, 'none')
headache_mild_antecedent = IT2_Antecedent(headache_mild, headache_input, 'mild')
headache_moderate_antecedent = IT2_Antecedent(headache_moderate, headache_input, 'moderate')
headache_severe_antecedent = IT2_Antecedent(headache_severe, headache_input, 'severe')

age_young_antecedent = IT2_Antecedent(age_young, age_input, 'young')
age_adolescent_antecedent = IT2_Antecedent(age_adolescent, age_input, 'adolescent')
age_adult_antecedent = IT2_Antecedent(age_adult, age_input, 'adult')
age_elderly_antecedent = IT2_Antecedent(age_elderly, age_input, 'elderly')

# Create Consequents for urgency
urgency_none_consequent = IT2_Consequent(urgency_none, urgency_output, 'none')  
urgency_delayed_consequent = IT2_Consequent(urgency_delayed, urgency_output, 'delayed')
urgency_urgent_consequent = IT2_Consequent(urgency_urgent, urgency_output, 'urgent')
urgency_immediate_consequent = IT2_Consequent(urgency_immediate, urgency_output, 'immediate')

# Define rules
rule1g = IT2_Rule([temperature_low_antecedent, headache_mild_antecedent], consequent=urgency_delayed_consequent)
rule2g = IT2_Rule([temperature_low_antecedent, headache_moderate_antecedent], consequent=urgency_urgent_consequent)
rule3g = IT2_Rule([temperature_low_antecedent, headache_severe_antecedent], consequent=urgency_immediate_consequent)
rule31g = IT2_Rule([temperature_low_antecedent, headache_none_antecedent], consequent=urgency_delayed_consequent)
rule41g = IT2_Rule([temperature_normal_antecedent, headache_none_antecedent], consequent=urgency_none_consequent)
rule4g = IT2_Rule([temperature_normal_antecedent, headache_mild_antecedent], consequent=urgency_none_consequent)
rule5g = IT2_Rule([temperature_normal_antecedent, headache_moderate_antecedent], consequent=urgency_delayed_consequent)
rule6g = IT2_Rule([temperature_normal_antecedent, headache_severe_antecedent], consequent=urgency_immediate_consequent)
rule71g = IT2_Rule([temperature_high_antecedent, headache_none_antecedent], consequent=urgency_delayed_consequent)
rule7g = IT2_Rule([temperature_high_antecedent, headache_mild_antecedent], consequent=urgency_delayed_consequent)
rule8g = IT2_Rule([temperature_high_antecedent, headache_moderate_antecedent], consequent=urgency_urgent_consequent)
rule9g = IT2_Rule([temperature_high_antecedent, headache_severe_antecedent], consequent=urgency_immediate_consequent)

rule9g = IT2_Rule([temperature_high_antecedent, headache_severe_antecedent], consequent=urgency_immediate_consequent)

# rule10g = IT2_Rule([temperature_very_high_antecedent], consequent=urgency_immediate_consequent)
# rule11g = IT2_Rule([temperature_very_low_antecedent], consequent=urgency_immediate_consequent)


# Immediate Care (Standard Rules)
rule0g_vhigh = IT2_Rule([temperature_very_high_antecedent], consequent=urgency_immediate_consequent)
rule0g_vlow = IT2_Rule([temperature_very_low_antecedent], consequent=urgency_immediate_consequent)
rule1g = IT2_Rule([headache_severe_antecedent], consequent=urgency_immediate_consequent)

# # No Hospital Needed (Age-Specific) - Adults
rule2g = IT2_Rule([age_adult_antecedent, temperature_normal_antecedent], consequent=urgency_none_consequent)

# Elderly with various temperature conditions
rule3g_low = IT2_Rule([age_elderly_antecedent, temperature_low_antecedent], consequent=urgency_none_consequent)
# rule3g_slightly_low = IT2_Rule([age_elderly_antecedent, temperature_normal_antecedent], consequent=urgency_none_consequent)
rule3g_normal = IT2_Rule([age_elderly_antecedent, temperature_normal_antecedent], consequent=urgency_none_consequent)
# rule3g_slightly_high = IT2_Rule([age_elderly_antecedent, temperature_normal_antecedent], consequent=urgency_none_consequent)

# Elderly with headache conditions
rule3g_headache_none = IT2_Rule([age_elderly_antecedent, headache_none_antecedent], consequent=urgency_none_consequent)
rule3g_headache_mild = IT2_Rule([age_elderly_antecedent, headache_mild_antecedent], consequent=urgency_none_consequent)

# Young and Adolescent Children
rule4g_young_normal = IT2_Rule([age_young_antecedent, temperature_normal_antecedent], consequent=urgency_none_consequent)
# rule4g_young_slightly_high = IT2_Rule([age_young_antecedent, temperature_normal_antecedent], consequent=urgency_none_consequent)
rule4g_adolescent_normal = IT2_Rule([age_adolescent_antecedent, temperature_normal_antecedent], consequent=urgency_none_consequent)
# rule4g_adolescent_slightly_high = IT2_Rule([age_adolescent_antecedent, temperature_normal_antecedent], consequent=urgency_none_consequent)

# Additional rules for young and adolescent with temperature slightly low
rule5g_young = IT2_Rule([age_young_antecedent, temperature_normal_antecedent], consequent=urgency_none_consequent)
rule6g_adolescent = IT2_Rule([age_adolescent_antecedent, temperature_normal_antecedent], consequent=urgency_none_consequent)

# Additional rules for headache condition in adolescents
rule6g_adolescent_headache_none = IT2_Rule([age_adolescent_antecedent, headache_none_antecedent], consequent=urgency_none_consequent)
rule6g_adolescent_headache_mild = IT2_Rule([age_adolescent_antecedent, headache_mild_antecedent], consequent=urgency_none_consequent)

# Delayed Admittance - Minor Urgency (Age-Specific) - Elderly
rule7g_elderly_low = IT2_Rule([age_elderly_antecedent, temperature_low_antecedent, headache_moderate_antecedent], consequent=urgency_delayed_consequent)
# rule7g_elderly_slightly_low = IT2_Rule([age_elderly_antecedent, temperature_normal_antecedent, headache_moderate_antecedent], consequent=urgency_delayed_consequent)
rule7g_elderly_normal = IT2_Rule([age_elderly_antecedent, temperature_normal_antecedent, headache_moderate_antecedent], consequent=urgency_delayed_consequent)
# rule7g_elderly_slightly_high = IT2_Rule([age_elderly_antecedent, temperature_normal_antecedent, headache_moderate_antecedent], consequent=urgency_delayed_consequent)

# Adults with delayed admittance - various temperature conditions
# rule8g_adult_slightly_low = IT2_Rule([age_adult_antecedent, temperature_normal_antecedent], consequent=urgency_delayed_consequent)
# rule8g_adult_slightly_high = IT2_Rule([age_adult_antecedent, temperature_normal_antecedent], consequent=urgency_delayed_consequent)
rule8g_adult_high = IT2_Rule([age_adult_antecedent, temperature_high_antecedent], consequent=urgency_delayed_consequent)

# Children with slight fever
rule9g_young_high = IT2_Rule([age_young_antecedent, temperature_high_antecedent, headache_none_antecedent, headache_mild_antecedent], consequent=urgency_delayed_consequent)
rule9g_adolescent_high = IT2_Rule([age_adolescent_antecedent, temperature_high_antecedent, headache_none_antecedent, headache_mild_antecedent], consequent=urgency_delayed_consequent)

# Adolescent with low temperature and moderate headache
rule10g = IT2_Rule([age_adolescent_antecedent, temperature_normal_antecedent, headache_moderate_antecedent], consequent=urgency_delayed_consequent)

# Urgent Admittance - Major but not life-threatening - Children with fever
rule11g_young = IT2_Rule([age_young_antecedent, temperature_high_antecedent, headache_moderate_antecedent], consequent=urgency_urgent_consequent)
rule11g_adolescent = IT2_Rule([age_adolescent_antecedent, temperature_high_antecedent, headache_moderate_antecedent], consequent=urgency_urgent_consequent)

# Elderly - high temperature
rule12g = IT2_Rule([age_elderly_antecedent, temperature_high_antecedent, headache_none_antecedent], consequent=urgency_urgent_consequent)
rule12g1 = IT2_Rule([age_elderly_antecedent, temperature_high_antecedent, headache_mild_antecedent], consequent=urgency_urgent_consequent)
# Immediate Admittance - Hypothermia
rule13g_adult = IT2_Rule([age_adult_antecedent, temperature_low_antecedent], consequent=urgency_immediate_consequent)
rule13g_young = IT2_Rule([age_young_antecedent, temperature_low_antecedent], consequent=urgency_immediate_consequent)
rule13g_adolescent = IT2_Rule([age_adolescent_antecedent, temperature_low_antecedent], consequent=urgency_immediate_consequent)

# Elderly with high temperature and moderate headache
rule14g = IT2_Rule([age_elderly_antecedent, temperature_high_antecedent, headache_moderate_antecedent], consequent=urgency_immediate_consequent)


# Create a rulebase and add rules
rulebase = IT2_Rulebase()

# Adding rules to the rulebase
rulebase.addRule(rule2g)
rulebase.addRule(rule3g_low)
rulebase.addRule(rule3g_normal)
rulebase.addRule(rule3g_headache_none)
rulebase.addRule(rule3g_headache_mild)
rulebase.addRule(rule4g_young_normal)
rulebase.addRule(rule4g_adolescent_normal)
rulebase.addRule(rule5g_young)
rulebase.addRule(rule6g_adolescent)
rulebase.addRule(rule6g_adolescent_headache_none)
rulebase.addRule(rule6g_adolescent_headache_mild)
rulebase.addRule(rule7g_elderly_low)
rulebase.addRule(rule7g_elderly_normal)
rulebase.addRule(rule8g_adult_high)
rulebase.addRule(rule9g_young_high)
rulebase.addRule(rule9g_adolescent_high)
rulebase.addRule(rule10g)
rulebase.addRule(rule11g_young)
rulebase.addRule(rule11g_adolescent)
rulebase.addRule(rule12g)
rulebase.addRule(rule12g1)
rulebase.addRule(rule13g_adult)
rulebase.addRule(rule13g_young)
rulebase.addRule(rule13g_adolescent)
# Adding rules to the rulebase
rulebase.addRule(rule1g)
rulebase.addRule(rule2g)
rulebase.addRule(rule3g)
rulebase.addRule(rule31g)
rulebase.addRule(rule41g)
rulebase.addRule(rule4g)
rulebase.addRule(rule5g)
rulebase.addRule(rule6g)
rulebase.addRule(rule71g)
rulebase.addRule(rule7g)
rulebase.addRule(rule8g)
rulebase.addRule(rule9g)

rulebase.addRule(rule14g)
rulebase.addRule(rule0g_vhigh)
rulebase.addRule(rule0g_vlow)
rulebase.addRule(rule1g)
rulebase.addRule(rule3g)
rulebase.addRule(rule6g)
rulebase.addRule(rule9g)

print(rulebase.toString())

def plotMFs(name, sets, discretizationLevel):
    """
    Plot the membership functions (MFs) for a given set of fuzzy sets.

    Parameters:
    name (str): Title of the plot.
    sets (list): List of fuzzy sets to be plotted.
    xAxisRange (tuple): The range of x-axis values.
    discretizationLevel (int): The number of points to discretize the MFs.
    """
    # Validate inputs
    if not sets or discretizationLevel <= 0:
        raise ValueError("Invalid sets or discretizationLevel")

    # Plotting
    plot.figure()
    plot.title(name)

    for i in range(len(sets)):
        plot.plotMF2(name.replace("Membership Functions",""),sets[i].getName(),sets[i],discretizationLevel,True)
    
    plot.legend()
    plot.show()
    
    
    
def getControlSurfaceData(useCentroidDefuzz,input1Discs,input2Discs,unit = False) -> None:
        """Get the data to plot the control surface"""
        if unit:
            test = []
        temp_range = Tuple(34,42)
        incrX = temp_range.getSize()/(input1Discs-1.0)
        incrY = headache_input.getDomain().getSize()/(input2Discs-1.0)
        x = []
        y = []
        z = [ [0]*input1Discs for i in range(input2Discs)]

        for i in range(input1Discs):
            x.append(temp_range.getLeft() + i*incrX)
        for i in range(input2Discs):
            y.append(headache_input.getDomain().getLeft()+i*incrY)
        
        for x_ in range(input1Discs):
            temperature_input.setInput(x[x_])
            for y_ in range(input2Discs):
                headache_input.setInput(y[y_])
                if useCentroidDefuzz:
                    out = rulebase.evaluate(1).get(urgency_output)
                else:
                    out = rulebase.evaluate(0).get(urgency_output)
                if out == None or math.isnan(out):
                    z[y_][x_] = 0.0
                    if unit:
                        test.append(0.0)
                else:
                    z[y_][x_] = out
                    if unit:
                        test.append(out)
        if unit:
            return test
        plot.plotControlSurface(x,y,z,temperature_input.getName(),headache_input.getName(),urgency_output.getName())
        
        

def output_single(age, headache, temperature, red_t = 0):
    
    if any(param < 0 for param in [age, headache, temperature]):
        raise ValueError("Input parameters cannot be negative")
    
    age_input.setInput(age)
    headache_input.setInput(headache)
    temperature_input.setInput(temperature)


    urgency = rulebase.evaluate(red_t).get(urgency_output)
    
    return urgency 

# def get1(age_l, age_u, headache_l, headache_u, temp_l, temp_u):
#     if age_l == age_u:
#         (age_l, age_u) = (age_l - 0.5, age_l + 0.5)

#     age_input.setInputMF(T1MF_Trapezoidal("inputmf", [age_l, age_l, age_u, age_u]))
#     headache_input.setInputMF(T1MF_Gauangle("inputmf", headache_l, (headache_l + headache_u) / 2, headache_u))
#     temperature_input.setInputMF(T1MF_Gauangle("inputmf", temp_l, (temp_l + temp_u)/2, temp_u))

#     #(peak, peak_x) = reduction_lom(rulebase)
#     u = rulebase.evaluate(0).get(urgency_output)
#     return u

def output_interval(age_lower, age_upper, headache_lower, headache_upper, temp_lower, temp_upper, red_t = 1):
    # Validate input parameters
    if any(param < 0 for param in [age_lower, age_upper, headache_lower, headache_upper, temp_lower, temp_upper]):
        raise ValueError("Input parameters cannot be negative")
    
    
    age_input.setInputMF(T1MF_Trapezoidal("AgeMF", [age_lower, age_lower, age_upper, age_upper]))
    headache_input.setInputMF(T1MF_Gauangle("HeadacheMF", headache_lower, (headache_lower + headache_upper) / 2, headache_upper))
    temperature_input.setInputMF(T1MF_Gauangle("inputmf", temp_lower, (temp_lower + temp_upper)/2, temp_upper))

    # Evaluate the rulebase
    try:
        urgency_value = rulebase.evaluate(red_t).get(urgency_output)
    except Exception as e:
        raise RuntimeError(f"Error in rulebase evaluation: {e}")

    # Return urgency and its defuzzified value
    return urgency_value  # defuzz(urgency_value)



# plotMFs("Temperature Membership Functions", [temperature_very_low, temperature_low, temperature_normal, temperature_high,temperature_very_high], 43)
# plotMFs("Age Membership Functions", [age_young, age_adolescent, age_adult, age_elderly], 130)
# plotMFs("Headache Membership Functions", [headache_none, headache_mild, headache_moderate, headache_severe], 100)
# plotMFs("Urgency Membership Functions", [urgency_none, urgency_delayed, urgency_urgent, urgency_immediate], 100)


# age_input.setInput(30)
# getControlSurfaceData(False, 100, 100)
# plot.show()
print(f"Urgency interval: {output_interval(80, 80, 0, 1, 35, 36, 1)}")
# print(f"Urgency single: {output_single(30, 9, 36.5)}")
