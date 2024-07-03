
import matplotlib.pyplot as plt

# Data to plot
years = ['2000', '2001', '2002', '2003', '2004', '2005',
         '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017',
         '2018', '2019', '2020', '2021', '2022', '2023']
attendance = [15000, 18000, 22000, 25000, 23000, 27000,
              30000, 31000, 29000, 33000, 35000, 37000,
              39000, 41000, 43000, 45000, 47000, 49000,
              51000, 53000, 55000, 57000, 59000, 61000]

# Plot a vertical bar chart
plt.figure(figsize=(14, 8))  # Width and height of the chart
plt.bar(x=years, height=attendance, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
    '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', 
    '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], 
    width=0.4)  # Band width of the bars

# Set the title and labels
plt.title('Annual Concert Attendance Over the Years', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Attendance', fontsize=14)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()