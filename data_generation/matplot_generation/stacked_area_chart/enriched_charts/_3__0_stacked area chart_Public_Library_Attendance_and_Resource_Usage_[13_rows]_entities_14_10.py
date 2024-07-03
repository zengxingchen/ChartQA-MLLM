
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 'Jun-2021',
              'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021', 'Nov-2021', 'Dec-2021'],
    'Adventure': [20000, 22000, 21000, 24000, 23000, 25000, 26000, 27000, 28000, 29000, 30000, 31000],
    'Technology': [25000, 26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000, 34000, 35000, 36000],
    'History': [15000, 16000, 15500, 18000, 17500, 19000, 20000, 21000, 22000, 23000, 24000, 25000]
}

df = pd.DataFrame(data)

# Figure and Plot
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(df['Month'], df['Adventure'], df['Technology'], df['History'],
             labels=['Adventure', 'Technology', 'History'],
             colors=['#FF6347', '#4682B4', '#32CD32'])

# Title and labels
plt.title('Monthly Interests in Various Topics', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Interests (in Numbers)', fontsize=12)
plt.legend(loc='upper left')

# Annotations
for i, (month, adventure, technology, history) in enumerate(zip(df['Month'], df['Adventure'], df['Technology'], df['History'])):
    total_interests = adventure + technology + history
    ax.annotate(f'Total: {total_interests}', (month, total_interests), textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.tight_layout()
plt.show()