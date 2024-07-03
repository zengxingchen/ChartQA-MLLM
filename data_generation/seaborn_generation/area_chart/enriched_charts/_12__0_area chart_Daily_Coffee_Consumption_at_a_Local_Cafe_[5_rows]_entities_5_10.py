
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data creation
data = {
    'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6',
             'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12'],
    'Distance (km)': [10.2, 12.5, 15.1, 14.3, 16.8, 18.4, 20.0, 19.5, 21.3, 22.7, 23.8, 25.1]
}

df = pd.DataFrame(data)

# Convert 'Week' from string to categorical to ensure correct order
df['Week'] = pd.Categorical(df['Week'], categories=[
    'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6',
    'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12'], ordered=True)

# Seaborn plot
plt.figure(figsize=(14, 8))
chart = sns.lineplot(x='Week', y='Distance (km)', data=df, color="#1abc9c")

# Filling the area under the line
plt.fill_between(x=df['Week'], y1=df['Distance (km)'], color="#1abc9c", alpha=0.3)

# Annotate
for i in range(df.shape[0]):
    plt.text(df['Week'][i], df['Distance (km)'][i]+0.5, f"{df['Distance (km)'][i]} km", horizontalalignment='center')

plt.title('Average Weekly Running Distance')
plt.xlabel('Week')
plt.ylabel('Distance (km)')

# Show plot
plt.tight_layout()
plt.show()