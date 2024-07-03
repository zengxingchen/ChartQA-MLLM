
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Sales': [
        200, 220, 230, 210, 240, 250, 300, 280, 290, 310,
        320, 330, 350, 340, 360, 370, 380, 390, 410, 420,
        430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530
    ]
}

df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(14, 8))
area_chart = sns.lineplot(data=df, x='Date', y='Sales', color="#FF6347")
plt.fill_between(data['Date'], data['Sales'], color="#FFA07A")

# Annotation
for index in range(0, df.shape[0], 3):  # Adding annotations every 3 days for more frequent labels
    date = df.iloc[index]['Date']
    sales = df.iloc[index]['Sales']
    plt.text(date, sales + 10, str(sales), ha='center')

# Customization
plt.title('Daily Sales in January 2023', pad=20)
plt.xlabel('Date')
plt.ylabel('Sales')
sns.despine()

# Show the plot
plt.show()