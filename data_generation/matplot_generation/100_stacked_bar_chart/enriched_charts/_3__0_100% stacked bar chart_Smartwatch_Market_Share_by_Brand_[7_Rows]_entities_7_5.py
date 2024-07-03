import matplotlib.pyplot as plt
import pandas as pd

# Data preparation
data = {
    'Category': ['2020 Q1', '2020 Q2', '2020 Q3', '2020 Q4', '2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4'],
    'Value A': [15, 20, 25, 10, 30, 25, 20, 25, 30, 25, 20, 30],
    'Value B': [25, 30, 20, 30, 20, 25, 30, 20, 25, 30, 25, 20],
    'Value C': [30, 25, 35, 30, 25, 20, 30, 25, 20, 25, 30, 25],
    'Value D': [30, 25, 20, 30, 25, 30, 20, 30, 25, 20, 25, 25]
}

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)
df_percent = df.div(df.sum(axis=1), axis=0) * 100

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))
df_percent.plot(kind='barh', stacked=True, width=0.7, ax=ax, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

# Customizations
ax.set_title('Quarterly Distribution of Values Over Years', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Category')
ax.legend(loc='lower right', bbox_to_anchor=(1, -0.2), ncol=4)

plt.tight_layout()
plt.show()