
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Visitors': [100, 150, 200, 180, 220, 210, 230, 250, 240, 260, 280, 300]
}

df = pd.DataFrame(data)

months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

plt.figure(figsize=(14, 8))
plt.plot(df['Month'], df['Visitors'], color='#FF5733', lw=2)
plt.fill_between(df['Month'], df['Visitors'], color='#FF5733', alpha=0.3)

for line in range(0, df.shape[0]):
     plt.text(df.Month[line], df.Visitors[line], df.Visitors[line], 
              horizontalalignment='center', size='small', color='black', weight='semibold')

plt.title('Monthly Visitors to the Art Gallery in 2023', fontsize=18, y=1.03)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Visitors', fontsize=14)
plt.ylim(0, None)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()