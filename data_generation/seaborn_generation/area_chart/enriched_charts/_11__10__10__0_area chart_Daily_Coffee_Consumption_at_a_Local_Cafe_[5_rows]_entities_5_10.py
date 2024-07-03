
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data creation
data = {
    'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 
             'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12', 'Week 13'],
    'Average_Cycling_Distance': [15, 18, 20, 22, 25, 28, 30, 33, 35, 38, 40, 42, 45]
}

df = pd.DataFrame(data)

# Convert 'Week' from string to categorical to ensure correct order
df['Week'] = pd.Categorical(df['Week'], categories=[
    'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 
    'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12', 'Week 13'], ordered=True)

# Seaborn plot
plt.figure(figsize=(14, 8))
chart = sns.lineplot(x='Week', y='Average_Cycling_Distance', data=df, color="#1f77b4")

# Filling the area under the line
plt.fill_between(x=df['Week'], y1=df['Average_Cycling_Distance'], color="#1f77b4", alpha=0.3)

# Annotate
for i in range(df.shape[0]):
    plt.text(df['Week'][i], df['Average_Cycling_Distance'][i] + 0.5, f"{df['Average_Cycling_Distance'][i]} km", horizontalalignment='center')

plt.title('Weekly Average Cycling Distance', pad=20)
plt.xlabel('Week')
plt.ylabel('Cycling Distance (km)')

# Show plot
plt.tight_layout()
plt.show()