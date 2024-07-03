
import matplotlib.pyplot as plt

# Data
cities = [
    'Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Cairo', 'Beijing', 'Dhaka',
    'Mexico City', 'Osaka', 'Karachi', 'Chongqing', 'Istanbul', 'Buenos Aires', 'Kolkata',
    'Lagos', 'Kinshasa', 'Manila', 'Tianjin', 'Rio de Janeiro', 'Guangzhou', 'Lahore',
    'Bangalore', 'Paris', 'Bogota', 'Jakarta', 'Chennai', 'Lima', 'Bangkok', 'Hyderabad'
]
populations = [
    37400068, 28514000, 25582000, 21650000, 20411000, 20076000, 19618000, 19578000,
    21581000, 19281000, 15400000, 15354000, 15030000, 14900000, 14850000,
    14203000, 13656000, 13482000, 13317000, 13293000, 13081000, 12188000,
    11978000, 10858000, 10816000, 10780000, 10470000, 10150000, 10302000, 9746000
]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(15, 10))  # Changed figure size

# Plotting the horizontal bar chart
ax.barh(cities, populations, color=['#8A2BE2', '#FF4500', '#00CED1', '#FF69B4', '#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2', '#FF4500', '#00CED1', '#FF69B4', '#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2', '#FF4500', '#00CED1', '#FF69B4', '#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2', '#FF4500', '#00CED1', '#FF69B4', '#FF6347', '#4682B4'], height=0.5)  # Changed colors and bar height

# Customizing the plot (labels, title, etc.)
ax.set_xlabel('Population')
ax.set_title('Population of the World’s Largest Cities', pad=20)
ax.set_xlim([9000000, 40000000])  # Adjusted to accommodate the minimum data point

# Display the plot
plt.tight_layout()
plt.show()