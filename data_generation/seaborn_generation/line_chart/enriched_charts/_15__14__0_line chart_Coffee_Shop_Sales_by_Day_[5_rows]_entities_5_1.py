
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data dictionary with month and corresponding average tourist visits
data = {
    "Month": ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    "Average_Visits": [1200, 1500, 2000, 2200, 2500, 3100, 3500, 3700, 3300, 2800, 2100, 1600]
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a line chart
plt.figure(figsize=(14, 8))  # Changing the size of the chart
sns.lineplot(data=df, x="Month", y="Average_Visits", color="#FF6347", marker="o")

# Annotating the highest and lowest tourist visit points
plt.annotate(
    'Highest\nVisits', xy=('August', 3700), xytext=('September', 4000),
    arrowprops=dict(facecolor='blue', shrink=0.05), color='blue', weight='bold'
)
plt.annotate(
    'Lowest\nVisits', xy=('January', 1200), xytext=('February', 1000),
    arrowprops=dict(facecolor='green', shrink=0.05), color='green', weight='bold'
)

# Adding chart title and labels
plt.title("Monthly Average Tourist Visits in 2023", pad=20)
plt.xlabel("Month")
plt.ylabel("Average Visits")

# Customizing the appearance of the ticks on the x-axis for better readability
plt.xticks(rotation=45)

# Show the final plot
plt.show()