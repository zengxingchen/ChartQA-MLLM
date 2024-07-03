
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data dictionary with month and corresponding book sales
data = {
    "Month": ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    "Book_Sales": [120, 130, 150, 170, 180, 190, 200, 195, 185, 160, 140, 130]
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a line chart
plt.figure(figsize=(12, 8))  # Changing the size of the chart
sns.lineplot(data=df, x="Month", y="Book_Sales", color="#4B0082", marker="o")

# Annotating the highest and lowest sales points
plt.annotate(
    'Highest\nSales', xy=('July', 200), xytext=('August', 205),
    arrowprops=dict(facecolor='green', shrink=0.05), color='green', weight='bold'
)
plt.annotate(
    'Lowest\nSales', xy=('January', 120), xytext=('February', 115),
    arrowprops=dict(facecolor='blue', shrink=0.05), color='blue', weight='bold'
)

# Adding chart title and labels
plt.title("Monthly Book Sales Trends in 2023", pad=20)
plt.xlabel("Month")
plt.ylabel("Book Sales")

# Customizing the appearance of the ticks on the x-axis for better readability
plt.xticks(rotation=45)

# Show the final plot
plt.show()