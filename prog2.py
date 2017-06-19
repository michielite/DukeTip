import numpy as np
import matplotlib.pyplot as plt
x = [-40, -20, 0, 20, 40, 60, 80]
y = [61, 177.33, 296.33, 680.33, 651, 534.67, 24.67]

result = np.polyfit(x, y, 3)
print(result)
eq = np.poly1d(result)
print(eq)
x2 = np.arange(-40, 90)
while True:
    angle=raw_input("Enter an angle between -40 and 90 degrees")
    number = int(angle)
    if number <=90 and number >=(-40):
        print(eq(number))
    else:
        print("Pleaase Enter a value between -40 and 90")
        break
yfit = np.polyval(result, x2)
plt.plot(x, y, label='Points')
plt.plot(x2, yfit, label='Fit')

