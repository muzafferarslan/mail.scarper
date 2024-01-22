import requests
from bs4 import BeautifulSoup

def find_all_links(url):
  # Web sitesinin HTML kodunu al
  response = requests.get(url)
  html = response.text
  # HTML kodunu ayrıştır
  soup = BeautifulSoup(html, "html.parser")
  # Tüm bağlantıları bul
  links = soup.find_all("a")
  # Bağlantıların URL'lerini listeye ekle
  links_list = []
  for link in links:
    links_list.append(link["href"])
  # Bulunan bağlantıların listesini döndür
  return links_list

def find_all_mails(links):
  # E-posta adreslerinin listesi
  mails_list = []
  for link in links:
    if link.startswith("https://ostimteknopark.com.tr/tr/company/firmalar-119/"):
      # Bağlantının HTML kodunu al
      response = requests.get(link, timeout=5)
      html = response.text

      # HTML kodunu ayrıştır
      soup = BeautifulSoup(html, "html.parser")

      # E-posta adreslerini bul
      mails = soup.find_all("a", href=lambda href: href and "mailto:" in href)

      # E-posta adreslerini listeye ekle
      for mail in mails:
        mails_list.append(mail["href"].replace("mailto:", ""))  # Bulunan e-posta adreslerinin listesini döndür
  return mails_list

# Örnek kullanım
url = "https://ostimteknopark.com.tr/tr/firmalar-119"
links = find_all_links(url)
mails = find_all_mails(links)

# Bulunan e-posta adreslerini yazdır
for mail in mails:
  print(mail)
