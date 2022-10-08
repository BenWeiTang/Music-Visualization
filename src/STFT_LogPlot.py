from scipy.io.wavfile import read
from scipy import signal
import numpy as np
# import matplotlib.pyplot as plt


#importing soud file from folder
file = 'Song_for_Ellen.wav'
file_name = file.split('.')[0]
sr, samps = read(file)

#variables
samples_per_second = sr
total_samples = len(samps)
time_seconds = total_samples / samples_per_second
time_vector = np.linspace(0, time_seconds, total_samples)
samps_normed = np.interp(samps,(samps.min(), samps.max()),(-1, 1))


#STFT Spectrogram Generation
#nperseg is twice the num of freq per seg 
#using 'samples_per_second' maps index to actual freq
#the input is samps_normed therefore Sxx will fall in the range between 0, 1
f, t, Sxx = signal.spectrogram(x=samps_normed, fs=samples_per_second, nperseg=samples_per_second)

#Plotting STFT Spectrogram
# plt.pcolormesh(t,f, Sxx)
# plt.title("'{}': Log Spectrogram".format(file_name))
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()


# #Plotting STFT Spectrogram on log2 y axis
# mag = np.abs(Sxx)
# mag_log = np.log2(mag) #NOTE: it produces negative numbers
# plt.pcolormesh(t, f, mag_log)
# plt.title("'{}': Log Spectrogram".format(file_name))
# plt.yscale("symlog", basey=2) #plot the y axis to log2 scale
# plt.show()


#export to a text file in csv format
text_file_Sxx = np.array(Sxx * 10_000.0, np.uint16)
np.savetxt('{}.txt'.format(file_name), text_file_Sxx, fmt="%d", delimiter=",", newline='\n')
