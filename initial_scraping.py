# import python libraries
 
import requests
from bs4 import BeautifulSoup
#Define the payload for your request execution

url = "http://localhost:8191/v1"
headers = {"Content-Type": "application/json"}
data = {
    "cmd": "request.get",
    "url": "https://www.datanearme.co/",
    "maxTimeout": 60000
}
# structure the payload and make the request call
response = requests.post(url, headers=headers, json=data)

# print the request codes
print("Status:", response.json().get('status', {}))
print("Status Code:", response.status_code)
print("FlareSolverr message:", response.json().get('message', {}))

# parsing logic
page_content = response.json().get('solution', {}).get('response', '')
soup = BeautifulSoup(page_content, 'html.parser')
# Find the div with class 'space-y-3'
target_div = soup.find('div', class_='space-y-3')
# article author
spans = target_div.find_all('span')
span_element = spans[-1]
span_text = span_element.get_text(strip=True)

# article title
h2_element = target_div.find('h2', class_=['font-semibold', 'font-poppins'])
h2_text = h2_element.get_text(strip=True)
print(f"article author: ",span_text, " article title: ", h2_text)
