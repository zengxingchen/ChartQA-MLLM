
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': ['Japan', 'France', 'Italy', 'Australia', 'Brazil', 'Canada', 'India', 'Germany', 'Mexico', 'UK', 'China', 'USA'],
    'Visitors': [15000, 18000, 14000, 20000, 16000, 17000, 19000, 21000, 15000, 18000, 22000, 25000]
}
df = pd.DataFrame(data)
df['Country'] = pd.Categorical(df['Country'], categories=data['Country'], ordered=True)

plt.figure(figsize=(16, 12))
plt.fill_between(x=df['Country'], y1=df['Visitors'], color='#4CAF50', alpha=0.7)
plt.plot(df['Country'], df['Visitors'], color='#1B5E20', lw=2)

for i in range(df.shape[0]):
    plt.text(df['Country'][i], df['Visitors'][i] + 500, str(df['Visitors'][i]), horizontalalignment='center')

plt.xlabel('Country')
plt.ylabel('Number of Visitors')
plt.title('Top Travel Destinations and Visitor Count in 2023', fontsize=18)
plt.xticks(rotation=45)
plt.show()