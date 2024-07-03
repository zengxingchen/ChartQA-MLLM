import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Sales': [
        100, 150, 130, 180, 200, 170, 210, 220, 190, 230,
        240, 250, 260, 280, 300, 310, 330, 340, 350, 370,
        380, 390, 400, 420, 430, 450, 460, 480, 490, 500, 520
    ]
}

df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(16, 10))
area_chart = sns.lineplot(data=df, x='Date', y='Sales', color="#4682B4")
plt.fill_between(data['Date'], data['Sales'], color="#87CEFA")

# Annotation
for index in range(0, df.shape[0], 5):
    date = df.iloc[index]['Date']
    sales = df.iloc[index]['Sales']
    plt.text(date, sales + 10, str(sales), ha='center')

# Customization
plt.title('Daily Sales in January 2023', pad=20)
plt.xlabel('Date')
plt.ylabel('Sales (Units)')
sns.despine()

# Show the plot
plt.show()