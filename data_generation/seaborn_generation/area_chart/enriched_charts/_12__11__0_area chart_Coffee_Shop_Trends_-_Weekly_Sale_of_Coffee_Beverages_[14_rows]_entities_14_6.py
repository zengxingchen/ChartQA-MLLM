
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Book_Sales": [150, 180, 170, 190, 210, 230, 220]
})

plt.figure(figsize=(12, 6))

sns.set_theme(style="whitegrid")
ax = sns.lineplot(
    x="Day",
    y="Book_Sales",
    data=data,
    color="#2ca02c",
    linewidth=2
)
ax.fill_between(data["Day"], data["Book_Sales"], color="#98df8a")

for i in range(data.shape[0]):
    plt.text(data["Day"][i], data["Book_Sales"][i] + 5, str(data["Book_Sales"][i]) + ' copies', 
             horizontalalignment='center', size='small', color='black', weight='semibold')

plt.xticks(rotation=0)

ax.set_title('Weekly Book Sales', fontsize=18, pad=20)
ax.set_xlabel('Day', fontsize=14)
ax.set_ylabel('Book Sales (copies)', fontsize=14)

plt.tight_layout()
plt.show()