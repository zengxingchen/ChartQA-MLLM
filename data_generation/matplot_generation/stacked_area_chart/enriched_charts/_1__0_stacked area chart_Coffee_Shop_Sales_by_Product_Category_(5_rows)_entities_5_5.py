
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Business': [800, 850, 870, 900, 920, 950, 970, 990, 1010, 1030, 1050, 1070],
    'Leisure': [400, 420, 430, 440, 460, 470, 480, 490, 500, 510, 520, 530],
    'Adventure': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
}

# Create a dataframe
df = pd.DataFrame(data)

# Define x-axis based on 'Month'
x = df['Month']

# Plot using specific color codes
plt.figure(figsize=(14, 8))
plt.stackplot(x, df['Business'], df['Leisure'], df['Adventure'], 
              colors=['#00429d', '#73a2c6', '#e6f5ff'])

# Adding title and labels
plt.title('Monthly Travelers for Different Purposes Over A Year', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Travelers', fontsize=14)

# Add annotations for 'Adventure' for the month of January and December
plt.annotate('Adventure in January', xy=(0, df['Business'][0] + df['Leisure'][0]), 
             xytext=(0, 1800), arrowprops=dict(facecolor='black', arrowstyle='->'))
             
plt.annotate('Adventure in December', xy=(11, df['Business'][11] + df['Leisure'][11] + df['Adventure'][11]), 
             xytext=(11, 2200), arrowprops=dict(facecolor='black', arrowstyle='->'))

# Display the figure
plt.show()