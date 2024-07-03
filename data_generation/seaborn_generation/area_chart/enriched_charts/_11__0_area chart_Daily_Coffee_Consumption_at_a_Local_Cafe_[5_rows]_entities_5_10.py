
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Page_Views': [1200, 1400, 1800, 2100, 2500, 3000, 3500, 3400, 2900, 2300, 1700, 1300]
}

df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

plt.figure(figsize=(14, 7))
chart = sns.lineplot(x='Month', y='Page_Views', data=df, color="#e74c3c")
plt.fill_between(x=df['Month'], y1=df['Page_Views'], color="#e74c3c", alpha=0.3)

for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Page_Views'][i] + 100, f"{df['Page_Views'][i]}", horizontalalignment='center')

plt.title('Monthly Page Views')
plt.xlabel('Month')
plt.ylabel('Page Views')

plt.tight_layout()
plt.show()