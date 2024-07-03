import matplotlib.pyplot as plt
import numpy as np

categories = ["Affordable Housing", "Public Transportation", "Green Spaces", "Healthcare Access", 
              "Education Quality", "Job Opportunities", "Crime Rate", "Air Quality", 
              "Internet Access", "Community Engagement"]
urban = [25, 35, 40, 20, 30, 50, 20, 25, 40, 30]
suburban = [45, 50, 35, 50, 40, 30, 40, 35, 45, 40]
rural = [30, 15, 25, 30, 30, 20, 40, 40, 15, 30]

barWidth = 0.85
r = np.arange(len(categories))

plt.figure(figsize=(14, 8))

plt.barh(r, urban, color='#FF5733', edgecolor='white', height=barWidth, label="Urban")
plt.barh(r, suburban, left=urban, color='#33FF57', edgecolor='white', height=barWidth, label="Suburban")
plt.barh(r, rural, left=np.add(urban, suburban), color='#3357FF', edgecolor='white', height=barWidth, label="Rural")

plt.xlabel('Percentage')
plt.title('Community Features in Different Areas')
plt.yticks(r, categories)
plt.legend(loc='lower right')
plt.show()