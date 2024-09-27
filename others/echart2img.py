import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from http.server import SimpleHTTPRequestHandler
import socketserver
import threading
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

# 设置文件路径
html_folder_path = r''  # 替换为存放 HTML 文件的文件夹路径
output_folder_path = r''  # 替换为存放输出图片的文件夹路径

# 确保输出文件夹存在
os.makedirs(output_folder_path, exist_ok=True)

# 启动本地HTTP服务器
PORT = 8000
Handler = SimpleHTTPRequestHandler

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

httpd = ThreadedTCPServer(("", PORT), Handler)

def start_server():
    os.chdir(html_folder_path)
    httpd.serve_forever()

thread = threading.Thread(target=start_server)
thread.daemon = True
thread.start()

time.sleep(2)  # 确保服务器已启动

# 启动本地HTTP服务器
server_url = f'http://localhost:{PORT}/'

def process_html_file(filename):
    # 设置 Chrome 浏览器选项
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # 无头模式
    chrome_options.add_argument('--disable-gpu')
    
    # 启动 Chrome 浏览器
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        screenshot_path = os.path.join(output_folder_path, filename.replace('.html', '.png'))
        
        # 如果目标文件已经存在则跳过
        if os.path.exists(screenshot_path):
            print(f"{screenshot_path} 已存在，跳过...")
            return

        file_url = server_url + urllib.parse.quote(filename)
        
        # 打开 HTML 文件
        driver.get(file_url)
        
        # 找到图表容器
        chart = driver.find_element(By.ID, 'container')
        
        # 等待图表完全渲染
        time.sleep(2)  # 可以根据需要调整等待时间
        
        # 获取图表尺寸
        chart_location = chart.location
        chart_size = chart.size
        
        # 设置窗口大小
        window_width = chart_location['x'] + chart_size['width']
        window_height = chart_location['y'] + chart_size['height']
        driver.set_window_size(window_width, window_height)
        
        # 截图
        chart.screenshot(screenshot_path)
        
        # 裁剪图片，去除多余的边框（可选）
        image = Image.open(screenshot_path)
        cropped_image = image.crop((chart_location['x'], chart_location['y'], chart_location['x'] + chart_size['width'], chart_location['y'] + chart_size['height']))
        cropped_image.save(screenshot_path)
    except Exception as e:
        print(f"处理文件 {filename} 时出错: {e}")
    finally:
        # 关闭浏览器
        driver.quit()

# 创建线程池
with ThreadPoolExecutor(max_workers=100) as executor:
    html_files = [f for f in os.listdir(html_folder_path) if f.endswith('.html')]
    executor.map(process_html_file, html_files)

# 关闭 HTTP 服务器
httpd.shutdown()
httpd.server_close()

print("所有 HTML 文件已转换为图片并保存。")
