
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data dictionary with month and corresponding average calorie intake in kcal
data = {
    "Month": ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    "Average_Calorie_Intake_kcal": [2200, 2100, 2300, 2500, 2700, 2900, 3100, 3000, 2800, 2600, 2400, 2300]
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a line chart
plt.figure(figsize=(14, 9))  # Changing the size of the chart
sns.lineplot(data=df, x="Month", y="Average_Calorie_Intake_kcal", color="#FF6347", marker="o")

# Annotating the highest and lowest calorie intake points
plt.annotate(
    'Highest\nCalorie Intake', xy=('July', 3100), xytext=('August', 3200),
    arrowprops=dict(facecolor='red', shrink=0.05), color='red', weight='bold'
)
plt.annotate(
    'Lowest\nCalorie Intake', xy=('February', 2100), xytext=('January', 2000),
    arrowprops=dict(facecolor='blue', shrink=0.05), color='blue', weight='bold'
)

# Adding chart title and labels
plt.title("Monthly Average Calorie Intake in 2023", pad=20)
plt.xlabel("Month")
plt.ylabel("Average Calorie Intake (kcal)")

# Customizing the appearance of the ticks on the x-axis for better readability
plt.xticks(rotation=45)

# Show the final plot
plt.show()