
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Nutrient": ["Protein", "Carbohydrates", "Fat", "Fiber", "Sugar", "Calcium", "Iron", "Potassium", "Sodium", "Vitamin C", "Vitamin D", "Vitamin B12"],
    "Average Daily Intake (mg)": [56, 300, 70, 30, 50, 1000, 18, 4700, 2300, 90, 20, 2.4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

# Area chart
ax.fill_between(df['Nutrient'], df['Average Daily Intake (mg)'], color='#66c2a5', alpha=0.7)

# Titles and labels
ax.set_title('Average Daily Intake of Nutrients', fontsize=16, pad=20)
ax.set_xlabel('Nutrient', fontsize=14)
ax.set_ylabel('Average Daily Intake (mg)', fontsize=14)

# Annotations
for i, txt in enumerate(df['Average Daily Intake (mg)']):
    ax.annotate(txt, (df['Nutrient'][i], df['Average Daily Intake (mg)'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()