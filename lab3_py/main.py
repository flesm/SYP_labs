# https://baskino.org/
# https://kinogo.pro/

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", category=UserWarning)


# Вяртае змест вэб-старонкі па зададзеным URL.
def get_page_content(url):
    response = requests.get(url)
    return response.text


# Падлічвае колькасць спасылак і словаў на вэб-старонцы.
def count_links_and_words(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = len(soup.find_all('a'))
    words = len(soup.get_text().split())
    return links, words


# Будуе гістаграму частаты сустракаемасці сімвалаў ў зададзеным слове.
def plot_character_frequency(text):
    char_freq = {char: text.count(char) for char in set(text)}
    plt.bar(char_freq.keys(), char_freq.values())
    plt.title(f"Частата сустракаемасці сімвалаў на сайце")
    plt.show()


# Будуе гістаграму частаты сустракаемасці даўжыняў словаў у зададзеным тэксце.
def plot_word_length_frequency(text):
    word_lengths = [len(word) for word in text.split() if len(word) >= 7]
    plt.hist(word_lengths, bins=range(7, max(word_lengths) + 2), align='left', rwidth=0.8)
    plt.title("Частата сустракаемасці даўжынь словаў")
    plt.xlabel("Даўжыня словаў")
    plt.ylabel("Частата")
    plt.show()


# Падлічвае колькасць малюнкаў на вэб-старонцы.
def count_images(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    images = len(soup.find_all('img'))
    return images


# Падлічвае агульны і сярэдні памер малюнкаў на вэб-старонцы.
def get_image_sizes(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    images = soup.find_all('img')
    total_size = 0
    for image in images:
        total_size += int(image['width']) * int(image['height'])
    average_size = total_size / len(images) if len(images) > 0 else 0
    return total_size, average_size


# Падлічвае колькасць загалоўкаў розных узроўняў на вэб-старонцы.
def count_headings(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    headings = {}
    for level in range(1, 7):  # Заголовки обычно от h1 до h6
        count = len(soup.find_all(f'h{level}'))
        headings[f'h{level}'] = count
    return headings


# Будуе гістаграму частаты сустракаемасці даўжынь слоў у загалоўках на вэб-старонцы.
def plot_heading_word_length_frequency(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    headings_text = ' '.join([heading.get_text() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])])
    word_lengths = [len(word) for word in headings_text.split()]
    plt.hist(word_lengths, bins=range(1, max(word_lengths) + 2), align='left', rwidth=0.8)
    plt.title("Частата сустракання даўжынь словаў у загалоўках")
    plt.xlabel("Даўжыня словаў")
    plt.ylabel("Частата")
    plt.show()


url = input("Увядзіце URL старонкі: ")

html_content = get_page_content(url)
links, words = count_links_and_words(html_content)
images = count_images(html_content)
total_size, average_size = get_image_sizes(html_content)
headings_count = count_headings(html_content)

print(f"Колькасць спасылак на старонцы: {links}")
print(f"Колькасць словаў на старонцы: {words}")
print(f"Колькасць малюнкаў на старонцы: {images}")
print(f"Агульны памер малюнкаў на старонцы: {total_size}")
print(f"Сярэдні памер малюнкаў на старонцы: {average_size}")
for heading, count in headings_count.items():
    print(f"Колькасць загалоўкаў {heading}: {count}")

text = BeautifulSoup(html_content, 'html.parser').get_text()
plot_character_frequency(text)
plot_word_length_frequency(text)
plot_heading_word_length_frequency(html_content)
