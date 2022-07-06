import random, math
import numpy as np

import seaborn as sns

#points = []

distances = []

r = 6_371

for i in range(10000):
    a = [np.random.normal(), np.random.normal(), np.random.normal()]
    b = [np.random.normal(), np.random.normal(), np.random.normal()]

    normal_a = 1/math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)
    normal_b = 1/math.sqrt(b[0]**2 + b[1]**2 + b[2]**2)

    a = [r*p*normal_a for p in a]
    b = [r*p*normal_b for p in b]

    d = r*math.acos((a[0]*b[0] + a[1]*b[1] + a[2]*b[2])/(r**2))

    #print("d:",d)

    distances.append(d)
    #points.append(p)

hours = [(1/0.048)*d for d in distances]
days = [h/24 for h in hours]
years = [d/365.25 for d in days]

import pandas

s = pandas.Series(years)
print(s.describe())

sns.set_theme()
sns.displot(years, kind="kde")
import matplotlib.pyplot as plt
plt.show()



#x = [p[0] for p in points]
#y = [p[1] for p in points]
#z = [p[2] for p in points]



''' Plot Code
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter(x, y, z)

plt.show()
'''