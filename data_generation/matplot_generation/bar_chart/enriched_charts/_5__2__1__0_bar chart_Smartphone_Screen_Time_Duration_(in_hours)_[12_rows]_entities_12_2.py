
import matplotlib.pyplot as plt

# Data to plot
years = ['2000', '2001', '2002', '2003', '2004', '2005',
         '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017',
         '2018', '2019', '2020', '2021', '2022', '2023']
ratings = [6.2, 7.3, 8.5, 9.0, 7.5, 6.8, 7.2, 8.1, 6.4, 7.6, 
           8.0, 7.9, 8.3, 7.7, 7.4, 8.6, 8.8, 9.2, 7.0, 7.8, 
           8.7, 7.1, 6.9, 8.9]

# Plot a horizontal bar chart
plt.figure(figsize=(12, 8))  # Width and height of the chart
plt.bar(x=years, height=ratings, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
    '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', 
    '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], 
    width=0.6)  # Band width of the bars

# Set the title and labels
plt.title('Annual Movie Ratings Over the Years', fontsize=18, pad=20)
plt.ylabel('Rating', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Set y-axis limits
plt.ylim(5.5, 9.5)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()