import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Running': [1, 1.5, 2, 1.2, 2.5, 3, 1.8],
    'Cycling': [2, 2.5, 3, 2.8, 3.5, 4, 2.7],
    'Swimming': [0.5, 1, 1.5, 1.2, 2, 2.5, 1.3],
    'Weightlifting': [1, 1.5, 2, 1.8, 2.5, 3, 1.6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot area chart for Running
ax.fill_between(df['Day'], df['Running'], color='#1f77b4', alpha=0.7, label='Running')

# Annotations
for i, txt in enumerate(df['Running']):
    ax.annotate(txt, (df['Day'][i], df['Running'][i]), textcoords="offset points", xytext=(0, 5), ha='center')

# Chart customization
ax.set_title('Weekly Hours Spent on Running Activities', fontsize=16)
ax.set_xlabel('Day', fontsize=14)
ax.set_ylabel('Hours', fontsize=14)
ax.legend(loc='upper left')

# Show plot
plt.tight_layout()
plt.show()