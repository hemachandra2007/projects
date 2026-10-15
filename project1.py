import requests
from bs4 import BeautifulSoup

url = "https://www.thehindu.com/news/national/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

headlines = soup.find_all("h3")

for headline in headlines[:5]:
    print("\n",headline.text)