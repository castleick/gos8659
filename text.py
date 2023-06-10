import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal

# Define the transfer function G(s) = 100 / (s+2)(s+3) 
s1 = signal.lti([100],[1, 5, 6])

# Define the frequency range
frequencies = np.logspace (-2, 2, 500)

# Calculate frequency response 
w, mag, phase = s1.blode(frequencies)

#create bode magnitude plot 
fig=plt.figure()
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(w, mag) #Bode magnitude plot
plt.title('Bode plot of G(S) = 100 / (s+2)(s+3)')
plt.ylabel('Magnitude [dB]')

# Create Bode phase plot 
plt.subplot(2, 1, 2)
plt.semilogx(w, phase) # Bode phase plot
plt.ylabel('Phase [degrees]')
plt.xlabel('Frequency [Hz]')
plt.show() 
st.pyplot(fig)