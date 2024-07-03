
import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
Books = np.array([120, 130, 140, 135, 145, 150, 155, 160, 165, 170])
Magazines = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
Newspapers = np.array([90, 95, 100, 105, 110, 115, 120, 125, 130, 135])
Journals = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

bar_width = 0.7
fig, ax = plt.subplots(figsize=(12, 10))

ax.bar(years, Books, width=bar_width, label='Books', color='#4B0082')
ax.bar(years, Magazines, bottom=Books, width=bar_width, label='Magazines', color='#7B68EE')
ax.bar(years, Newspapers, bottom=Books+Magazines, width=bar_width, label='Newspapers', color='#4682B4')
ax.bar(years, Journals, bottom=Books+Magazines+Newspapers, width=bar_width, label='Journals', color='#3CB371')

ax.set_ylabel('Quantity of Publications')
ax.set_title('Quantity of Different Types of Publications Over Years (2010-2019)', pad=20)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

for i in range(len(years)):
    ax.text(i, Books[i]/2, str(Books[i]), ha='center', va='center', color='white')
    ax.text(i, Books[i]+Magazines[i]/2, str(Magazines[i]), ha='center', va='center', color='black')
    ax.text(i, Books[i]+Magazines[i]+Newspapers[i]/2, str(Newspapers[i]), ha='center', va='center', color='white')
    ax.text(i, Books[i]+Magazines[i]+Newspapers[i]+Journals[i]/2, str(Journals[i]), ha='center', va='center', color='black')

plt.tight_layout()
plt.show()