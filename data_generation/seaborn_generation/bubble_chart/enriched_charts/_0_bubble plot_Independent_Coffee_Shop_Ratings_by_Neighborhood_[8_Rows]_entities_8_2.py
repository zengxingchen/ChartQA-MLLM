
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the data table
data = {
    'Model': ['Accord', 'Civic', 'Camry', 'Corolla', 'Mustang', 'Charger', 'Challenger', 'Impreza',
              'Forester', 'Tucson', 'CX-5', 'Rav4', 'WRX', 'Altima', 'Maxima', 'Supra', 'Miata'],
    'Fuel Efficiency (mpg)': [30, 35, 28, 32, 20, 22, 21, 25, 26, 29, 27, 30, 24, 32, 24, 22, 35],
    'Price (USD)': [24000, 20000, 28000, 19000, 35000, 32000, 33000, 27500, 31000, 27000, 26000, 29000,
                    32000, 23000, 36000, 50000, 18000],
    'Engine Power (hp)': [190, 180, 200, 170, 450, 410, 485, 152, 182, 161, 187, 176, 268, 182, 300,
                          382, 155]
}

df = pd.DataFrame(data)

# Plotting the bubble chart with customized colors and sizes
plt.figure(figsize=(10, 6))
bubble_chart = sns.scatterplot(
    data=df,
    x="Fuel Efficiency (mpg)",
    y="Price (USD)",
    size="Engine Power (hp)",
    sizes=(100, 1000),
    hue="Engine Power (hp)",
    palette=["#2ecc71", "#3498db", "#e74c3c", "#f1c40f", "#9b59b6", "#34495e", "#95a5a6", "#1abc9c",
             "#d35400", "#7f8c8d", "#bdc3c7", "#16a085", "#27ae60", "#2980b9", "#8e44ad", "#2c3e50", "#f39c12"],
    alpha=0.7,
    legend=False
)

bubble_chart.set_title("Car Models: Fuel Efficiency vs Price vs Engine Power")
bubble_chart.set_xlabel("Fuel Efficiency (mpg)")
bubble_chart.set_ylabel("Price (USD)")

plt.show()