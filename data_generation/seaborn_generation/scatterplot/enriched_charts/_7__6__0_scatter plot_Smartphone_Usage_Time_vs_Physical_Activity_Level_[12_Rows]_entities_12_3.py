
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the data points
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Sugar Intake (grams)': [30, 45, 60, 40, 55, 70, 50, 35, 50, 65, 45, 60, 75, 55],
    'Calories Consumed': [1500, 1700, 1800, 1600, 2000, 2200, 1900, 1550, 1750, 1850, 1650, 2100, 2300, 1950]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize a seaborn scatterplot
plt.figure(figsize=(14, 10))
scatter = sns.scatterplot(
    x='Sugar Intake (grams)',
    y='Calories Consumed',
    data=df,
    palette=['#FF6347', '#FFA07A', '#8B0000', '#FFD700', '#DAA520', '#FF4500', '#2E8B57',
             '#8FBC8F', '#3CB371', '#20B2AA', '#4682B4', '#5F9EA0', '#6A5ACD', '#7B68EE'],
    s=200  # Define the size of the points
)

# Set the title
scatter.set_title('Daily Sugar Intake vs. Calories Consumed', fontsize=16)

# Show the plot
plt.show()