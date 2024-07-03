
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Reading': [300, 320, 350, 370, 390, 410, 430, 450, 470, 490, 510, 530],
    'Writing': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
    'Studying': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
}

# Create a dataframe
df = pd.DataFrame(data)

# Define x-axis based on 'Month'
x = df['Month']

# Plot using specific color codes
plt.figure(figsize=(16, 10))
plt.stackplot(x, df['Reading'], df['Writing'], df['Studying'], 
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Adding title and labels
plt.title('Monthly Activities for Different Purposes Over A Year', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Activities', fontsize=14)

# Add annotations for 'Studying' for the month of January and December
plt.annotate('Studying in January', xy=(0, df['Reading'][0] + df['Writing'][0]), 
             xytext=(0, 600), arrowprops=dict(facecolor='black', arrowstyle='->'))
             
plt.annotate('Studying in December', xy=(11, df['Reading'][11] + df['Writing'][11] + df['Studying'][11]), 
             xytext=(11, 1100), arrowprops=dict(facecolor='black', arrowstyle='->'))

# Display the figure
plt.show()