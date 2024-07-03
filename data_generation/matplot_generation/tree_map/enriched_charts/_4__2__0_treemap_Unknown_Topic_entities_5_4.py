
import matplotlib.pyplot as plt
import squarify

# Data
categories = [
    'Cardiovascular Health', 'Mental Wellness', 'Nutrition', 'Sleep Science', 
    'Physical Fitness', 'Public Health', 'Neuroscience', 'Addiction & Recovery', 
    'Reproductive Health', 'Child Development', 'Gerontology', 'Epidemiology', 
    'Immunology', 'Genetics', 'Healthcare Innovation', 'Social Determinants', 
    'Disease Prevention', 'Patient Advocacy', 'Health Policy', 'Biomedical Research'
]
revenue = [
    15000, 12000, 13000, 10000, 17000, 14000, 11000, 9000, 16000, 8000, 7000, 6000, 
    5000, 4000, 3000, 2000, 18000, 9000, 4000, 1500
]

# Colors
colors = [
    '#D32F2F', '#C2185B', '#7B1FA2', '#512DA8', '#303F9F', '#1976D2', '#0288D1', 
    '#0097A7', '#00796B', '#388E3C', '#689F38', '#AFB42B', '#FBC02D', '#FFA000', 
    '#F57C00', '#E64A19', '#5D4037', '#616161', '#455A64', '#1B5E20'
]

plt.figure(figsize=(20, 12))

# Treemap
squarify.plot(sizes=revenue, label=categories, color=colors, alpha=0.8)

plt.title('Health & Psychology: Key Areas of Research and Interest', fontsize=20, pad=20)

# Removing axes
plt.axis('off')

# Display the plot
plt.show()