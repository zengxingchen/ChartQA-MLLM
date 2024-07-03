
import matplotlib.pyplot as plt

# Generate data points
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
calories = [1800, 2200, 2100, 2500, 2400, 2700, 2600]

plt.figure(figsize=(12, 8))  # Change the width and height of the chart

# Create a horizontal bar chart with specified bar width and colors
plt.barh(days, calories, color=[
    '#FF5733', '#33B8FF', '#8E33FF', '#FFC300', '#57C785', '#D733FF', '#FF8D33'], height=0.5)

plt.xlabel('Calories', fontsize=14)
plt.title('Weekly Calorie Intake', fontsize=16)
plt.xlim(1000, 2800)  # Adjusted to start from 1000 for better visualization

plt.tight_layout()
plt.show()