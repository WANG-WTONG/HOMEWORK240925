import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt

url = 'https://datatopics.worldbank.org/debt/ids/countryanalytical/CHN?_gl=1*1cnm8fd*_gcl_au*NDI4NTcyNzcyLjE3MjcwODA0NDc.'
response = requests.get(url)

if response.ok:
    print("OK")
else:
    print(f"FALSE，CODE：{response.status_code}")

content = response.text
soup = bs(content, "html.parser")

all_spacer2 = soup.findAll("div", attrs={"class": "spacer2"})

data = []
for spacer2 in all_spacer2[:11]:
    spacer22 = spacer2.get_text(strip=True)
    if spacer22:
        
        try:
            value = float(spacer22.replace(',', ''))
            data.append(value)
        except ValueError:
            print(f"WRONG：{spacer22}")


start_year = 2012
x_labels = [str(year) for year in range(start_year, start_year + len(data))]

plt.figure(figsize=(8, 6))
plt.plot(x_labels, data, marker='o', linestyle='-', color='b', label='Debt Value')
plt.title('Total External Debt Stocks')
plt.xlabel('Year')
plt.ylabel('Debt Value (in millions USD)')

plt.xticks(rotation=45)

plt.legend()

plt.tight_layout()

plt.show()
