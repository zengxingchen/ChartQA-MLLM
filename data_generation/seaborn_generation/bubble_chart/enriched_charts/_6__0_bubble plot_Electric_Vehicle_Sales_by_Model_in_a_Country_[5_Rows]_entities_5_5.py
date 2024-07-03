
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Country': ['United States', 'China', 'Germany', 'India', 'France', 'United Kingdom', 
                'Canada', 'South Korea', 'Australia', 'Japan', 'Brazil', 'Italy'],
    'Budget (Million USD)': [200, 150, 100, 50, 75, 60, 40, 30, 20, 90, 35, 25],
    'Revenue (Million USD)': [800, 500, 300, 150, 250, 220, 180, 120, 90, 350, 140, 100],
    'Rating': [85, 80, 75, 70, 78, 77, 72, 69, 65, 82, 68, 66]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df, 
                               x='Revenue (Million USD)', 
                               y='Budget (Million USD)', 
                               size='Rating', 
                               hue='Country', 
                               palette=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", 
                                        "#c2c2f0", "#ffb3e6", "#c4e17f", "#ff6666",
                                        "#ffb366", "#99c2a2", "#c2f0c2", "#b3b3cc"],
                               sizes=(50, 2000))

plt.title('Film Industry: Budget vs Revenue and Rating', pad=20)
plt.xlabel('Revenue (Million USD)')
plt.ylabel('Budget (Million USD)')

bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Country')

plt.show()