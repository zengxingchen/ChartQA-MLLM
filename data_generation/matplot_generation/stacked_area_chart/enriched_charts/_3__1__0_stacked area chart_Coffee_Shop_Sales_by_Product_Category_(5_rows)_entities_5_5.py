
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Football': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
    'Basketball': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'Tennis': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],
}

# Create a dataframe
df = pd.DataFrame(data)

# Define x-axis based on 'Month'
x = df['Month']

# Plot using specific color codes
plt.figure(figsize=(16, 10))
plt.stackplot(x, df['Football'], df['Basketball'], df['Tennis'], 
              colors=['#FF5733', '#33FF57', '#3357FF'])

# Adding title and labels
plt.title('Monthly Participation in Different Sports Activities', fontsize=20)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Number of Participants', fontsize=16)

# Add annotations for 'Football' for the month of January and December
plt.annotate('Football in January', xy=(0, df['Football'][0]), 
             xytext=(0, 400), arrowprops=dict(facecolor='black', arrowstyle='->'))
             
plt.annotate('Football in December', xy=(11, df['Football'][11] + df['Basketball'][11] + df['Tennis'][11]), 
             xytext=(11, 800), arrowprops=dict(facecolor='black', arrowstyle='->'))

# Add legend
plt.legend(['Football', 'Basketball', 'Tennis'], loc='upper left', fontsize=14)

# Display the figure
plt.show()