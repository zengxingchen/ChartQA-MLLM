
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Sector': ['Healthcare', 'Technology', 'Finance', 'Energy', 'Real Estate', 'Transportation', 
               'Consumer Goods', 'Industrial', 'Telecommunications', 'Utilities', 'Agriculture', 
               'Education', 'Entertainment', 'Manufacturing', 'Aerospace', 'Retail', 
               'Pharmaceuticals', 'Hospitality', 'Automotive', 'Construction', 'Mining', 
               'Chemical', 'Food & Beverages'],
    'Amount (Billions)': [450.5, 380.4, 320.3, 275.2, 245.1, 220.0, 
                          200.6, 185.5, 160.4, 140.3, 120.2, 105.1, 
                          95.0, 85.7, 75.4, 65.3, 55.2, 45.1, 35.0, 
                          25.9, 15.8, 10.6, 5.4]
}

df = pd.DataFrame(data)

# Color scheme
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6',
          '#c2f0c2','#ff6666','#6666ff','#66ff66','#ffb366','#ff66b3',
          '#9999ff','#66ffb3','#ffb3b3','#99b3ff','#b3ff66','#ff9999',
          '#99ff66','#66ff99','#ff99b3','#99b3ff','#b366ff']

# Plotting the Treemap
plt.figure(figsize=(18, 10))  # Change width and height reasonably
squarify.plot(sizes=df['Amount (Billions)'], label=df['Sector'], color=colors, alpha=0.8)
plt.title('Investment in Various Sectors - 2021 (Billions USD)', fontsize=18, fontweight='bold', y=1.05)
plt.axis('off')
plt.show()