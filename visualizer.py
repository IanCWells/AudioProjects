#Code to visualize sound on a plot

import matplotlib.pyplot as plt
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
plt.plot(time,data)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Girl from Ipanema Cover Audio File Plot")
plt.show()