
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature_Change': [1.2, 1.5, 1.8, 2.0, 2.3, 2.5, 2.8, 2.6, 2.4, 2.1, 1.9, 1.6]
}

df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

colors = ["#4daf4a", "#377eb8", "#e41a1c", "#984ea3", "#ff7f00", "#ffff33", "#a65628", "#f781bf", "#999999", "#66c2a5", "#fc8d62", "#8da0cb"]

plt.figure(figsize=(16, 9))

sns.lineplot(data=df, x='Month', y='Temperature_Change', color='#4daf4a', marker='o', linewidth=2.5)

plt.text(0, df['Temperature_Change'][0], f"{df['Temperature_Change'][0]}", color='black', ha="center")
plt.text(5, df['Temperature_Change'][5], f"{df['Temperature_Change'][5]}", color='black', ha="center")
plt.text(11, df['Temperature_Change'][11], f"{df['Temperature_Change'][11]}", color='black', ha="center")

plt.title('Monthly Temperature Change in 2023', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Temperature Change (°C)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()