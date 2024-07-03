
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
                'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'Concert Attendance': [5000, 7000, 8000, 7500, 9000, 11000, 12000, 13000, 15000, 16000, 17000, 18000],
    'Online Streams': [15000, 18000, 20000, 21000, 23000, 25000, 27000, 29000, 31000, 32000, 33000, 34000],
    'Merchandise Sales': [3000, 3500, 4000, 4500, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]
}

df = pd.DataFrame(data)

# Figure and Plot
fig, ax = plt.subplots(figsize=(16, 10))
ax.stackplot(df['Quarter'], df['Concert Attendance'], df['Online Streams'], df['Merchandise Sales'],
             labels=['Concert Attendance', 'Online Streams', 'Merchandise Sales'],
             colors=['#e6194B', '#3cb44b', '#ffe119'])

# Title and labels
plt.title('Quarterly Music Industry Revenue Streams', pad=20)
plt.xlabel('Quarter')
plt.ylabel('Revenue (in Thousands)')

# Annotations
for i, (quarter, concert, streams, merch) in enumerate(zip(df['Quarter'], df['Concert Attendance'], df['Online Streams'], df['Merchandise Sales'])):
    total_revenue = concert + streams + merch
    ax.annotate(f'Total: {total_revenue}', (i, total_revenue), textcoords="offset points", xytext=(0, 10), ha='center')

# Legend
plt.legend(loc='upper right')

# Show plot
plt.tight_layout()
plt.show()