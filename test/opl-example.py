# This is an example of how to call from Python.
import subprocess 

model = '../models/resource-sched-model-4.mod'
data = './problems/init_test_1.dat'

# Call a subprocess
#subprocess.check_call(['oplrun','../models/resource-sched-model-4.mod', './problems/init_test_1.dat'])

# Call a subprocess and get the output as a string into a variable
raw_output = subprocess.check_output(['oplrun', model, data])
print("Raw Output:")
print(raw_output)
