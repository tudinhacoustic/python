# # import numpy
# from scipy import stats

# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# x = stats.mode(speed)

# print(x)

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()
