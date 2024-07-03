
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Average Temperature': [15.2, 16.3, 18.5, 21.0, 24.7, 27.3, 29.1, 28.4, 26.1, 22.7, 18.9, 16.5]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
chart = sns.lineplot(x='Month', y='Average Temperature', data=df, color="#FF5733")

plt.fill_between(x=df['Month'], y1=df['Average Temperature'], color="#FF5733", alpha=0.3)

for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Average Temperature'][i]+0.5, f"{df['Average Temperature'][i]}°C", horizontalalignment='center')

plt.title('Monthly Average Temperature', fontsize=18, pad=20)
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()