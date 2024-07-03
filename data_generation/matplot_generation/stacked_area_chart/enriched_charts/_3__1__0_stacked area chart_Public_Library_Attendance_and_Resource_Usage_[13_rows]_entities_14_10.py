
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['Jan-2023', 'Feb-2023', 'Mar-2023', 'Apr-2023', 'May-2023', 'Jun-2023', 'Jul-2023', 'Aug-2023', 'Sep-2023', 'Oct-2023', 'Nov-2023', 'Dec-2023'],
    'In-Store Sales': [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000],
    'Online Sales': [12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000],
    'Wholesale': [8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500]
}

df = pd.DataFrame(data)

# Figure and Plot
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(df['Month'], df['In-Store Sales'], df['Online Sales'], df['Wholesale'],
             labels=['In-Store Sales', 'Online Sales', 'Wholesale'],
             colors=['#FF5733', '#33FF57', '#3357FF'])

# Title and labels
plt.title('Monthly Sales Distribution for 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales (in USD)')
plt.legend(loc='upper left')

# Annotations
for i, (month, in_store, online, wholesale) in enumerate(zip(df['Month'], df['In-Store Sales'], df['Online Sales'], df['Wholesale'])):
    total_sales = in_store + online + wholesale
    ax.annotate(f'Total: {total_sales}', (i, total_sales), textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.tight_layout()
plt.show()