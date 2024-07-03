
import matplotlib.pyplot as plt

# Data to plot
years = ['2000', '2001', '2002', '2003', '2004', '2005',
         '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017',
         '2018', '2019', '2020', '2021', '2022', '2023']
emissions = [410, 415, 420, 430, 435, 440, 445, 450, 460, 470, 
             480, 490, 500, 510, 515, 520, 525, 530, 540, 550, 
             560, 570, 580, 590]

# Plot a vertical bar chart
plt.figure(figsize=(14, 8))  # Width and height of the chart
plt.bar(x=years, height=emissions, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
    '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', 
    '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], 
    width=0.6)  # Band width of the bars

# Set the title and labels
plt.title('Annual CO2 Emissions Over the Years', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('CO2 Emissions (in metric tons)', fontsize=14)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()