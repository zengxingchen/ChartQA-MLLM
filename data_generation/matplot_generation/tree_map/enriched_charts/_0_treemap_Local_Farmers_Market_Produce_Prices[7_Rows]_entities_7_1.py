
import matplotlib.pyplot as plt
import squarify

# Data points
brands = ['Samsung', 'Apple', 'Xiaomi', 'OPPO', 'Vivo', 'Motorola', 'Lenovo', 'LG', 'Realme', 
          'Huawei', 'OnePlus', 'Sony', 'Nokia', 'Google', 'Asus', 'Tecno', 'Alcatel', 'ZTE', 'HTC', 'Others']
market_share = [21.2, 15.6, 9.7, 9.3, 7.9, 5.8, 4.2, 3.1, 3.0, 2.9, 2.7, 2.3, 2.2, 1.6, 1.4, 1.3, 1.1, 0.9, 0.6, 10.1]

# Color scheme
colors = ['#FF6347', '#FFD700', '#FF8C00', '#FF4500', '#008000', '#00BFFF', '#1E90FF', '#0000FF',
          '#4B0082', '#9400D3', '#FF1493', '#FFB6C1', '#48D1CC', '#708090', '#2F4F4F', '#F0E68C',
          '#FFFACD', '#FFE4E1', '#EEE8AA', '#D3D3D3']

plt.figure(figsize=(12, 8))
squarify.plot(sizes=market_share, label=brands, color=colors, alpha=0.7)

# Chart details
plt.title('Global Smartphone Market Share in 2023')
plt.axis('off')

plt.show()