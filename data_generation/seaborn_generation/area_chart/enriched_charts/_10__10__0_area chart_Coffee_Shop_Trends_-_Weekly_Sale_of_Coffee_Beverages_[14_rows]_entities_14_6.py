
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Books_Sold": [200, 300, 450, 600, 750, 900, 1100, 1050, 950, 850, 650, 500]
})

plt.figure(figsize=(16, 8))

sns.set_theme(style="whitegrid")
ax = sns.lineplot(
    x="Month",
    y="Books_Sold",
    data=data,
    color="#2ca02c",
    linewidth=2
)
ax.fill_between(data["Month"], data["Books_Sold"], color="#98df8a")

for i in range(data.shape[0]):
    plt.text(data["Month"][i], data["Books_Sold"][i] + 30, str(data["Books_Sold"][i]) + ' Books', 
             horizontalalignment='center', size='small', color='black', weight='semibold')

plt.xticks(rotation=45)

ax.set_title('Monthly Books Sold', fontsize=16, pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Books Sold', fontsize=12)

plt.tight_layout()
plt.show()