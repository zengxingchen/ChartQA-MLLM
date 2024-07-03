
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Hours_of_Exercise': [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12],
    'Hours_of_Sleep': [6.8, 7.0, 7.2, 7.5, 7.8, 8.0, 8.1, 8.3, 8.5, 8.7, 8.8, 9.0, 9.1, 7.0, 7.2, 7.5, 7.3, 7.0, 6.8, 6.5, 6.3, 6.1, 5.9, 5.7]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 6))
scatter_plot = sns.scatterplot(data=df, x='Hours_of_Exercise', y='Hours_of_Sleep', color="#1f77b4")

# Customize the plot
scatter_plot.set_title('Correlation Between Exercise and Sleep Patterns')
scatter_plot.set(xlabel='Average Hours of Exercise per Week', ylabel='Average Hours of Sleep per Night')

plt.show()