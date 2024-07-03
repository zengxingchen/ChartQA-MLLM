
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Daily_Water_Intake_Liters': [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0],
    'Average_Energy_Level': [4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.2, 7.4, 7.3, 7.1, 6.8, 6.6, 6.3, 6.0, 5.8, 5.6, 5.3, 5.1, 4.9, 4.8, 4.7, 4.6, 4.5, 4.4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
scatter_plot = sns.scatterplot(data=df, x='Daily_Water_Intake_Liters', y='Average_Energy_Level', color="#1E90FF")

# Customize the plot
scatter_plot.set_title('Effect of Daily Water Intake on Energy Levels', fontsize=20, pad=20)
scatter_plot.set(xlabel='Daily Water Intake (Liters)', ylabel='Average Energy Level (1-10)')

plt.show()