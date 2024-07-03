import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
calcium = [120, 115, 130, 140, 135, 145, 150, 155, 160, 150, 140, 135]
protein = [90, 85, 92, 88, 91, 97, 100, 102, 95, 93, 89, 87]
vitamins = [60, 55, 62, 58, 65, 70, 72, 75, 68, 64, 61, 60]
fat = [20, 25, 22, 18, 30, 25, 28, 22, 20, 30, 25, 22]

plt.figure(figsize=(14, 10))
plt.stackplot(months, calcium, protein, vitamins, fat, 
              colors=['#FF6347', '#4682B4', '#FFD700', '#8A2BE2'])

plt.title('Monthly Nutritional Intake', fontdict={'fontsize': 24}, pad=40)
plt.xlabel('Month')
plt.ylabel('Intake (grams)')

peak_protein_month = months[protein.index(max(protein))]
peak_protein_value = max(protein)
plt.text(peak_protein_month, peak_protein_value, 'Peak Protein Intake', ha='center', va='bottom', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

plt.legend(['Calcium', 'Protein', 'Vitamins', 'Fat'], loc='upper left', fontsize=12)
plt.show()