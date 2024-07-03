
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [65000, 63000, 62000, 61000, 60000, 59000, 58000, 57000, 56000, 55000, 54000, 53000]
}

df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#1f77b4", "#ff7f0e"]

plt.figure(figsize=(14, 7))

sns.lineplot(data=df, x='Month', y='Revenue', color='#1f77b4', marker='o', linewidth=2.5)

plt.text(0, df['Revenue'][0], f"${df['Revenue'][0]:,}", color='black', ha="center")
plt.text(5, df['Revenue'][5], f"${df['Revenue'][5]:,}", color='black', ha="center")
plt.text(11, df['Revenue'][11], f"${df['Revenue'][11]:,}", color='black', ha="center")

plt.title('Monthly Sales Revenue Decline for a Fictional Retail Store in 2023', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Revenue ($)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()