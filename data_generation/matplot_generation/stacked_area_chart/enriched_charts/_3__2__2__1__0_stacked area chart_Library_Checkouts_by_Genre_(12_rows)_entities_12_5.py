
import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
product_sales = [1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300, 3500, 3700]
service_revenue = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520]
subscription_fees = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320]

fig, ax = plt.subplots(figsize=(18, 10))
ax.stackplot(months, product_sales, service_revenue, subscription_fees, colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

ax.set_title('Monthly Revenue by Category in 2023', fontsize=18, loc='center')
ax.set_ylabel('Revenue (in thousands $)', fontsize=15)
ax.set_xlabel('Month', fontsize=15)
ax.margins(0, 0)

ax.annotate('Peak Product Sales', xy=('December', 3700), xytext=('October', 4000),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.legend(['Product Sales', 'Service Revenue', 'Subscription Fees'], loc='upper left')

plt.show()