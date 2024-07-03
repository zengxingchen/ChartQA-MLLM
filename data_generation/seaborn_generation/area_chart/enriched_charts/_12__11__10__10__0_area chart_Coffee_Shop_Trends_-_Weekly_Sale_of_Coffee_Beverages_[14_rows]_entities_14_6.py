
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Hours_Spent_Reading": [20, 22, 25, 28, 30, 32, 35, 33, 29, 26, 24, 21]
})

plt.figure(figsize=(16, 8))

sns.set_theme(style="whitegrid")
ax = sns.lineplot(
    x="Month",
    y="Hours_Spent_Reading",
    data=data,
    color="#2ca02c",
    linewidth=2
)
ax.fill_between(data["Month"], data["Hours_Spent_Reading"], color="#98df8a")

for i in range(data.shape[0]):
    plt.text(data["Month"][i], data["Hours_Spent_Reading"][i] + 1, str(data["Hours_Spent_Reading"][i]) + ' hrs', 
             horizontalalignment='center', size='small', color='black', weight='semibold')

plt.xticks(rotation=45)

ax.set_title('Monthly Hours Spent Reading', fontsize=18, pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Hours Spent', fontsize=14)

plt.tight_layout()
plt.show()