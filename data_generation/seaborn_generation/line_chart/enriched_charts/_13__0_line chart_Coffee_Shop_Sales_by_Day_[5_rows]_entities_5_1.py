
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data dictionary with month and corresponding average rainfall in mm
data = {
    "Month": ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    "Average_Rainfall_mm": [78, 65, 90, 110, 150, 180, 200, 190, 160, 130, 100, 85]
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a line chart
plt.figure(figsize=(12, 8))  # Changing the size of the chart
sns.lineplot(data=df, x="Month", y="Average_Rainfall_mm", color="#1F77B4", marker="o")

# Annotating the highest and lowest rainfall points
plt.annotate(
    'Highest\nRainfall', xy=('July', 200), xytext=('August', 210),
    arrowprops=dict(facecolor='green', shrink=0.05), color='green', weight='bold'
)
plt.annotate(
    'Lowest\nRainfall', xy=('February', 65), xytext=('January', 50),
    arrowprops=dict(facecolor='blue', shrink=0.05), color='blue', weight='bold'
)

# Adding chart title and labels
plt.title("Monthly Average Rainfall in 2021", pad=20)
plt.xlabel("Month")
plt.ylabel("Average Rainfall (mm)")

# Customizing the appearance of the ticks on the x-axis for better readability
plt.xticks(rotation=45)

# Show the final plot
plt.show()