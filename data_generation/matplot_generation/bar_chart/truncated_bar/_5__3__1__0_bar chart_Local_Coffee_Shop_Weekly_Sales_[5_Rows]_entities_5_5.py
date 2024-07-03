
import matplotlib.pyplot as plt

categories = ["North America", "Europe", "Asia", "South America", "Africa", "Australia", "Antarctica"]
percentages = [24.0, 20.0, 18.0, 12.0, 10.0, 9.0, 7.0]

plt.figure(figsize=(10, 12))

plt.bar(categories, percentages, color=['#FF5733', '#3375FF', '#FFC300', '#8E33FF', '#FF33AB', '#57C785', '#D733FF'], width=0.5)

plt.ylabel('Percentage of Population', fontsize=14)
plt.title('Continental Population Distribution', fontsize=18, pad=20)
plt.ylim(5, 30)

plt.tight_layout()
plt.show()