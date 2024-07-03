
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Occupation': ['Healthcare Workers', 'Teachers', 'Software Engineers', 'Construction Workers',
                   'Retail Workers', 'Lawyers', 'Artists', 'Musicians',
                   'Scientists', 'Writers', 'Athletes', 'Journalists',
                   'Finance Professionals', 'Sales Representatives', 'Government Employees',
                   'IT Technicians', 'Marketing Professionals', 'Engineers'],
    'Average Sleep Hours': [6.5, 7.2, 7.0, 6.8, 6.9, 6.4, 7.5, 7.1, 7.3, 7.6, 8.0, 6.7, 6.6, 6.9, 7.0, 7.1, 7.2, 6.8]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", 
          "#c4e17f", "#76d7c4", "#ff6f61", "#6b5b95", "#d64161", "#feb236",
          "#ff7b25", "#d1c4e9", "#f6abb6", "#6a0dad", "#ffdf00", "#ff4500"]
squarify.plot(sizes=df['Average Sleep Hours'], label=df['Occupation'], alpha=0.8, color=colors)
plt.title('Average Hours of Sleep per Night by Occupation in 2024', fontsize=16, fontweight='bold')
plt.axis('off')
plt.show()