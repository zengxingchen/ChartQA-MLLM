
import matplotlib.pyplot as plt

# Sample data
data = [
    {'Quarter': 'Q1-2021', 'Cookies': 520, 'Cakes': 430, 'Pastries': 350, 'Bread': 710, 'Donuts': 300},
    {'Quarter': 'Q2-2021', 'Cookies': 560, 'Cakes': 440, 'Pastries': 360, 'Bread': 680, 'Donuts': 320},
    {'Quarter': 'Q3-2021', 'Cookies': 540, 'Cakes': 420, 'Pastries': 400, 'Bread': 730, 'Donuts': 300},
    {'Quarter': 'Q4-2021', 'Cookies': 580, 'Cakes': 470, 'Pastries': 390, 'Bread': 760, 'Donuts': 350},
    {'Quarter': 'Q1-2022', 'Cookies': 500, 'Cakes': 460, 'Pastries': 420, 'Bread': 700, 'Donuts': 310},
    {'Quarter': 'Q2-2022', 'Cookies': 530, 'Cakes': 480, 'Pastries': 410, 'Bread': 720, 'Donuts': 330},
    {'Quarter': 'Q3-2022', 'Cookies': 515, 'Cakes': 450, 'Pastries': 415, 'Bread': 740, 'Donuts': 325}
]

# Extract information for plotting
quarters = [entry['Quarter'] for entry in data]
cookies = [entry['Cookies'] for entry in data]
cakes = [entry['Cakes'] for entry in data]
pastries = [entry['Pastries'] for entry in data]
bread = [entry['Bread'] for entry in data]
donuts = [entry['Donuts'] for entry in data]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(quarters, cookies, label='Cookies', color='skyblue')
ax.bar(quarters, cakes, bottom=cookies, label='Cakes', color='sandybrown')
ax.bar(quarters, pastries, bottom=[i+j for i,j in zip(cookies, cakes)], label='Pastries', color='lightgreen')
ax.bar(quarters, bread, bottom=[i+j+k for i,j,k in zip(cookies, cakes, pastries)], label='Bread', color='lightcoral')
ax.bar(quarters, donuts, bottom=[i+j+k+l for i,j,k,l in zip(cookies, cakes, pastries, bread)], label='Donuts', color='plum')

# Adding labels and title
plt.ylabel('Units Sold')
plt.xlabel('Quarter')
plt.title('Sales Data by Quarter')

# Adding legend
plt.legend(loc='upper left')

# Adding grid on y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotating values on top of the bars for better readability
for i in range(len(quarters)):
    total = cookies[i] + cakes[i] + pastries[i] + bread[i] + donuts[i]
    plt.text(i, total + 5, str(total), ha='center')

# Display plot
plt.show()