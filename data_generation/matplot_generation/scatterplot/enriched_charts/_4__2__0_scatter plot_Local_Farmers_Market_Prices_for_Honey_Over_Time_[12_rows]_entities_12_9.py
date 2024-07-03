
import matplotlib.pyplot as plt

# Define the data for the scatterplot
days = list(range(1, 32))
steps = [12000, 13000, 12500, 14000, 14500, 13500, 15000, 15500, 16000, 16200,
         15800, 15300, 14900, 16500, 16800, 17000, 17400, 18000, 18500, 19000,
         19500, 20000, 20500, 21000, 21500, 22000, 22500, 23000, 23500, 24000, 24500]
distance = [9.2, 10.0, 9.5, 10.7, 11.1, 10.3, 11.5, 11.8, 12.2, 12.3,
            12.0, 11.6, 11.3, 12.5, 12.7, 13.0, 13.2, 13.5, 14.0, 14.5,
            14.8, 15.0, 15.3, 15.7, 16.0, 16.5, 16.8, 17.0, 17.5, 18.0, 18.3]

# Create the scatterplot
plt.figure(figsize=(16, 12))
plt.scatter(steps, distance, color='#FF4500')  # Modify the color scheme using a specific color code

# Apply labels and a title to the scatterplot
plt.xlabel('Daily Steps Count')
plt.ylabel('Daily Distance Walked (km)')
plt.title('Daily Distance Walked vs Steps Count')

# Display the scatterplot
plt.show()