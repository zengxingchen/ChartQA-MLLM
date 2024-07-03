
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    'Country': ['USA', 'Canada', 'UK', 'Australia', 'Germany', 'France', 'Japan', 'South Korea', 'India', 'Brazil'],
    'AverageSleepHours': [6.8, 7.2, 7.0, 7.4, 6.9, 7.1, 6.5, 6.4, 6.7, 7.3],
    'StressLevel': [7.5, 5.6, 6.1, 4.8, 6.9, 5.4, 7.8, 7.6, 6.5, 5.9],
    'PhysicalActivity': [2.5, 3.4, 2.8, 3.6, 3.0, 2.7, 2.2, 2.1, 2.9, 3.1]
}
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 10))

# Create the bubble chart
bubble = sns.scatterplot(data=df, x='AverageSleepHours', y='StressLevel', size='PhysicalActivity', 
                         hue='Country', palette=['#FF6347', '#4682B4', '#32CD32', '#FFD700', 
                                                 '#8A2BE2', '#FF69B4', '#00CED1', '#FF4500',
                                                 '#2E8B57', '#8B4513'],
                         sizes=(100, 2000), alpha=0.7, edgecolor='w', linewidth=1)
bubble.set_title('Average Sleep Hours vs Stress Levels in Different Countries', weight='bold', size=18)
bubble.set_xlabel('Average Sleep Hours', weight='bold', size=14)
bubble.set_ylabel('Stress Level (1-10)', weight='bold', size=14)

# Adjust legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Show the plot
plt.show()