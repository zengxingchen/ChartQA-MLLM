
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data points
data = {
    'Day': list(range(1, 31)),
    'Sales': [200, 220, 230, 250, 240, 260, 270, 300, 320, 310,
              350, 360, 370, 390, 400, 420, 430, 410, 450, 470,
              480, 500, 490, 510, 530, 550, 560, 580, 590, 600]
}
df = pd.DataFrame(data)

# Define the color palette as specific color codes
color = "#2E8B57"

# Set the figure size for width and height
plt.figure(figsize=(16, 8))

# Create an area plot
plt.plot(df['Day'], df['Sales'], color=color, linewidth=2)
plt.fill_between(df['Day'], df['Sales'], color=color, alpha=0.3)

# Annotating the highest sales on the chart
max_sales_day = df['Sales'].idxmax() + 1
max_sales = df['Sales'].max()
plt.text(max_sales_day, max_sales + 10, f'Peak: {max_sales} units', horizontalalignment='center', color='black')

# Set the title
plt.title('Monthly Sales Performance', pad=20)

# Set the x and y axis labels
plt.xlabel('Day')
plt.ylabel('Sales (units)')

# Show the plot
plt.show()