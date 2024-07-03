
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Hours_of_Exercise': [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15],
    'Hours_of_Sleep': [6.5, 6.7, 6.9, 7.0, 7.2, 7.3, 7.5, 7.6, 7.8, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 9))
scatter_plot = sns.scatterplot(data=df, x='Hours_of_Exercise', y='Hours_of_Sleep', color="#1f77b4")

# Customize the plot
scatter_plot.set_title('Correlation Between Exercise and Sleep Patterns', fontsize=15)
scatter_plot.set(xlabel='Average Hours of Exercise per Week', ylabel='Average Hours of Sleep per Night')

plt.show()