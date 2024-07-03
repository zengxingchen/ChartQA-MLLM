
import matplotlib.pyplot as plt

# Data
values = [
    3, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
    27, 28, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 44, 45, 46, 47, 48, 50, 52, 
    53, 54, 55, 56, 58, 60, 62, 64, 65, 66, 68, 70, 72, 73, 74, 75, 76, 78, 80, 82, 
    83, 84, 85, 86, 87, 88, 90, 92, 94, 95, 96, 98, 100, 102, 103, 104, 106, 108, 
    110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 
    142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 
    174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200
]

# Create histogram
plt.figure(figsize=(12, 6))
plt.hist(values, bins=25, color='#2ca02c', rwidth=0.8)

# Customize chart
plt.title('Weekly Running Distances (in miles)')
plt.xlabel('Distance (miles)')
plt.ylabel('Frequency')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)

plt.show()