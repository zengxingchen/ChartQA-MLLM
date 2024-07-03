
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', 
                 '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', 
                 '2020', '2021', '2022', '2023', '2024'],
    'Under 18': [30, 28, 29, 27, 26, 27, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7],
    '18-65': [55, 57, 56, 58, 58, 57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 68, 69, 70, 71, 72, 73, 73, 74, 75],
    'Over 65': [15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 18, 18, 18]
}

categories = data['Category']
under_18_values = data['Under 18']
adult_values = data['18-65']
senior_values = data['Over 65']

ind = np.arange(len(categories))  # the x locations for the groups
width = 0.75  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 9))

p1 = ax.bar(ind, under_18_values, width, color='#ff9999')
p2 = ax.bar(ind, adult_values, width, bottom=under_18_values, color='#66b3ff')
p3 = ax.bar(ind, senior_values, width, bottom=np.array(under_18_values) + np.array(adult_values), color='#99ff99')

ax.set_ylabel('Percentage')
ax.set_title('Population Age Distribution Over Years')
ax.set_xticks(ind)
ax.set_xticklabels(categories, rotation=45)
ax.legend((p1[0], p2[0], p3[0]), ('Under 18', '18-65', 'Over 65'))

plt.show()