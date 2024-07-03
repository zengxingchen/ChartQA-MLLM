
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [120, 130, 150, 170, 160, 180, 220, 210, 200, 190, 180, 170]

# Modifications to data to enrich visualization
revenue[6] += 20  # July
revenue[-1] -= 10  # December

# Modify color scheme with color codes, change figure size
plt.figure(figsize=(12, 8))
plt.plot(months, revenue, color='#ff5733', marker='o')

# Adding labels with annotations
for i, (month, rev) in enumerate(zip(months, revenue)):
    plt.annotate(f'${rev}', (month, rev), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Company Monthly Revenue for 2023')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')

# Display chart
plt.show()