
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data: Number of travel activities in various cities
data = {
    "City": ["Paris", "Paris", "Paris", "Paris",
             "New York", "New York", "New York", "New York",
             "Rome", "Rome", "Rome", "Rome",
             "Tokyo", "Tokyo", "Tokyo", "Tokyo",
             "Sydney", "Sydney", "Sydney", "Sydney",
             "London", "London", "London", "London",
             "Dubai", "Dubai", "Dubai", "Dubai",
             "Barcelona", "Barcelona", "Barcelona", "Barcelona"],
    "Activity": ["City Tours", "Museum Visits", "Culinary Tours", "Nightlife",
                 "City Tours", "Museum Visits", "Culinary Tours", "Nightlife",
                 "City Tours", "Museum Visits", "Culinary Tours", "Nightlife",
                 "City Tours", "Museum Visits", "Culinary Tours", "Nightlife",
                 "City Tours", "Museum Visits", "Culinary Tours", "Nightlife",
                 "City Tours", "Museum Visits", "Culinary Tours", "Nightlife",
                 "City Tours", "Museum Visits", "Culinary Tours", "Nightlife",
                 "City Tours", "Museum Visits", "Culinary Tours", "Nightlife"],
    "Number of Activities": [150, 120, 90, 60,
                             180, 130, 110, 70,
                             160, 100, 80, 50,
                             200, 140, 100, 80,
                             130, 90, 70, 60,
                             170, 110, 90, 75,
                             140, 120, 85, 65,
                             160, 110, 95, 70]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group data by Activity
grouped_data = df.groupby("Activity").sum().reset_index()

# Define color list
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#ff6666", "#c2f0c2", "#ffb3b3"]

# Plot
plt.figure(figsize=(14, 10))
squarify.plot(sizes=grouped_data['Number of Activities'], label=grouped_data['Activity'], alpha=0.8, color=colors)
plt.title('Travel & Adventure: Number of Activities Offered in Major Cities', fontsize=15, pad=15)
plt.axis('off')
plt.show()