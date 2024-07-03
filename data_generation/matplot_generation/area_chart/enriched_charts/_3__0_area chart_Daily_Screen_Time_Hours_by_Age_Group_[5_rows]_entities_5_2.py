
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Day": list(range(1, 32)),
    "Books_Sold": [50, 55, 53, 57, 59, 63, 62, 67, 70, 75, 78, 82, 85, 88, 90, 92, 91, 94, 97, 95, 98, 100, 102, 105, 108, 107, 110, 113, 115, 117, 120]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the area plot
plt.figure(figsize=(14, 8))
area_chart = plt.plot(df['Day'], df['Books_Sold'], color="#2ca02c")
plt.fill_between(df['Day'], df['Books_Sold'], color="#2ca02c", alpha=0.3)

# Annotate a specific day
plt.annotate('Highest Sales',
             xy=(31, 120),
             xytext=(20, 110),
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             )

# Add chart title and labels
plt.title('Daily Book Sales in January', fontsize=16, pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Number of Books Sold')

# Show the plot
plt.show()