
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
mental_health_expenditure = [120, 110, 130, 140, 190, 180, 170, 160, 200, 220, 210, 230]
physical_health_expenditure = [150, 170, 160, 180, 200, 210, 220, 230, 240, 250, 260, 270]

# Plot setup
fig, ax = plt.subplots(figsize=(14, 10))

# Stacked bar chart (vertical)
plt.bar(months, mental_health_expenditure, color='#FF6347', edgecolor='white', width=0.65, label='Mental Health Expenditure')
plt.bar(months, physical_health_expenditure, bottom=mental_health_expenditure, color='#4682B4', edgecolor='white', width=0.65, label='Physical Health Expenditure')

# Adding numerical labels
for i, (mh, ph) in enumerate(zip(mental_health_expenditure, physical_health_expenditure)):
    plt.text(i, mh / 2, str(mh), ha='center', va='center', color='black')
    plt.text(i, mh + ph / 2, str(ph), ha='center', va='center', color='black')

# Labels, title and legend
plt.ylabel('Expenditure (in thousands)')
plt.title('Monthly Health Expenditure on Mental and Physical Health')
plt.legend()

# Show the plot
plt.show()