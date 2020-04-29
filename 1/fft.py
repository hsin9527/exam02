import matplotlib.pyplot as plt
import numpy as np
import serial
import time


Fs = 300

t = np.arange(0,10,1/10)

x = np.zeros(100) 
y = np.zeros(100)
z = np.zeros(100) 

serdev = '/dev/ttyACM0' 

s = serial.Serial(serdev,115200)

for i in range(300):
    line=s.readline()
    #print(line)
    if(i%3 == 0): x[int(i/3)] = float(line)
    elif(i%3 == 1): y[int(i/3)] = float(line)
    elif(i%3 == 2): z[int(i/3)] = float(line)

disa = np.zeros(100)
disb = np.zeros(100)
dis = np.zeros(100)
great =  np.zeros(100)
for i in range(100):
    tu = 0.05
    if (i==0):
        disa[i]=0
        disb[i]=0
    else:
        disa[i]=disa[i-1]+x[i-1]*9.8/2*0.1*0.1
        disb[i]=disb[i-1]+y[i-1]*9.8/2*0.1*0.1
    dis[i] = np.sqrt(disa[i]*disa[i]+disb[i]*disb[i])
    if dis[i] > tu:   great[i] = 1
    else:   great[i] = 0

fig, ax = plt.subplots(2, 1)

ax[0].plot(t,x, label = 'x')
ax[0].plot(t,y, label = 'y')
ax[0].plot(t,z, label = 'z')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[0].legend()

ax[1].stem(t,great) 
ax[1].set_xlabel('Time')
ax[1].set_ylabel('displacement larger than 5')

plt.show()

s.close()