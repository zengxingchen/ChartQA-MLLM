
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Exercise_Hours': [5, 7, 10, 15, 20, 25, 22, 18, 14, 10, 6, 4]
}

df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

plt.figure(figsize=(16, 8))
chart = sns.lineplot(x='Month', y='Exercise_Hours', data=df, color="#3498db")
plt.fill_between(x=df['Month'], y1=df['Exercise_Hours'], color="#3498db", alpha=0.3)

for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Exercise_Hours'][i] + 0.5, f"{df['Exercise_Hours'][i]}", horizontalalignment='center')

plt.title('Monthly Exercise Hours')
plt.xlabel('Month')
plt.ylabel('Exercise Hours')

plt.tight_layout()
plt.show()