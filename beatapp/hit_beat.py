import soundfile as sf
import io

from six.moves.urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np

def getSignal(audio):
  data, samplerate = sf.read(io.BytesIO(urlopen(audio).read()))

  return data


def getPeak(signal_1, signal_2):
    if len(signal_1)<len(signal_2):
        peak1 = []
        for i in range(0,len(signal_1),20):
            peak1.append(np.max(signal_1[i:i+20]))
        peak1 = np.array(peak1)
        peak2 = []
        for i in range(0,len(signal_2[0:len(signal_1)]),20):
            peak2.append(np.max(signal_2[i:i+20]))
        peak2 = np.array(peak2)

    else:
        peak1 = []
        for i in range(0,len(signal_2),20):
            peak1.append(np.max(signal_1[i:i+20]))
        peak1 = np.array(peak1)
        peak2 = []
        for i in range(0,len(signal_2[0:]),20):
            peak2.append(np.max(signal_2[i:i+20]))
        peak2 = np.array(peak2)
    return peak1, peak2

def getscore(audio_1, audio_2):
    signal_1 = getSignal(audio_1)
    signal_2 = getSignal(audio_2)

    peak = getPeak(signal_1,signal_2)
    return 100-(np.sum(np.abs(peak[0]-peak[1]))/peak[0].shape[0])*100
