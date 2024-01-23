#Code to visualize sound on a plot

import matplotlib.pyplot as plt
import numpy as np
#Code for reading in our sound file. I am using a local file on my desktop for this.
import soundfile as sf # Import our soundfile dependency
data, fs = sf.read('IPAGIRL.wav') # Load a wave file called input.wav

#Here we are rrescaling our time axis to display in seconds
time = []
# Go through from 0 to the length of the data
for value in range(0, len(data)): 
    # Determine the current sample value in time
    new_time_value = value / fs
    # Add it to the resulting array   
    time.append(new_time_value)

time = [value/fs for value in range(0, len(data))]

fft_result = np.fft.fft(data)
frequencies = np.fft.fftfreq(len(fft_result), 1/fs)

#Creating a freq_range_mask totake a look at only the frequencies we would like to look at
freq_range_mask = (frequencies >= 0) & (frequencies <= 5000)
plt.subplot(2, 1, 2)
# Plot the magnitude spectrum (only positive frequencies)
plt.plot(frequencies[freq_range_mask], np.abs(fft_result[freq_range_mask]))

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT of Audio Signal")

plt.tight_layout()
plt.show()

#Our Findings Show that we most commonly have recorded G2,A2,F2, and A3 frequencies in our recording.  
#We can further explore this callibration by recorded single notes to reduce noise. 