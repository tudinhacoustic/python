import numpy

speed1 = [86, 87, 88, 86, 87, 85, 86]
speed2 = [32, 111, 138, 28, 59, 77, 97]
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# x = numpy.var(speed2)
standardDeviation = numpy.std(speed1)
average = numpy.average(ages)
print("The average is", average)
print("The standard deviation is", standardDeviation)
