
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    "Brand": ["Apple", "Samsung", "Xiaomi", "Huawei", "OnePlus", "Google", "Nokia", "Sony", "Motorola"],
    "Market Share": [30, 25, 15, 10, 7, 5, 4, 2, 2]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the color scheme
palette_color = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#c4e17f", "#76dd1f", "#ff6464"]

# Plot the pie chart
plt.figure(figsize=(10, 8))
plt.pie(df['Market Share'], labels=df['Brand'], colors=palette_color, autopct='%1.1f%%', startangle=140)
plt.title('Smartphone Market Share by Brand')
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

# Display the plot
plt.show()