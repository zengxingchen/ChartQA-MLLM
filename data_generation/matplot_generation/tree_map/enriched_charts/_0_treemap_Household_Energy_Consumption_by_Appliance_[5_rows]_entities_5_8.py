
import matplotlib.pyplot as plt
import squarify

# Data
manufacturer = ['Samsung', 'Apple', 'Xiaomi', 'OPPO', 'Vivo', 'Huawei', 'Realme', 'Lenovo', 'Others']
market_share = [21.2, 15.6, 10.8, 8.9, 8.0, 4.3, 3.5, 3.1, 24.6]
color_code = ['#FF5733', '#33FF57', '#3357FF', '#FF33AC', '#FFFF33', '#57FFC7', '#C757FF', '#FFAF33', '#777777']

# Plot
plt.figure(figsize=(12, 8))
squarify.plot(sizes=market_share, label=manufacturer, color=color_code, alpha=0.7)
plt.title('Global Smartphone Market Share by Manufacturer in 2022', fontsize=18)
plt.axis('off')
plt.show()