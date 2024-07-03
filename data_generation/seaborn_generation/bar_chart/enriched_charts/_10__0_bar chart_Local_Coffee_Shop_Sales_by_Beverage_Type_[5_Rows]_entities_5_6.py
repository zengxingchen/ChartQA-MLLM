
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': [
        'United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
        'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea',
        'Spain', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia',
        'Turkey', 'Switzerland'
    ],
    'Life_Expectancy': [
        78.9, 76.4, 84.5, 81.1, 69.4, 81.2, 82.4, 75.9, 83.2, 82.2, 72.6, 82.7,
        83.6, 82.9, 75.0, 71.7, 81.6, 75.3, 75.9, 83.7
    ]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(14, 8))

ax = sns.barplot(
    x="Country",
    y="Life_Expectancy",
    data=df,
    palette=[
        '#3498db', '#e74c3c', '#2ecc71', '#f1c40f', '#8e44ad', '#d35400',
        '#1abc9c', '#2c3e50', '#f39c12', '#7f8c8d', '#c0392b', '#bdc3c7',
        '#16a085', '#2980b9', '#9b59b6', '#34495e', '#27ae60', '#95a5a6',
        '#ecf0f1', '#55efc4'
    ]
)

ax.bar_label(ax.containers[0], fmt='%.1f', label_type='edge', padding=3)

ax.set(title='Life Expectancy by Country in 2023', xlabel='Country', ylabel='Life Expectancy (Years)')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

plt.show()