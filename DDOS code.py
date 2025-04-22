

import requests
import threading

# Target (for testing, use localhost)
url = "http://localhost:8000"

# Function to send continuous requests
def send_requests():
    while True:
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
        except:
            print("Server might be down or refusing connection")

# Launch multiple threads to simulate heavy traffic
for i in range(50):  # You can increase this number for more load
    thread = threading.Thread(target=send_requests)
    thread.start()

