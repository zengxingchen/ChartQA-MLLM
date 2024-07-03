
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given dataset
data = {
    'Car Model': ['Toyota Corolla', 'Honda Civic', 'Ford Focus', 'Chevrolet Cruze', 'Hyundai Elantra',
                  'Nissan Sentra', 'Kia Forte', 'Volkswagen Jetta', 'Subaru Impreza', 'Mazda 3'],
    'Average MPG': [33, 35, 30, 28, 32, 31, 29, 33, 27, 36]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize a Matplotlib figure and set its size
plt.figure(figsize=(10, 8))

# Create horizontal bar chart
sns.barplot(
    x='Average MPG',
    y='Car Model',
    data=df,
    palette=[
        '#FF5733', '#C70039', '#900C3F', '#571845', '#2E86C1',
        '#1F618D', '#3498DB', '#AED6F1', '#5DADE2', '#2874A6'
    ],
    dodge=False
)

# Customize the chart
plt.title('Average Fuel Efficiency by Car Model')
plt.xlabel('Average Miles Per Gallon (MPG)')
plt.ylabel('Car Model')

# Adjust the width of the bars
for patch in plt.gca().patches:
    patch.set_height(0.5)

# Show the plot
plt.show()