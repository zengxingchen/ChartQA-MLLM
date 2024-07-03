
import matplotlib.pyplot as plt

# Data to plot
years = ['2000', '2001', '2002', '2003', '2004', '2005',
         '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017',
         '2018', '2019', '2020', '2021', '2022', '2023']
population = [1500000, 1600000, 1700000, 1800000, 1900000, 2000000,
              2100000, 2200000, 2300000, 2400000, 2500000, 2600000,
              2700000, 2800000, 2900000, 3000000, 3100000, 3200000,
              3300000, 3400000, 3500000, 3600000, 3700000, 3800000]

# Plot a horizontal bar chart
plt.figure(figsize=(12, 10))  # Width and height of the chart
plt.barh(y=years, width=population, color=[
    '#003f5c', '#374c80', '#7a5195', '#bc5090',
    '#ef5675', '#ff764a', '#ffa600', '#003f5c',
    '#374c80', '#7a5195', '#bc5090', '#ef5675',
    '#ff764a', '#ffa600', '#003f5c', '#374c80',
    '#7a5195', '#bc5090', '#ef5675', '#ff764a',
    '#ffa600', '#003f5c', '#374c80', '#7a5195'], 
    height=0.5)  # Band height of the bars

# Set the title and labels
plt.title('City Population Growth Over the Years', fontsize=18, pad=20)
plt.xlabel('Population', fontsize=14)
plt.ylabel('Year', fontsize=14)

# Set y-axis limit
plt.xlim(1000000, 4000000)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()