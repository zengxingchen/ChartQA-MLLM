
import matplotlib.pyplot as plt
import numpy as np

categories = ["Affordable Housing", "Public Transportation", "Green Spaces", "Healthcare Access", 
              "Education Quality", "Job Opportunities", "Crime Rate", "Air Quality", 
              "Internet Access", "Community Engagement"]
urban = [28, 42, 35, 20, 35, 50, 15, 25, 30, 40]
suburban = [37, 48, 30, 40, 40, 25, 35, 30, 50, 40]
rural = [35, 10, 35, 40, 25, 25, 50, 45, 20, 20]

barWidth = 0.85
r = np.arange(len(categories))

plt.figure(figsize=(10, 16))

plt.bar(r, urban, color='#1f77b4', edgecolor='white', width=barWidth, label="Urban")
plt.bar(r, suburban, bottom=urban, color='#ff7f0e', edgecolor='white', width=barWidth, label="Suburban")
plt.bar(r, rural, bottom=np.add(urban, suburban), color='#2ca02c', edgecolor='white', width=barWidth, label="Rural")

plt.ylabel('Percentage')
plt.title('Resource Availability in Different Areas')
plt.xticks(r, categories, rotation=90)
plt.legend(loc='upper right')
plt.show()