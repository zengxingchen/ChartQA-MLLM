
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Hours_of_Reading': [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12],
    'Hours_of_Study': [1.5, 2.0, 2.4, 2.9, 3.3, 3.6, 3.9, 4.1, 4.3, 4.5, 4.7, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))
scatter_plot = sns.scatterplot(data=df, x='Hours_of_Reading', y='Hours_of_Study', color="#2ca02c")

# Customize the plot
scatter_plot.set_title('Correlation Between Reading and Study Patterns')
scatter_plot.set(xlabel='Average Hours of Reading per Week', ylabel='Average Hours of Study per Week')

plt.show()