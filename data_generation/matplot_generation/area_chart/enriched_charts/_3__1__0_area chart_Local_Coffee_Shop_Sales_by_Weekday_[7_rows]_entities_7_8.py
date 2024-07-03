
import matplotlib.pyplot as plt

# Data
years = [
    2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
    2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023
]
funding = [
    150, 160, 170, 185, 195, 210, 225, 240, 260, 280, 
    300, 320, 350, 370, 390, 410, 430, 450, 470, 500, 
    530, 560, 600, 650
]

# Plot
plt.figure(figsize=(14, 10))
plt.fill_between(years, funding, color='#4682B4', alpha=0.7)

# Titles and labels
plt.title('Annual Mental Health Funding', fontsize=20, pad=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Funding (in millions)', fontsize=16)

# Annotations
for i, txt in enumerate(funding):
    plt.annotate(txt, (years[i], funding[i]), textcoords="offset points", xytext=(0, 5), ha='center')

# Display the plot
plt.show()