
import matplotlib.pyplot as plt

# Data provided in the question
chart_data = [
    {'Month': 'January', 'Fruits (kg)': 10, 'Vegetables (kg)': 15, 'Dairy (kg)': 8, 'Meat (kg)': 12},
    {'Month': 'February', 'Fruits (kg)': 12, 'Vegetables (kg)': 17, 'Dairy (kg)': 9, 'Meat (kg)': 14},
    {'Month': 'March', 'Fruits (kg)': 14, 'Vegetables (kg)': 19, 'Dairy (kg)': 10, 'Meat (kg)': 16},
    {'Month': 'April', 'Fruits (kg)': 16, 'Vegetables (kg)': 21, 'Dairy (kg)': 11, 'Meat (kg)': 18},
    {'Month': 'May', 'Fruits (kg)': 18, 'Vegetables (kg)': 23, 'Dairy (kg)': 12, 'Meat (kg)': 20},
    {'Month': 'June', 'Fruits (kg)': 20, 'Vegetables (kg)': 25, 'Dairy (kg)': 13, 'Meat (kg)': 22},
    {'Month': 'July', 'Fruits (kg)': 22, 'Vegetables (kg)': 27, 'Dairy (kg)': 14, 'Meat (kg)': 24},
    {'Month': 'August', 'Fruits (kg)': 24, 'Vegetables (kg)': 29, 'Dairy (kg)': 15, 'Meat (kg)': 26},
    {'Month': 'September', 'Fruits (kg)': 26, 'Vegetables (kg)': 31, 'Dairy (kg)': 16, 'Meat (kg)': 28},
    {'Month': 'October', 'Fruits (kg)': 28, 'Vegetables (kg)': 33, 'Dairy (kg)': 17, 'Meat (kg)': 30},
    {'Month': 'November', 'Fruits (kg)': 30, 'Vegetables (kg)': 35, 'Dairy (kg)': 18, 'Meat (kg)': 32},
    {'Month': 'December', 'Fruits (kg)': 32, 'Vegetables (kg)': 37, 'Dairy (kg)': 19, 'Meat (kg)': 34}
]

# Extracting the data for plotting
months = [entry['Month'] for entry in chart_data]
fruits_kg = [entry['Fruits (kg)'] for entry in chart_data]
vegetables_kg = [entry['Vegetables (kg)'] for entry in chart_data]
dairy_kg = [entry['Dairy (kg)'] for entry in chart_data]
meat_kg = [entry['Meat (kg)'] for entry in chart_data]

# Plotting the data
plt.figure(figsize=(16, 12))

plt.plot(months, fruits_kg, label='Fruits', marker='o', linestyle='-', color='#1f78b4')
plt.plot(months, vegetables_kg, label='Vegetables', marker='s', linestyle='--', color='#33a02c')
plt.plot(months, dairy_kg, label='Dairy', marker='^', linestyle='-.', color='#e31a1c')
plt.plot(months, meat_kg, label='Meat', marker='d', linestyle=':', color='#ff7f00')

# Adding the title and labels
plt.title('Monthly Food Consumption', fontsize=20, pad=30)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Consumption (kg)', fontsize=16)
plt.xticks(rotation=45, fontsize=14)
plt.yticks(fontsize=14)

# Inverting y-axis
plt.gca().invert_yaxis()

# Adding annotations
for i, txt in enumerate(fruits_kg):
    plt.annotate(txt, (months[i], fruits_kg[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, txt in enumerate(vegetables_kg):
    plt.annotate(txt, (months[i], vegetables_kg[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, txt in enumerate(dairy_kg):
    plt.annotate(txt, (months[i], dairy_kg[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, txt in enumerate(meat_kg):
    plt.annotate(txt, (months[i], meat_kg[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Adding a legend
plt.legend(loc='upper right', fontsize=14)

# Adjust layout to prevent clipping and show the plot
plt.tight_layout()
plt.show()