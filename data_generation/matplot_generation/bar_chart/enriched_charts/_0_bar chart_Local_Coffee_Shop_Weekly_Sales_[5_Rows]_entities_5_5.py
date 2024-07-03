
import matplotlib.pyplot as plt

# Generate data points
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
temperatures = [32.0, 34.5, 42.0, 53.5, 63.0, 72.5, 78.0, 76.5, 68.0, 57.0, 47.5, 38.0]

plt.figure(figsize=(14, 8))  # Change the width and height of the chart

# Create a horizontal bar chart with specified bar height and colors
plt.barh(months, temperatures, color=[
    '#FF5733', '#FF8D33', '#FFC300', '#EDDD53', '#ADD45C',
    '#57C785', '#33B8FF', '#3375FF', '#8E33FF', '#D733FF',
    '#FF33AB', '#FF3366'], height=0.6)

plt.xlabel('Average Temperature (°F)', fontsize=14)
plt.title('Average Monthly Temperatures in New York City', fontsize=16)
plt.xlim(0, 90)  # Adjusted to give some space for readability

plt.tight_layout()
plt.show()