
import matplotlib.pyplot as plt
import numpy as np

ages = [
    17, 18, 19, 20, 20, 21, 21, 21, 22, 22, 23, 23, 23, 24, 24, 24, 24, 25, 25, 
    25, 26, 26, 27, 27, 27, 28, 28, 28, 29, 29, 29, 30, 30, 30, 31, 31, 31, 32, 
    32, 33, 33, 34, 34, 35, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40, 40, 
    41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 48, 49, 50, 52, 53, 54, 
    55, 56, 58, 60, 61, 62, 63, 65, 66, 68, 69, 70
]

bins = range(15, 75, 5)

plt.figure(figsize=(12, 6))
plt.hist(ages, bins=bins, color='#ff6347', rwidth=0.9, orientation='horizontal')
plt.ylabel('Age Group')
plt.xlabel('Frequency')
plt.title('Age Distribution in Music & Performing Arts')
plt.grid(axis='x')
plt.show()