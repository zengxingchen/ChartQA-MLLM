
import matplotlib.pyplot as plt

# Data to plot
years = ['2000', '2001', '2002', '2003', '2004', '2005',
         '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017',
         '2018', '2019', '2020', '2021', '2022', '2023']
ratings = [4.5, 4.7, 4.6, 4.8, 4.9, 5.0, 4.3, 4.4, 4.2, 4.6, 
           4.7, 4.5, 4.9, 4.8, 4.6, 4.7, 4.5, 4.8, 4.9, 5.0, 
           4.3, 4.4, 4.2, 4.6]

# Plot a horizontal bar chart
plt.figure(figsize=(10, 12))  # Width and height of the chart
plt.barh(y=years, width=ratings, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', 
    '#A833FF', '#FF8333', '#57FF33', '#33A8FF', 
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', 
    '#A833FF', '#FF8333', '#57FF33', '#33A8FF', 
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', 
    '#A833FF', '#FF8333', '#57FF33', '#33A8FF'], 
    height=0.5)  # Band height of the bars

# Set the title and labels
plt.title('Annual Movie Ratings Over the Years', fontsize=18)
plt.xlabel('Rating', fontsize=14)
plt.ylabel('Year', fontsize=14)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()