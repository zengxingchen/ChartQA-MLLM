
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
online_sales = [120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340]
in_store_sales = [150, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360]
wholesale_sales = [130, 145, 155, 170, 185, 200, 215, 230, 245, 260, 275, 290]

# Stacked Area Chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(months, online_sales, in_store_sales, wholesale_sales, colors=['#FF9999', '#66B2FF', '#99FF99'])

# Customizing the plot
ax.set_title('Monthly Sales Volume by Channel in 2023', pad=20)
ax.set_ylabel('Sales Volume (Thousands of Units)')
ax.set_xlabel('Month')
ax.margins(0, 0)

# Adding annotation
ax.annotate('Holiday Season Peak', xy=('December', 990), xytext=('November', 1050),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Adding a legend
ax.legend(['Online Sales', 'In-Store Sales', 'Wholesale Sales'], loc='upper left')

# Displaying the plot
plt.show()