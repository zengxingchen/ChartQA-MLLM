
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# The generated data would be a full year's worth of daily sales data
data = {
    'Date': pd.date_range(start='2023-01-01', end='2023-12-31'),
    'Sales': [100 + i * 0.5 for i in range(365)]  # Hypothetical sales data
}
sales_data = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the area plot
plt.figure(figsize=(12, 6))
area_chart = sns.lineplot(data=sales_data, x='Date', y='Sales', color='#1f77b4')
plt.fill_between(sales_data['Date'], sales_data['Sales'], alpha=0.3, color='#1f77b4')

# Annotate a specific event
peak_sales_date = sales_data.loc[sales_data['Sales'].idxmax(), 'Date']
peak_sales_value = sales_data['Sales'].max()
plt.text(peak_sales_date, peak_sales_value, 'Peak Sales', horizontalalignment='left', size='medium', color='black')

# Customize the plot with titles and labels
plt.title('Daily Sales Trend of ABC Company - 2023')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()