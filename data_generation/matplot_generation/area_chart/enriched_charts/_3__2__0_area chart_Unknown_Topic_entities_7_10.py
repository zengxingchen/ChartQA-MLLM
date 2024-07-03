
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Date": pd.date_range(start="2023-01-01", end="2023-01-31"),
    "Stock_Price": [
        150, 152, 153, 155, 158, 160, 159, 161, 162, 164, 167, 170, 165, 168, 172, 
        175, 178, 176, 179, 181, 185, 188, 190, 192, 194, 195, 193, 191, 189, 187, 190
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df["Date"], df["Stock_Price"], color='#ff6600')

plt.title('Daily Stock Prices in January', fontsize=18, loc='left', pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Stock Price ($)', fontsize=14)

for i, price in enumerate(df["Stock_Price"]):
    plt.text(df["Date"][i], price + 1, str(price), ha='center', va='bottom', fontsize=9)

plt.grid(True, color='#d9d9d9', linestyle='-', linewidth=0.8, which='both')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()