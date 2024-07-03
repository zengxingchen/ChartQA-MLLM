
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data creation
data = {
    'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 
             'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12', 'Week 13'],
    'Weekly_Hiking_Distance': [5, 8, 12, 15, 18, 20, 22, 25, 28, 30, 33, 35, 38]
}

df = pd.DataFrame(data)

# Convert 'Week' from string to categorical to ensure correct order
df['Week'] = pd.Categorical(df['Week'], categories=[
    'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 
    'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12', 'Week 13'], ordered=True)

# Seaborn plot
plt.figure(figsize=(16, 10))
chart = sns.lineplot(x='Week', y='Weekly_Hiking_Distance', data=df, color="#ff5733")

# Filling the area under the line
plt.fill_between(x=df['Week'], y1=df['Weekly_Hiking_Distance'], color="#ff5733", alpha=0.3)

# Annotate
for i in range(df.shape[0]):
    plt.text(df['Week'][i], df['Weekly_Hiking_Distance'][i] + 0.5, f"{df['Weekly_Hiking_Distance'][i]} km", horizontalalignment='center')

plt.title('Weekly Hiking Distance', pad=20)
plt.xlabel('Week')
plt.ylabel('Hiking Distance (km)')

# Show plot
plt.tight_layout()
plt.show()