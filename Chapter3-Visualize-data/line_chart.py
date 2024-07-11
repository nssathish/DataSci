import matplotlib.pyplot as plt

variance = [pow(2, _) for _ in range(0, 9)]
bias_squared = [pow(2, _) for _ in range(8, -1, -1)]

total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
plt.plot(xs, variance, "g-", label="variance")
plt.plot(xs, bias_squared, "r-.", label="bias^2")
plt.plot(xs, total_error, "b:", label="total error")

plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()
