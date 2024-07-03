
import matplotlib.pyplot as plt

# Data Points
sleep_hours = [
    3.2, 4.1, 4.7, 5.0, 5.2, 5.5, 6.0, 6.1, 6.3, 6.7, 7.0, 7.1, 7.3, 7.5, 7.7, 8.0, 8.2, 8.5, 8.8, 9.0,
    9.3, 9.5, 9.7, 10.0, 10.2, 10.5, 10.7, 11.0, 11.2, 11.5, 11.7, 12.0, 12.3, 12.5, 12.7, 13.0, 13.3, 13.5, 
    13.8, 14.0, 14.3, 14.5, 14.8, 15.0, 15.2, 15.5, 15.8, 16.0, 16.3, 16.5, 16.8, 17.0, 17.3, 17.5, 17.8, 18.0, 
    18.2, 18.5, 18.8, 19.0, 19.3, 19.5, 19.8, 20.0, 20.3, 20.5, 20.8, 21.0, 21.3, 21.5, 21.8, 22.0, 22.3, 22.5, 
    22.8, 23.0, 23.3, 23.5, 23.8, 24.0, 24.3, 24.5, 24.8, 25.0, 25.3, 25.5, 25.8, 26.0, 26.3, 26.5, 26.8, 27.0, 
    27.3, 27.5, 27.8, 28.0, 28.3, 28.5, 28.8, 29.0
]

# Histogram Configuration
plt.figure(figsize=(10, 8))
plt.hist(sleep_hours, bins=20, orientation='horizontal', color='#3498db', rwidth=0.7)
plt.title('Daily Sleep Hours Distribution')
plt.ylabel('Sleep Hours')
plt.xlabel('Frequency')
plt.grid(axis='x', color='gray', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()