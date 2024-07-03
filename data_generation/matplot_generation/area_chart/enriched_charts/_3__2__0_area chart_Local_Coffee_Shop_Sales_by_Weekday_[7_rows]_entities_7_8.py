
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-02-01', end='2023-02-28'),
    'Visitor_Count': [
        150, 155, 160, 170, 175, 180, 185, 190, 200, 205,
        210, 220, 225, 230, 235, 240, 250, 255, 260, 270,
        275, 280, 290, 295, 300, 310, 315, 320
    ]
}
df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))

plt.plot(df['Date'], df['Visitor_Count'], color="#3498db")
plt.fill_between(df['Date'], df['Visitor_Count'], color="#3498db", alpha=0.4)

max_visitor_count = df['Visitor_Count'].max()
max_date = df.loc[df['Visitor_Count'].idxmax(), 'Date']
plt.annotate(f'Peak: {max_visitor_count}', xy=(max_date, max_visitor_count),
             xytext=(max_date, max_visitor_count + 10), textcoords='data',
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05),
             horizontalalignment='center', verticalalignment='top')

plt.title('Daily Tourists at Famous Landmark in February 2023', pad=20)
plt.xlabel('Date')
plt.ylabel('Tourist Count')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()