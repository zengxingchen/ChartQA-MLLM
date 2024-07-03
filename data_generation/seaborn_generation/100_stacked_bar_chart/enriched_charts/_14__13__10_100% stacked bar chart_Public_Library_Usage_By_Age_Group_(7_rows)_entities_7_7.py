
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Destination': 'Startup A', 'Public Speaking': 30, 'Debating': 25, 'Networking': 15, 'Entrepreneurship': 20, 'Project Management': 10},
    {'Destination': 'Startup B', 'Public Speaking': 25, 'Debating': 20, 'Networking': 20, 'Entrepreneurship': 25, 'Project Management': 10},
    {'Destination': 'Startup C', 'Public Speaking': 20, 'Debating': 30, 'Networking': 10, 'Entrepreneurship': 30, 'Project Management': 10},
    {'Destination': 'Startup D', 'Public Speaking': 15, 'Debating': 15, 'Networking': 25, 'Entrepreneurship': 20, 'Project Management': 25},
    {'Destination': 'Startup E', 'Public Speaking': 30, 'Debating': 20, 'Networking': 20, 'Entrepreneurship': 15, 'Project Management': 15},
    {'Destination': 'Startup F', 'Public Speaking': 20, 'Debating': 25, 'Networking': 15, 'Entrepreneurship': 25, 'Project Management': 15},
    {'Destination': 'Startup G', 'Public Speaking': 25, 'Debating': 20, 'Networking': 25, 'Entrepreneurship': 15, 'Project Management': 15}
]

df = pd.DataFrame(data)
df = df.set_index('Destination')

cumulative_sum = df.cumsum(axis=1)

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD']

fig, ax = plt.subplots(figsize=(12, 8))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.6)
    bottom = cumulative_sum[column]

ax.legend(title='Skills', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Startup')
ax.set_title('Skills Distribution in Startup Founders')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()