import requests
from bs4 import BeautifulSoup
import csv

base_url = 'https://boxnovel.com/novel/outside-of-time/'

def get_soup():
    response = requests.get(base_url)
    # print(response.text)
    return BeautifulSoup(response.text, 'html.parser')

data = get_soup()
# new_data = data.find('div', class_='post-title')
# print(data)

# novel_list = []

# # Scrape novels and their latest chapters
# page = 1
# while True:
#     url = f'{base_url}/page/{page}'
#     soup = get_soup(url)
    
#     novels = soup.find_all('div', class_='novel-info')
#     if not novels:
#         break
    
#     for novel in novels:
#         title = novel.find('h2').text
#         latest_chapter = novel.find('a', class_='latest-chapter').text
#         chapter_link = novel.find('a', class_='latest-chapter')['href']
        
#         # Navigate to the latest chapter page
#         chapter_soup = get_soup(chapter_link)
#         chapter_content = chapter_soup.find('div', class_='chapter-content').text
        
#         novel_list.append([title, latest_chapter, chapter_content])
    
#     page += 1

# # Save the data to a CSV file
# with open('novels.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Title', 'Latest Chapter', 'Content'])
#     writer.writerows(novel_list)
