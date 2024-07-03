
import matplotlib.pyplot as plt
import pandas as pd

# Data provided
data = [
    {'Month': 'January', 'Chocolate Sales (Scoops)': 350},
    {'Month': 'February', 'Chocolate Sales (Scoops)': 280},
    {'Month': 'March', 'Chocolate Sales (Scoops)': 300},
    {'Month': 'April', 'Chocolate Sales (Scoops)': 450},
    {'Month': 'May', 'Chocolate Sales (Scoops)': 500},
    {'Month': 'June', 'Chocolate Sales (Scoops)': 530},
    {'Month': 'July', 'Chocolate Sales (Scoops)': 600},
    {'Month': 'August', 'Chocolate Sales (Scoops)': 590}
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Let's plot the 'Month' on the x-axis and 'Chocolate Sales (Scoops)' on the y-axis
x = df['Month']
y = df['Chocolate Sales (Scoops)']

# Plotting the area chart
plt.fill_between(x, y, color="skyblue", alpha=0.4)
plt.plot(x, y, color="Slateblue", alpha=0.6, linewidth=2)

# Adding title and labels
plt.title('Chocolate Sales (Scoops) by Month')
plt.xlabel('Month')
plt.ylabel('Chocolate Sales (Scoops)')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add a grid for easier reading
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Displaying the plot
plt.tight_layout()
plt.show()