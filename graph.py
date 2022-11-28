import matplotlib.pyplot as plt
# y axis values
date = [0.002, 0.005, 0.27, 0.3, 0.5, 0.9, 1.3]
uptime = [0.003, 0.0112, 0.0376, 0.11, 0.189, 0.3435, 0.94]
free = [0.0143, 0.002, 0.04, 0.09, 0.25, 0.53, 1.2]
netstat = [0.005, 0.0149, 0.0267, 0.0386, 0.0556, 0.06, 0.3188]
w = [0.0126, 0.032, 0.09, 0.19, 0.4, 0.75, 1.99]
ps = [0.0066, 0.02, 0.07, 0.15, 0.3, 0.38, 2.18]
# corresponding y axis values
x = [1, 5, 10, 15, 20, 25, 100]

# plotting the points 
# plt.plot(x, date, color='green', linestyle='dashed', linewidth=2, marker='o', markerfacecolor='pink', markersize=8)
# plt.plot(x, uptime, color='blue', linestyle='dashed', linewidth=2, marker='o', markerfacecolor='pink', markersize=8)
# plt.plot(x, free, color='yellow', linestyle='dashed', linewidth=2, marker='o', markerfacecolor='pink', markersize=8)
# plt.plot(x, netstat, color='red', linestyle='dashed', linewidth=2, marker='o', markerfacecolor='pink', markersize=8)
# plt.plot(x, w, color='orange', linestyle='dashed', linewidth=2, marker='o', markerfacecolor='pink', markersize=8)
plt.plot(x, ps, color='purple', linestyle='dashed', linewidth=2, marker='o', markerfacecolor='pink', markersize=8)

# setting x and y axis range
# plt.ylim(0, 2.4)
# plt.xlim(0, 110)

# naming the x axis
plt.xlabel('itearations')
# naming the y axis
plt.ylabel('time taken (s)')

# show a legend
# plt.legend()

# giving a title to my graph
plt.title('ps')
# function to show the plot
plt.show()
