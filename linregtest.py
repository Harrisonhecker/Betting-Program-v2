import numpy as np
from sklearn.linear_model import LinearRegression

#x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
#y = np.array([5, 20, 14, 32, 22, 38])

x = np.array([1.80, -2.74, 8.88, 4.45, 13.13, 10.05, -14.06, -4.80, -8.68, 14.62, -2.71, 13.28, 0.14, 4.61, -3.05, 8.11, 1.56, -3.05, 0.49, 6.23, 6.74, 7.44, 11.14, 14.67, 6.23, 8.11, 6.74, 11.14, 7.44, 4.61]).reshape((-1, 1))
y = np.array([83, 79, 67, 70, 63, 78, 99, 111, 77, 82, 71, 72, 80, 66, 83, 76, 66, 74, 79, 63, 73, 80, 83, 59, 70, 76, 81, 75, 71, 84])

model = LinearRegression()

model.fit(x, y)

r_sq = model.score(x,y)

print("coefficient of determination: " + str(r_sq) + "\n")

print("intercept: " + str(model.intercept_))
print("slope: " + str(model.coef_) + "\n")

y_pred = model.predict(x)
print("predicted response: " + str(y_pred) + "\n")

y_pred = model.intercept_ + model.coef_ * x
print("predicted response: " + str(y_pred) + "\n")

#x_new = np.arange(5).reshape((-1, 1))
x_new = np.array([14.67]).reshape((-1,1))
y_new = model.predict(x_new)
print("predicted response (new): " + str(y_new) + "\n")

