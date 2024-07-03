
import matplotlib.pyplot as plt

# Data
years = [
    2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
    2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023
]
funding = [
    150, 165, 180, 200, 220, 245, 270, 295, 325, 355, 
    385, 420, 455, 490, 530, 570, 610, 650, 690, 735, 
    780, 830, 880, 935
]

# Plot
plt.figure(figsize=(16, 8))
plt.fill_between(years, funding, color='#FF6347', alpha=0.6)

# Titles and labels
plt.title('Annual AI Research Funding', fontsize=22, pad=30)
plt.xlabel('Year', fontsize=18)
plt.ylabel('Funding (in millions)', fontsize=18)

# Annotations
for i, txt in enumerate(funding):
    plt.annotate(txt, (years[i], funding[i]), textcoords="offset points", xytext=(0, 5), ha='center')

# Display the plot
plt.show()