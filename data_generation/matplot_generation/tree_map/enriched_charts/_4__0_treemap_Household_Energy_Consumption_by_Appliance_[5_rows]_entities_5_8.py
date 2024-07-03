
import matplotlib.pyplot as plt
import squarify

# Data
source = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass', 'Ocean', 'Nuclear', 'Natural Gas', 'Coal', 'Oil']
production = [18.0, 15.0, 12.5, 5.5, 9.0, 3.0, 10.5, 11.5, 15.0, 0.5]
color_code = ['#FFA07A', '#20B2AA', '#778899', '#DDA0DD', '#66CDAA', '#FF4500', '#2E8B57', '#8A2BE2', '#D2691E', '#FF6347']

# Plot
plt.figure(figsize=(14, 10))
squarify.plot(sizes=production, label=source, color=color_code, alpha=0.8)
plt.title('Global Renewable Energy Production by Source in 2023', fontsize=20, pad=20)
plt.axis('off')
plt.show()