import matplotlib.pyplot as plt
import numpy as np

topic = [i for i in range(2,11)]
ll = []
paraNum = 1138 * np.array(topic) + np.array(topic) * 12819

for t in topic:
    filename = str(t) + "_output.txt"
    with open(filename) as f:
        print "read " + filename 
        text = f.readlines()
        target = text[-3]
        ll.append(int(target[target.find('-') : ]))

aic = 2 * paraNum - 2 * np.array(ll)
