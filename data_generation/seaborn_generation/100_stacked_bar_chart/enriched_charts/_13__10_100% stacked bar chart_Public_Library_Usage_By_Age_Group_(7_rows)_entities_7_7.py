
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Destination': 'University A', 'Public Speaking': 25, 'Debating': 20, 'Critical Thinking': 30, 'Ethics': 15, 'Philosophical Inquiry': 10},
    {'Destination': 'University B', 'Public Speaking': 20, 'Debating': 25, 'Critical Thinking': 25, 'Ethics': 20, 'Philosophical Inquiry': 10},
    {'Destination': 'University C', 'Public Speaking': 15, 'Debating': 25, 'Critical Thinking': 20, 'Ethics': 25, 'Philosophical Inquiry': 15},
    {'Destination': 'University D', 'Public Speaking': 30, 'Debating': 15, 'Critical Thinking': 20, 'Ethics': 25, 'Philosophical Inquiry': 10},
    {'Destination': 'University E', 'Public Speaking': 20, 'Debating': 20, 'Critical Thinking': 25, 'Ethics': 20, 'Philosophical Inquiry': 15},
    {'Destination': 'University F', 'Public Speaking': 25, 'Debating': 15, 'Critical Thinking': 20, 'Ethics': 15, 'Philosophical Inquiry': 25},
    {'Destination': 'University G', 'Public Speaking': 20, 'Debating': 20, 'Critical Thinking': 15, 'Ethics': 30, 'Philosophical Inquiry': 15}
]

df = pd.DataFrame(data)
df = df.set_index('Destination')

cumulative_sum = df.cumsum(axis=1)

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A1FF33']

fig, ax = plt.subplots(figsize=(10, 6))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.5)
    bottom = cumulative_sum[column]

ax.legend(title='Skills', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('University')
ax.set_title('Distribution of Skills in Philosophy & Ethics by University')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()