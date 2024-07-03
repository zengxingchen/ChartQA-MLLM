
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Hours Spent": [8, 7.5, 6, 5, 4.5, 3, 2.5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Area chart
ax.fill_between(df['Day'], df['Hours Spent'], color='#FFA07A', alpha=0.7)

# Titles and labels
ax.set_title('Hours Spent on Physical Activities in a Week', fontsize=16, pad=20)
ax.set_xlabel('Day', fontsize=14)
ax.set_ylabel('Hours Spent', fontsize=14)

# Annotations
for i, txt in enumerate(df['Hours Spent']):
    ax.annotate(txt, (df['Day'][i], df['Hours Spent'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()