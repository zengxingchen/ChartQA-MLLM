
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Sector': ['Healthcare', 'Technology', 'Finance', 'Energy', 'Real Estate', 'Transportation', 
               'Consumer Goods', 'Industrial', 'Telecommunications', 'Utilities', 'Agriculture', 
               'Education', 'Entertainment', 'Manufacturing', 'Aerospace', 'Retail', 
               'Pharmaceuticals', 'Hospitality', 'Automotive', 'Construction', 'Mining', 
               'Chemical', 'Food & Beverages', 'Wellness', 'Sports', 'Personal Care', 
               'Public Services', 'Insurance', 'Media'],
    'Amount (Billions)': [480.5, 390.4, 310.3, 290.2, 260.1, 230.0, 
                          210.6, 190.5, 170.4, 150.3, 130.2, 110.1, 
                          100.0, 90.7, 80.4, 70.3, 60.2, 50.1, 40.0, 
                          30.9, 20.8, 15.6, 10.4, 8.2, 6.5, 4.3, 3.1, 
                          2.9, 1.7]
}

df = pd.DataFrame(data)

# Color scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', '#FFA133', 
          '#33A1FF', '#A1FF33', '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', 
          '#A133FF', '#FFA133', '#33A1FF', '#A1FF33', '#FF5733', '#33FF57', '#3357FF', 
          '#FF33A1', '#33FFA1', '#A133FF', '#FFA133', '#33A1FF', '#A1FF33', '#FF5733', 
          '#33FF57']

# Plotting the Treemap
plt.figure(figsize=(20, 12))  # Change width and height reasonably
squarify.plot(sizes=df['Amount (Billions)'], label=df['Sector'], color=colors, alpha=0.8)
plt.title('Investment in Various Sectors - 2023 (Billions USD)', fontsize=20, fontweight='bold', y=1.05)
plt.axis('off')
plt.show()