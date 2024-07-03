
import matplotlib.pyplot as plt
import numpy as np

# Generated data points representing the age distribution of a hypothetical population
ages = np.concatenate((np.repeat(np.arange(1, 21), np.random.randint(30, 60, 20)),
                       np.repeat(np.arange(21, 40), np.random.randint(20, 50, 19)),
                       np.repeat(np.arange(40, 60), np.random.randint(10, 40, 20)),
                       np.repeat(np.arange(60, 80), np.random.randint(5, 30, 20)),
                       np.repeat(np.arange(80, 101), np.random.randint(1, 20, 21))))

# Plotting the histogram
plt.figure(figsize=(12, 8))
plt.hist(ages, bins=50, orientation='horizontal', color='#1D8348', rwidth=0.8)

# Customizing the plot
plt.title('Age Distribution of a Hypothetical Population')
plt.xlabel('Number of Individuals')
plt.ylabel('Age')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Showing the plot
plt.show()