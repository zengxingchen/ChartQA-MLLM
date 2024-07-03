
import matplotlib.pyplot as plt

# Data
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
         2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
         2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
visitors = [150, 160, 180, 190, 210, 230, 250, 270, 300, 320, 
            340, 360, 380, 400, 420, 450, 470, 490, 510, 530, 
            550, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760]

plt.figure(figsize=(16, 8))

# Area chart
plt.fill_between(years, visitors, color='#8A2BE2', alpha=0.6)

# Headline and labels
plt.title('Annual Visitors to National Park', fontsize=18, pad=25)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Visitors (in thousands)', fontsize=14)

# Annotations
plt.annotate('Significant Increase in Tourism', xy=(2021, 580), xytext=(2015, 400),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

# Show plot
plt.show()