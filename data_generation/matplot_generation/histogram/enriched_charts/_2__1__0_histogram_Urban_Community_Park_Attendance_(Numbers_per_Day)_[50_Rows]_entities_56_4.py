
import matplotlib.pyplot as plt

books_read = [
    35, 28, 32, 45, 38, 40, 42, 37, 29, 33, 41, 34, 36, 39, 50, 30, 27, 31, 43, 44, 
    46, 48, 47, 49, 52, 51, 53, 55, 54, 56, 57, 59, 58, 60, 61, 62, 64, 63, 66, 65, 
    67, 68, 70, 69, 72, 71, 73, 75, 74, 76, 77, 78, 80, 79, 82, 81, 83, 85, 84, 86, 
    88, 87, 89, 91, 90, 92, 93, 95, 94, 96, 98, 97, 99, 100, 101, 103, 102, 104, 106, 
    105, 108, 107, 109, 110, 111, 112, 114, 113, 115, 116, 118, 117, 119, 120, 122, 
    121, 123, 125, 124, 126, 127, 129, 128, 130, 132, 131, 133, 135, 134, 136, 138, 
    137, 139, 140, 142, 141, 143, 145, 144, 146, 148, 147, 149, 150
]

plt.figure(figsize=(12, 8))

plt.hist(books_read, bins=15, orientation='horizontal', color='#1f77b4', edgecolor='#ff7f0e', linewidth=0.8)

plt.title('Number of Books Read in a Year', pad=15)
plt.ylabel('Number of Books')
plt.xlabel('Frequency of Days')

plt.grid(axis='x', color='grey', linestyle='--', linewidth=0.6)

plt.show()