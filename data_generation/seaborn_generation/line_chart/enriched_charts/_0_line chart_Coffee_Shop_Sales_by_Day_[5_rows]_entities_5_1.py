
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data dictionary with month and corresponding average temperature
data = {
    "Month": ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    "Average_Temperature_C": [2, 3, 6, 11, 16, 20, 22, 21, 18, 13, 7, 3]
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a line chart
plt.figure(figsize=(10, 6))  # Changing the size of the chart
sns.lineplot(data=df, x="Month", y="Average_Temperature_C", color="#FF5733", marker="o")

# Annotating the highest and lowest temperature points
plt.annotate(
    'Highest\nTemperature', xy=('July', 22), xytext=('August', 23),
    arrowprops=dict(facecolor='green', shrink=0.05), color='green', weight='bold'
)
plt.annotate(
    'Lowest\nTemperature', xy=('January', 2), xytext=('February', 1),
    arrowprops=dict(facecolor='blue', shrink=0.05), color='blue', weight='bold'
)

# Adding chart title and labels
plt.title("Monthly Average Temperature Trends in 2021")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")

# Customizing the appearance of the ticks on the x-axis for better readability
plt.xticks(rotation=45)

# Show the final plot
plt.show()