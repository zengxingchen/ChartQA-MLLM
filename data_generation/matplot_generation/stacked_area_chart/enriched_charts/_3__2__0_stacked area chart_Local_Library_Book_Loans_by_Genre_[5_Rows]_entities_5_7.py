
import matplotlib.pyplot as plt

years = list(range(2011, 2022))
protein = [55, 57, 60, 62, 65, 68, 70, 73, 75, 78, 80]
carbohydrates = [120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170]
fats = [30, 32, 35, 37, 40, 42, 45, 47, 50, 52, 55]

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(years, protein, carbohydrates, fats, colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

ax.annotate('Increase in Protein Intake', xy=(2018, 73), xytext=(2014, 90),
            arrowprops=dict(facecolor='#1f77b4', shrink=0.05))

plt.xlabel('Year')
plt.ylabel('Nutrient Intake (g)')
plt.title('Annual Nutrient Intake (2011-2021)', pad=20)

plt.legend(['Protein', 'Carbohydrates', 'Fats'], loc='upper left')
plt.show()