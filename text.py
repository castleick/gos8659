import streamlit as st
import matplotlib.pyplot as plt 
import numpy as np 
from scipy import signal
import control as ctl

# 전달함수 G1 정의
G1 = ctl.TransferFunction([100],[1, 5, 6])

#전달함수 출력
st.write(G1)

#feedback
G2 = ctl.feedback(G1)

#전달함수 출력
st.write(G2)

# Step Response 그래프 그리기
fig3=plt.figure()
t, y = ctl.step_response(G2)
plt.plot(t, y)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.title('Step Response')
plt.grid()
plt.show()

st.pyplot(fig3)

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