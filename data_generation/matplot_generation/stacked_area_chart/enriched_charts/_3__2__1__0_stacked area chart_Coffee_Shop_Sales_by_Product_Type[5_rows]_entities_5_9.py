
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
protein = [50, 52, 55, 58, 60, 62, 65, 67, 70, 72, 75, 78]
carbohydrates = [30, 32, 35, 37, 40, 42, 45, 47, 50, 52, 55, 58]
fat = [20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45, 48]

plt.figure(figsize=(14, 8))
plt.stackplot(months, protein, carbohydrates, fat, 
              labels=['Protein', 'Carbohydrates', 'Fat'],
              colors=['#ff9999', '#66b3ff', '#99ff99'])

plt.title('Monthly Nutrient Intake Breakdown', y=1.02)
plt.xlabel('Month')
plt.ylabel('Nutrient Intake (g)')
plt.legend(loc='upper left')
plt.xticks(rotation=45)

peak_protein = max(protein)
peak_month = months[protein.index(peak_protein)]
plt.annotate(f'Peak Protein Intake\n{peak_protein} g',
             xy=(peak_month, peak_protein),
             xytext=(peak_month, peak_protein + 10),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()