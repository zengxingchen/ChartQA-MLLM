
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Italy', 'Brazil', 
                'Canada', 'Russia', 'South Korea', 'Australia', 'Spain', 'Mexico', 'Indonesia', 
                'Netherlands', 'Saudi Arabia', 'Turkey', 'Switzerland', 'Nigeria', 'Argentina', 
                'South Africa', 'Egypt', 'Philippines', 'Vietnam', 'Thailand', 'Colombia', 
                'Malaysia', 'Chile'],
    'AverageMonthlyStreamingHours': [350, 320, 280, 260, 300, 290, 270, 250, 310, 330, 340, 360, 
                                     280, 290, 300, 270, 260, 250, 240, 260, 280, 300, 310, 270, 
                                     320, 280, 270, 300, 260, 270],
    'PercentageOutdoorActivities': [60, 50, 45, 55, 40, 58, 57, 52, 35, 65, 48, 43, 68, 53, 42, 
                                    32, 63, 25, 40, 60, 35, 45, 55, 30, 38, 42, 50, 48, 45, 40]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
sns.scatterplot(data=df, x='AverageMonthlyStreamingHours', y='PercentageOutdoorActivities', 
                palette=['#ff5733', '#33ff57'], 
                s=150)

plt.title('Relationship between Monthly Streaming Hours and Outdoor Activities', fontsize=20, pad=25)
plt.xlabel('Average Monthly Streaming Hours', fontsize=16)
plt.ylabel('Percentage of Population Engaged in Outdoor Activities', fontsize=16)

plt.show()