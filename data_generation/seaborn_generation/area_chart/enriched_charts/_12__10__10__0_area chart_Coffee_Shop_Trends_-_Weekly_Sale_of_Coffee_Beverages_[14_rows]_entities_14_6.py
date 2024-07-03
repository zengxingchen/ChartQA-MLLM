
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Steps_Taken": [8000, 9500, 10500, 11000, 12000, 13000, 12500, 13500, 14000, 15000, 16000, 15500]
})

plt.figure(figsize=(18, 9))

sns.set_theme(style="whitegrid")
ax = sns.lineplot(
    x="Month",
    y="Steps_Taken",
    data=data,
    color="#1f77b4",
    linewidth=2
)
ax.fill_between(data["Month"], data["Steps_Taken"], color="#aec7e8")

for i in range(data.shape[0]):
    plt.text(data["Month"][i], data["Steps_Taken"][i] + 500, str(data["Steps_Taken"][i]) + ' Steps', 
             horizontalalignment='center', size='small', color='black', weight='semibold')

plt.xticks(rotation=45)

ax.set_title('Monthly Steps Taken', fontsize=20, pad=30)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Steps Taken', fontsize=14)

plt.tight_layout()
plt.show()