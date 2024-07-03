
import matplotlib.pyplot as plt

years = ['2000', '2001', '2002', '2003', '2004', '2005',
         '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017',
         '2018', '2019', '2020', '2021', '2022', '2023']
books_published = [150, 160, 170, 180, 185, 190, 195, 200, 210, 220, 
                   225, 230, 235, 240, 250, 260, 270, 280, 290, 300, 
                   310, 320, 330, 340]

plt.figure(figsize=(14, 8))
plt.bar(years, books_published, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
    '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', 
    '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], 
    width=0.6)

plt.ylim(150, 350)
plt.title('Annual Books Published Over the Years', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Books Published', fontsize=14)

plt.tight_layout()
plt.show()