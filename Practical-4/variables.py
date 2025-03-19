# Walk to bus stop: 15 mins
#步行到巴士站： 15 分钟
a = 15
# Bus journey: 1 hr 15 mins = 75 mins
# 巴士旅程：1 小时 15 分钟 = 75 分钟
b = 75
# Total time for bus commute
# 公交车通勤总时间
c = a + b

# Drive: 1 hr 30 mins = 90 mins
#驾驶：1 小时 30 分钟 = 90 分钟
d = 90
# Walk from car park: 5 mins
# 从停车场步行： 5 分钟
e = 5
# Total time for car commute
# 汽车通勤的总时间
f = d + e

# Compare c and f: Which is shorter?
#比较 c 和 f：哪个更短？
# c = 90 mins, f = 95 mins, so walking + bus is quicker
#c=90 分钟，f=95 分钟，所以步行 + 巴士更快
print("Bus commute time:", c, "mins")
print("Car commute time:", f, "mins")
# Section 4.2: Working with Booleans
# 第 4.2 节：使用布尔值

# Initialize boolean variables
#初始化布尔变量
X = True
Y = False

# Create W as the logical AND of X and Y
W = X and Y

# Truth table for W (X and Y):
# X = True, Y = True  -> W = True
# X = True, Y = False -> W = False
# X = False, Y = True -> W = False
# X = False, Y = False -> W = False
print("W =", W)  # Output: False