import requests
import os
from bs4 import BeautifulSoup as bs

def get_bbc_text(url:str) -> list:    
    article = requests.get(url)
    soup = bs(article.content, "html.parser")
    all_text_blocks = soup.find_all("div", {"data-component": "text-block"})
    text = ""

    for text_block in all_text_blocks:
        text += text_block.get_text()
        text += "\n"

    return text

def write_to_file(text:str, filename:str) -> None:
    
    folder_path = 'texts'

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = os.path.join(folder_path, filename)
    with open(filename, "w") as file:
        file.write(text)

def generate_file(url:str, filename:str) -> None:
    text = get_bbc_text(url)
    write_to_file(text, filename)

if __name__ == "__main__":
    url = 'https://www.bbc.co.uk/news/world-europe-49345912'
    generate_file(url, "bbc_text.txt")