
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Visitors": [450, 900, 1300, 1700, 2500, 2800, 3300, 3100, 2600, 2200, 1400, 800]
})

plt.figure(figsize=(16, 8))

sns.set_theme(style="whitegrid")
ax = sns.lineplot(
    x="Month",
    y="Visitors",
    data=data,
    color="#2ca02c",
    linewidth=2
)
ax.fill_between(data["Month"], data["Visitors"], color="#98df8a")

for i in range(data.shape[0]):
    plt.text(data["Month"][i], data["Visitors"][i] + 50, str(data["Visitors"][i]), 
             horizontalalignment='center', size='small', color='black', weight='semibold')

plt.xticks(rotation=45)

ax.set_title('Monthly Visitors to a National Museum', fontsize=16, pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Number of Visitors', fontsize=12)

plt.tight_layout()
plt.show()