
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
membership_growth = [
    2, 5, 10, 15, 20, 25, 30, 28, 23, 18, 12, 7
]

# Create the plot
plt.figure(figsize=(14, 7))  # Change the size of the chart
plt.plot(months, membership_growth, marker='s', color="#2E8B57", linewidth=2)  # Change color and add markers

# Annotations
for i, growth in enumerate(membership_growth):
    plt.annotate(f"{growth}%", (months[i], growth), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#FF4500")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Month')
plt.ylabel('Membership Growth (%)')
plt.title('Monthly Gym Membership Growth')
plt.grid(True)

# Show the plot
plt.show()