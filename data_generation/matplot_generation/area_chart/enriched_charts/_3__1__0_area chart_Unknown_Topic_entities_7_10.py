
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Calories_Burned': [300, 400, 450, 350, 500, 600, 550]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(14, 9))

# Plot area chart for Calories Burned
ax.fill_between(df['Day'], df['Calories_Burned'], color='#ff5733', alpha=0.7, label='Calories Burned')

# Annotations
for i, txt in enumerate(df['Calories_Burned']):
    ax.annotate(txt, (df['Day'][i], df['Calories_Burned'][i]), textcoords="offset points", xytext=(0, 5), ha='center')

# Chart customization
ax.set_title('Weekly Calories Burned from Exercise', fontsize=18)
ax.set_xlabel('Day', fontsize=14)
ax.set_ylabel('Calories', fontsize=14)
ax.legend(loc='upper right')

# Show plot
plt.tight_layout()
plt.show()