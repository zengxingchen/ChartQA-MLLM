
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': ['Japan', 'Switzerland', 'Spain', 'Italy', 'Australia', 'Sweden', 
                'Canada', 'Norway', 'Netherlands', 'France', 'Germany', 'United States'],
    'GDP_Growth_Rate_Percentage': [1.5, 1.8, 2.1, 1.2, 2.3, 1.9, 2.0, 1.7, 1.6, 1.4, 1.3, 2.2]
}

df = pd.DataFrame(data)
df = df.sort_values('GDP_Growth_Rate_Percentage')

f, ax = plt.subplots(figsize=(14, 8))

sns.barplot(
    y="Country", 
    x="GDP_Growth_Rate_Percentage", 
    data=df,
    palette=['#3498db', '#9b59b6', '#2ecc71', '#f1c40f', '#e74c3c', '#e67e22', 
             '#1abc9c', '#34495e', '#7f8c8d', '#2980b9', '#d35400', '#8e44ad'],
    edgecolor=".2",
    linewidth=1.5
)

sns.set_context("poster", font_scale=0.8)
ax.bar_label(ax.containers[0], label_type='edge')

ax.set_xlim(0, 3)
ax.set_xlabel('GDP Growth Rate (%)')
ax.set_ylabel('Country')
ax.set_title('Average GDP Growth Rate in Different Countries', pad=20)

plt.tight_layout()
plt.show()