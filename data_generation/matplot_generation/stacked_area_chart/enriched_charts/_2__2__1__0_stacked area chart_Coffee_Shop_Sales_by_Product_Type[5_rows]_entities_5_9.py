
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
streaming_services = [1800, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000]
movies = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300]
concerts = [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350]

plt.figure(figsize=(14, 8))
plt.stackplot(months, streaming_services, movies, concerts, 
              labels=['Streaming Services', 'Movies', 'Concerts'],
              colors=['#5a9bd4', '#ff5733', '#2ecc71'])

plt.title('Monthly Entertainment Expenditure', y=1.02)
plt.xlabel('Month')
plt.ylabel('Expenditure (USD)')
plt.legend(loc='upper right')
plt.xticks(rotation=45)

peak_streaming_sales = max(streaming_services)
peak_month = months[streaming_services.index(peak_streaming_sales)]
plt.annotate(f'Peak Streaming Services Expenditure\n{peak_streaming_sales} USD',
             xy=(peak_month, peak_streaming_sales),
             xytext=(peak_month, peak_streaming_sales + 500),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()