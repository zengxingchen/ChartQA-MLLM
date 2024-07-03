
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data dictionary with month and corresponding number of visitors
data = {
    "Month": ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    "Number_of_Visitors": [1200, 1350, 1450, 1600, 1800, 2200, 2400, 2500, 2300, 2100, 1900, 1700]
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a line chart
plt.figure(figsize=(14, 9))  # Changing the size of the chart
sns.lineplot(data=df, x="Month", y="Number_of_Visitors", color="#FF5733", marker="o")

# Annotating the highest and lowest visitor points
plt.annotate(
    'Highest\nVisitors', xy=('August', 2500), xytext=('September', 2600),
    arrowprops=dict(facecolor='green', shrink=0.05), color='green', weight='bold'
)
plt.annotate(
    'Lowest\nVisitors', xy=('January', 1200), xytext=('February', 1100),
    arrowprops=dict(facecolor='blue', shrink=0.05), color='blue', weight='bold'
)

# Adding chart title and labels
plt.title("Monthly Number of Visitors to the Museum in 2023", pad=20)
plt.xlabel("Month")
plt.ylabel("Number of Visitors")

# Customizing the appearance of the ticks on the x-axis for better readability
plt.xticks(rotation=45)

# Show the final plot
plt.show()