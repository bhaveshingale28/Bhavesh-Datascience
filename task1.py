import numpy as np

scores = np.random.randint(0, 101, 50)

mean = np.mean(scores)
print("Mean:", mean)

median = np.median(scores)
print("Median:", median)

standard_deviation = np.std(scores)
print("Standard Deviation:", standard_deviation)

max_value = np.max(scores)
print("Highest Score:", max_value)

min_value = np.min(scores)
print("Lowest Score:", min_value)

failed = scores[scores < 40]
print("Failed (<40):", failed)

passed = scores[scores > 85]
print("Distinction (>85):", passed)

normalized_scores = (scores - min_value) / (max_value - min_value)
print("Normalized Scores:\n", normalized_scores)

new_arr = scores.reshape(5, 10)
print("Reshaped Array (5x10):\n", new_arr)

row_averages = np.mean(new_arr, axis=1)
print("Row-wise Averages:", row_averages)