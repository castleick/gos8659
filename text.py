import matplotlib.pyplot as plt 
import numpy as np 
from scipy import signal

# Define the systems  
G0 = signal.lti([100], [1])
G1 = signal.lti([1], [1, 1, 2])
G2 = signal.lti([1], [1, 1, 3])
G3 = signal.lti([100], [1, 5, 6])

# Define the frequency range
frequencies = np.logspace (-2, 2, 500)

# Calculate frequency response
systems = [G0,G1, G2, G3]
labels = ['Proportional Element', 'Intergral Element', 'First-Order Lag Element', 'Overall System']
colors = ['r', 'g', 'b', 'm']


plt.figure(figsize=(12, 8))

# Bode magnitude plot
fig=plt.figure()
plt.subplot(2, 1, 1)
for sys, label, color in zip(systems, labels, colors):
    w, mag,_= sys.bode(frequencies)
    plt.semilogx(w, mag, color=color, label=label)
plt.title('Bode plot')
plt.ylabel('Magnitude [dB]')
plt.legend()
st.pyplot(fig)

# Bode phase plot
fig1 = plt.figure()
plt.subplot(2, 1, 2)
for sys, _, color in zip(systems, labels, colors):
    w, _, phase = sys.bode(frequencies)
    plt.semilogx(w, phase, color=color)
plt.ylabel('phase [degrees]')
plt.legend('Frequency [Hz]')

plt.show()

st.pyplot(fig1)