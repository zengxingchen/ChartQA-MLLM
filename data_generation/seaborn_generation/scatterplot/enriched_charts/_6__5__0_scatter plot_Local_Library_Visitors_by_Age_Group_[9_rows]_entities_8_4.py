
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Average_Time_on_Social_Media_per_Day': [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15],
    'Average_Happiness_Level': [6.2, 6.5, 6.7, 6.9, 7.0, 7.2, 7.3, 7.1, 6.8, 6.5, 6.3, 6.1, 6.0, 5.8, 5.7, 5.5, 5.3, 5.2, 5.1, 5.0, 4.9, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 4.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
scatter_plot = sns.scatterplot(data=df, x='Average_Time_on_Social_Media_per_Day', y='Average_Happiness_Level', color="#2A9D8F")

# Customize the plot
scatter_plot.set_title('Effect of Social Media Usage on Happiness Levels', fontsize=18, pad=20)
scatter_plot.set(xlabel='Average Time on Social Media per Day (hours)', ylabel='Average Happiness Level (1-10)')

plt.show()