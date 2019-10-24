
import matplotlib.pyplot as plt
import readcol

files= readcol.readcol('times.list')
Time= files[:,0]
Redshift= files[:,1]


#plt.plot(Time, Redshift)
#plt.ylabel('Redshift')
#plt.xlabel('Time')

plt.xlabel("Time 'Gyr'")
plt.ylabel("Redshift")
plt.plot(Time, Redshift, "k-", linewidth=3)
plt.tick_params(axis="Redshift", labelcolor="b")

plt.show()






