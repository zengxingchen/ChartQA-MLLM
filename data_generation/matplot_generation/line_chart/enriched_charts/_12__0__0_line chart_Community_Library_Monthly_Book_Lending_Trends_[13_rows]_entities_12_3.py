
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
audience_engagement = [
    10, 12, 18, 24, 28, 32, 30, 25, 22, 18, 15, 12
]

# Create the plot
plt.figure(figsize=(12, 8))  # Change the size of the chart
plt.plot(months, audience_engagement, marker='o', color="#1E90FF", linewidth=3)  # Change color and add markers

# Annotations
for i, engagement in enumerate(audience_engagement):
    plt.annotate(f"{engagement}%", (months[i], engagement), textcoords="offset points", xytext=(0, 10),
                 ha='center', color="#FF6347")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Month')
plt.ylabel('Audience Engagement (%)')
plt.title('Monthly Audience Engagement')
plt.grid(True)

# Show the plot
plt.show()