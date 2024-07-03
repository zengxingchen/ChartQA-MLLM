
import matplotlib.pyplot as plt
import numpy as np

# Generated data points representing the score distribution of a hypothetical test
scores = np.concatenate((
    np.repeat(np.arange(24, 50), np.random.randint(30, 60, 26)),
    np.repeat(np.arange(50, 75), np.random.randint(20, 50, 25)),
    np.repeat(np.arange(75, 101), np.random.randint(10, 40, 26))
))

# Plotting the histogram
plt.figure(figsize=(10, 15))
plt.hist(scores, bins=30, orientation='vertical', color='#FF5733', rwidth=0.85)

# Customizing the plot
plt.title('Score Distribution of a Hypothetical Test')
plt.ylabel('Number of Students')
plt.xlabel('Test Scores')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Showing the plot
plt.show()