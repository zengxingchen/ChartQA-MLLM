import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Category": ["R&D", "Marketing", "Operations", "Sales", "Customer Service", "IT", "HR", "Finance", "Administration", "Legal", "Logistics", "Procurement"],
    "Expenditure (Billion USD)": [450, 380, 520, 310, 230, 150, 120, 200, 100, 90, 250, 140]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(14, 9))

# Area chart
ax.fill_between(df['Category'], df['Expenditure (Billion USD)'], color='#4daf4a', alpha=0.7)

# Titles and labels
ax.set_title('Annual Expenditure by Department', fontsize=18, pad=25)
ax.set_xlabel('Department', fontsize=15)
ax.set_ylabel('Expenditure (Billion USD)', fontsize=15)

# Annotations
for i, txt in enumerate(df['Expenditure (Billion USD)']):
    ax.annotate(txt, (df['Category'][i], df['Expenditure (Billion USD)'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()