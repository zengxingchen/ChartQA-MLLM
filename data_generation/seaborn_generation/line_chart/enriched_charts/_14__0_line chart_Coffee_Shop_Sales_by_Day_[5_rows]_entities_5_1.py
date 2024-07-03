
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data dictionary with month and corresponding average tourist visits
data = {
    "Month": ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    "Average_Visits": [1200, 1500, 1800, 2400, 2800, 3500, 4000, 4200, 3000, 2500, 1800, 1300]
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a line chart
plt.figure(figsize=(12, 7))  # Changing the size of the chart
sns.lineplot(data=df, x="Month", y="Average_Visits", color="#1E90FF", marker="o")

# Annotating the highest and lowest tourist visit points
plt.annotate(
    'Highest\nVisits', xy=('August', 4200), xytext=('September', 4500),
    arrowprops=dict(facecolor='red', shrink=0.05), color='red', weight='bold'
)
plt.annotate(
    'Lowest\nVisits', xy=('January', 1200), xytext=('February', 1000),
    arrowprops=dict(facecolor='purple', shrink=0.05), color='purple', weight='bold'
)

# Adding chart title and labels
plt.title("Monthly Average Tourist Visits in 2023")
plt.xlabel("Month")
plt.ylabel("Average Visits")

# Customizing the appearance of the ticks on the x-axis for better readability
plt.xticks(rotation=45)

# Show the final plot
plt.show()