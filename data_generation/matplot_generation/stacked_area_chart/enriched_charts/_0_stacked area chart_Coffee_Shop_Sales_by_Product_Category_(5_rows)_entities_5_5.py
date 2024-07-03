
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Housing': [700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700],
    'Transportation': [150, 160, 150, 165, 155, 150, 160, 155, 150, 165, 155, 150],
    'Food': [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410],
}

# Create a dataframe
df = pd.DataFrame(data)

# Define x-axis based on 'Month'
x = df['Month']

# Plot using specific color codes
plt.figure(figsize=(12, 6))
plt.stackplot(x, df['Housing'], df['Transportation'], df['Food'], 
              colors=['#FFDDC1', '#FFABAB', '#FFC3A0'])

# Adding title and labels
plt.title('Personal Monthly Budget Over A Year')
plt.xlabel('Month')
plt.ylabel('Expenses (USD)')

# Add annotations for 'Food' for the month of January and December
plt.annotate('Food in January', xy=(0, df['Housing'][0] + df['Transportation'][0]), 
             xytext=(0, 1200), arrowprops=dict(facecolor='black', arrowstyle='->'))
             
plt.annotate('Food in December', xy=(11, df['Housing'][11] + df['Transportation'][11] + df['Food'][11]), 
             xytext=(11, 1000), arrowprops=dict(facecolor='black', arrowstyle='->'))

# Display the figure
plt.show()