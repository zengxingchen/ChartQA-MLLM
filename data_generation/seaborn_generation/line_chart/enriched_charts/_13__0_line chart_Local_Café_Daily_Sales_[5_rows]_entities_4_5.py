
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Calories_Burned': [250, 300, 270, 310, 280, 330, 290, 340, 320, 370, 360, 400]
}

df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#1f77b4", "#ff7f0e"]

plt.figure(figsize=(14, 8))

sns.lineplot(data=df, x='Month', y='Calories_Burned', palette=colors, marker='o', linewidth=2.5)

plt.text(0, df['Calories_Burned'][0], f"{df['Calories_Burned'][0]}", color='black', ha="center")
plt.text(5, df['Calories_Burned'][5], f"{df['Calories_Burned'][5]}", color='black', ha="center")
plt.text(11, df['Calories_Burned'][11], f"{df['Calories_Burned'][11]}", color='black', ha="center")

plt.title('Monthly Calories Burned in Fitness Activities in 2023', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Calories Burned', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()