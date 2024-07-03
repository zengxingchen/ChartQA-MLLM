
import matplotlib.pyplot as plt

# Data to plot
years = ['2000', '2001', '2002', '2003', '2004', '2005',
         '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017',
         '2018', '2019', '2020', '2021', '2022', '2023']
emissions = [450, 455, 460, 475, 480, 485, 490, 495, 505, 515, 
             525, 535, 545, 555, 565, 575, 585, 595, 605, 615, 
             625, 635, 645, 655]

# Plot a horizontal bar chart
plt.figure(figsize=(12, 10))  # Width and height of the chart
plt.barh(y=years, width=emissions, color=[
    '#4e79a7', '#f28e2c', '#e15759', '#76b7b2', 
    '#59a14f', '#edc949', '#af7aa1', '#ff9da7', 
    '#9c755f', '#bab0ab', '#4e79a7', '#f28e2c', 
    '#e15759', '#76b7b2', '#59a14f', '#edc949', 
    '#af7aa1', '#ff9da7', '#9c755f', '#bab0ab', 
    '#4e79a7', '#f28e2c', '#e15759', '#76b7b2'], 
    height=0.5)  # Band height of the bars

# Set the title and labels
plt.title('Annual CO2 Emissions Over the Years (2000-2023)', fontsize=18, pad=20)
plt.xlabel('CO2 Emissions (in metric tons)', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.xlim(440, 660)  # Truncated y-axis limits

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()