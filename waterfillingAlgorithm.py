#implements waterfilling algorithm for multi-user networks.
import numpy as np

def doWF(snr, dPt):
    #snr: channel power/noise power
    #dPt: total power available

    assert isinstance(snr, np.ndarray), "snr should be ndimensional numpy array"
    inversSnr = 1/snr
    channelsSortedIndexes = np.argsort(inversSnr)#[::-1]
    channelsSorted = inversSnr[channelsSortedIndexes]
    dNchannels = snr.size
    dRemovedChannels = 0
    lamda =  (dPt +np.sum(channelsSorted))/dNchannels
    Ps = (lamda - channelsSorted[dNchannels-dRemovedChannels-1])
    
    while Ps<0:
        dRemovedChannels+= 1
        channelsSorted = channelsSorted[np.arange(0,dNchannels - dRemovedChannels)]
        lamda =  (dPt +np.sum(channelsSorted))/(dNchannels-dRemovedChannels)
        Ps = (lamda - channelsSorted[dNchannels-dRemovedChannels-1])
        
    powers = lamda - channelsSorted[np.arange(0,dNchannels-dRemovedChannels)]
    
    dDiffernceInPower = dPt - np.sum(powers)
    
    optP = powers + dDiffernceInPower/(dNchannels-dRemovedChannels)
    
    optindexes = channelsSortedIndexes[np.arange(0,(dNchannels-dRemovedChannels))]
    optimalAllocation = np.zeros(dNchannels)
    optimalAllocation[optindexes] = optP
    return optimalAllocation, lamda
                                      

        
        

              

