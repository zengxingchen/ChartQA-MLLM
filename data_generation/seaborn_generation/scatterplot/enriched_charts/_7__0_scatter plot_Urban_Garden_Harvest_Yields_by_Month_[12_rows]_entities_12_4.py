
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame from the provided data
data = {
    'AthleteID': range(1, 51),
    'TrainingHours': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0],
    'PerformanceScore': [55, 58, 61, 65, 68, 70, 73, 75, 77, 79, 82, 84, 85, 87, 88, 89, 91, 92, 94, 95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]
}

df = pd.DataFrame(data)

# Setting the figure size for the scatterplot
plt.figure(figsize=(14, 8))

# Plotting the scatterplot with a specific color scheme
sns.scatterplot(x='TrainingHours', y='PerformanceScore', data=df, color='#1f77b4')

# Set the chart title and labels
plt.title('Impact of Training Hours on Athlete Performance', fontsize=16, pad=20)
plt.xlabel('Training Hours', fontsize=14)
plt.ylabel('Performance Score', fontsize=14)

# Display the scatterplot
plt.show()