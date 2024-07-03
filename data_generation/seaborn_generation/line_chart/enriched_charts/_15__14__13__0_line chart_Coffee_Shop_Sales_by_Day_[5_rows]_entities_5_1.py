
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data dictionary with month and corresponding number of sales
data = {
    "Month": ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    "Number_of_Sales": [500, 550, 700, 850, 900, 800, 950, 1100, 1150, 1200, 1300, 1250]
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a line chart
plt.figure(figsize=(16, 10))  # Changing the size of the chart
sns.lineplot(data=df, x="Month", y="Number_of_Sales", color="#1F77B4", marker="o")

# Annotating the highest and lowest sales points
plt.annotate(
    'Highest\nSales', xy=('November', 1300), xytext=('October', 1350),
    arrowprops=dict(facecolor='red', shrink=0.05), color='red', weight='bold'
)
plt.annotate(
    'Lowest\nSales', xy=('January', 500), xytext=('February', 450),
    arrowprops=dict(facecolor='purple', shrink=0.05), color='purple', weight='bold'
)

# Adding chart title and labels
plt.title("Monthly Sales of Electric Cars in 2023", pad=20)
plt.xlabel("Month")
plt.ylabel("Number of Sales")

# Customizing the appearance of the ticks on the x-axis for better readability
plt.xticks(rotation=45)

# Show the final plot
plt.show()