
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Attendees': [120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340],
    'Speakers': [15, 18, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42],
    'Workshops': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    'Exhibitors': [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

cumulative = df.cumsum(axis=1)

plt.figure(figsize=(14, 10))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']
plt.stackplot(cumulative.index, cumulative['Attendees'], cumulative['Speakers'],
              cumulative['Workshops'], cumulative['Exhibitors'], labels=cumulative.columns, colors=colors)
plt.legend(loc='upper right')
plt.title('Annual Conference Metrics by Month', fontsize=18, pad=20)
plt.xlabel('Month')
plt.ylabel('Count')

plt.annotate('Peak Attendees', xy=(11, cumulative.loc['December', 'Attendees']),
             xytext=(11, cumulative.loc['December', 'Attendees'] + 50),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak Speakers', xy=(11, cumulative.loc['December', 'Speakers']),
             xytext=(11, cumulative.loc['December', 'Speakers'] + cumulative.loc['December', 'Attendees'] + 50),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak Workshops', xy=(11, cumulative.loc['December', 'Workshops']),
             xytext=(11, cumulative.loc['December', 'Workshops'] + cumulative.loc['December', 'Speakers'] + cumulative.loc['December', 'Attendees'] + 50),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))

plt.tight_layout()
plt.show()