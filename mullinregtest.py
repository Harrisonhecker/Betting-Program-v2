import numpy as np
from sklearn.linear_model import LinearRegression

#x = [
 # [0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]
#]
#y = [4, 5, 20, 14, 32, 22, 38, 43]


# our team offensive rating, defensive rating, rebound differential, 3 point percentage, field goal percentage, 3 point attempts, field goal attempts
x = [
    [128.2, 74.6, 20.0, 0.476, 0.557, 21, 21], 
    [120.6, 82.4, 19.0, 0.267, 0.517, 15, 18], 
    [86.7, 57.3, 19.0, 0.286, 0.404, 28, 18], 
    [105.5, 120.5, -5.0, 0.318, 0.424, 22, 15], 
    [130.6, 85.5, 11.0, 0.3, 0.469, 20, 18], 
    [129.0, 117.7, -1.0, 0.4, 0.519, 20, 18], 
    [102.9, 115.7, -2.0, 0.231, 0.473, 13, 22], 
    [143.3, 88.1, 23.0, 0.565, 0.5, 23, 18], 
    [101.5, 100.0, 6.0, 0.421, 0.464, 19, 12], 
    [101.2, 107.2, -8.0, 0.375, 0.459, 24, 14], 
    [135.7, 87.1, 18.0, 0.421, 0.612, 19, 7], 
    [123.3, 80.8, 11.0, 0.36, 0.525, 25, 29], 
    [104.3, 81.4, 8.0, 0.4, 0.464, 15, 20], 
    [111.3, 114.5, -6.0, 0.429, 0.5, 14, 7], 
    [107.4, 117.6, -13.0, 0.474, 0.436, 19, 19], 
    [98.5, 102.9, 1.0, 0.462, 0.375, 13, 15], 
    [87.7, 93.2, 4.0, 0.381, 0.343, 21, 12], 
    [82.2, 86.3, -1.0, 0.294, 0.357, 17, 23], 
    [127.4, 105.5, 8.0, 0.5, 0.563, 16, 17], 
    [90.9, 104.5, -18.0, 0.4, 0.367, 10, 20], 
    [104.5, 128.4, -6.0, 0.263, 0.441, 19, 19], 
    [87.0, 94.2, 17.0, 0.286, 0.429, 14, 13], 
    [103.0, 114.9, 0.0, 0.313, 0.406, 16, 17], 
    [100.0, 109.5, 14.0, 0.071, 0.5, 14, 22], 
    [69.5, 105.1, -7.0, 0.207, 0.283, 29, 2], 
    [111.9, 137.3, -6.0, 0.533, 0.571, 15, 11], 
    [83.3, 124.2, -24.0, 0.263, 0.4, 19, 11], 
    [124.6, 131.6, 6.0, 0.348, 0.46, 23, 6],
    [104.3, 87.0, 9.0, 0.214, 0.536, 14, 10],
    [121.7, 103.3, 10.0, 0.357, 0.48, 14, 20],
    [120.0, 129.2, 1.0, 0.44, 0.483, 25, 12], 
    [98.5, 86.4, 4.0, 0.462, 0.523, 13, 20]  
]
# opponent points scored
y = [53, 56, 43, 88, 53, 73, 81, 59, 66, 89, 61, 59, 57, 71, 80, 70, 68, 63, 77, 69, 86, 65, 77, 69, 62, 92, 82, 75, 60, 62, 84, 57]

# osu points scored
#y = [91, 82, 65, 77, 81, 80, 72, 96, 67, 84, 95, 90, 73, 69, 73, 67, 64, 60, 93, 60, 70, 60, 69, 63, 41, 75, 55, 71, 72, 73, 78, 65]
x, y = np.array(x), np.array(y)


model = LinearRegression()
model.fit(x,y)

r_sq = model.score(x,y)

print("coefficient of determination: " + str(r_sq) + "\n")

print("intercept: " + str(model.intercept_))
print("slope: " + str(model.coef_) + "\n")

y_pred = model.predict(x)
print("predicted response: " + str(y_pred) + "\n")

y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)
#print("predicted response: " + str(y_pred) + "\n")

#x_new = np.arange(10).reshape((-1, 2))
x_new = np.array([
                  [109.1, 103.3, 3.5, .360, .463, 18.4, 15.8]
                  ]).reshape((-1, 7))
y_new = model.predict(x_new)
print("predicted response (new): " + str(y_new) + "\n")