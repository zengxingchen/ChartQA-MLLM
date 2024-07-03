
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the data table
data = {
    'Company': ['Apple', 'Microsoft', 'Amazon', 'Google', 'Facebook', 'Tesla', 'Berkshire Hathaway', 'Visa', 'JPMorgan Chase', 
                'Johnson & Johnson', 'Walmart', 'Procter & Gamble', 'NVIDIA', 'Mastercard', 'Home Depot', 'Intel', 'Verizon', 'Coca-Cola'],
    'Dividend Yield (%)': [0.6, 0.9, 0, 0, 0, 0, 0, 0.7, 2.3, 2.5, 1.6, 2.3, 0.1, 0.5, 2.2, 2.8, 4.3, 3.1],
    'Stock Price (USD)': [150, 300, 3500, 2800, 325, 1100, 420000, 210, 150, 160, 140, 140, 600, 360, 310, 55, 58, 61],
    'Market Cap (Billion USD)': [2500, 2300, 1600, 1700, 1000, 900, 620, 500, 450, 430, 410, 350, 340, 320, 310, 220, 230, 230]
}

df = pd.DataFrame(data)

# Plotting the bubble chart with customized colors and sizes
plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(
    data=df,
    x="Dividend Yield (%)",
    y="Stock Price (USD)",
    size="Market Cap (Billion USD)",
    sizes=(100, 2000),
    hue="Market Cap (Billion USD)",
    palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
             "#bcbd22", "#17becf", "#9edae5", "#ffbb78", "#98df8a", "#c49c94", "#f7b6d2", "#c5b0d5", "#c7c7c7", "#dbdb8d"],
    alpha=0.8,
    legend=False
)

bubble_chart.set_title("Stock Prices vs. Dividend Yield vs. Market Cap", fontsize=16, pad=20)
bubble_chart.set_xlabel("Dividend Yield (%)", fontsize=12)
bubble_chart.set_ylabel("Stock Price (USD)", fontsize=12)

plt.show()