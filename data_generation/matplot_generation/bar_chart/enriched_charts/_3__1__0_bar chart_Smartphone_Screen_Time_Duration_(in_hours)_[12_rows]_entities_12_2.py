import matplotlib.pyplot as plt

years = ['2000', '2001', '2002', '2003', '2004', '2005',
         '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017',
         '2018', '2019', '2020', '2021', '2022', '2023']
books_published = [150, 160, 170, 180, 185, 190, 195, 200, 210, 220, 
                   225, 230, 235, 240, 250, 260, 270, 280, 290, 300, 
                   310, 320, 330, 340]

plt.figure(figsize=(12, 10))
plt.barh(y=years, width=books_published, color=[
    '#4c72b0', '#55a868', '#c44e52', '#8172b2', 
    '#ccb974', '#64b5cd', '#e377c2', '#7f7f7f', 
    '#bcbd22', '#17becf', '#4c72b0', '#55a868', 
    '#c44e52', '#8172b2', '#ccb974', '#64b5cd', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#4c72b0', '#55a868', '#c44e52', '#8172b2'], 
    height=0.5)

plt.title('Annual Books Published Over the Years', fontsize=18, pad=20)
plt.xlabel('Books Published', fontsize=14)
plt.ylabel('Year', fontsize=14)

plt.tight_layout()
plt.show()