
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Daily_Screen_Time': [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12],
    'Mental_Wellbeing_Score': [8.9, 8.8, 8.7, 8.5, 8.3, 8.1, 8.0, 7.8, 7.5, 7.3, 7.0, 6.8, 6.5, 6.3, 6.0, 5.8, 5.5, 5.3, 5.0, 4.8, 4.5, 4.3, 4.0, 3.8]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 5))
scatter_plot = sns.scatterplot(data=df, x='Daily_Screen_Time', y='Mental_Wellbeing_Score', color="#FF5733")

# Customize the plot
scatter_plot.set_title('Correlation Between Screen Time and Mental Well-being')
scatter_plot.set(xlabel='Average Daily Screen Time (hours)', ylabel='Mental Well-being Score')

plt.show()