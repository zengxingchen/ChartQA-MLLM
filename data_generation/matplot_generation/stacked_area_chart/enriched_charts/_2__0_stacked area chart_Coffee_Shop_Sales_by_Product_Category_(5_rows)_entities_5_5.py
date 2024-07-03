
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'AI Research': [500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720],
    'Robotics': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'Quantum Computing': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210],
}

# Create a dataframe
df = pd.DataFrame(data)

# Define x-axis based on 'Month'
x = df['Month']

# Plot using specific color codes
plt.figure(figsize=(14, 8))
plt.stackplot(x, df['AI Research'], df['Robotics'], df['Quantum Computing'], 
              colors=['#69B3A2', '#404080', '#DAA520'])

# Adding title and labels
plt.title('Tech Research Budget Allocation Over A Year', pad=20)
plt.xlabel('Month')
plt.ylabel('Budget (in thousands USD)')

# Add annotations for 'Quantum Computing' for the month of January and December
plt.annotate('Quantum Computing in January', xy=(0, df['AI Research'][0] + df['Robotics'][0]), 
             xytext=(0, 700), arrowprops=dict(facecolor='black', arrowstyle='->'))
             
plt.annotate('Quantum Computing in December', xy=(11, df['AI Research'][11] + df['Robotics'][11] + df['Quantum Computing'][11]), 
             xytext=(11, 1000), arrowprops=dict(facecolor='black', arrowstyle='->'))

# Display the figure
plt.show()