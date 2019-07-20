import numpy as np
import waterfillingAlgorithm as waterfill

#example 1
#snr = np.array([2, 26, 6.5])
#dPt = 0.75

#example 2
#This sample test is from Wireless Communication by Andrea Goldsmith
#Example 10.2
snr = np.array([2.63, 0.087, 17.77])

dPt = 1

Opt, lamda = waterfill.doWF(snr, dPt)
print("Power and lambda", Opt, lamda) 
               
