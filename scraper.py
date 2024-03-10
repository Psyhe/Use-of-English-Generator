import requests
import os
from bs4 import BeautifulSoup as bs

def write_to_file(text:str, filename:str) -> None:
    
    folder_path = 'texts'

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = os.path.join(folder_path, filename)
    with open(filename, "w") as file:
        file.write(text)

def get_bbc_text(url:str) -> list:    
    article = requests.get(url)
    soup = bs(article.content, "html.parser")
    all_text_blocks = soup.find_all("div", {"data-component": "text-block"})

    title_block = soup.find("h1", {"class": "ssrcss-fmi64d-StyledHeading e10rt3ze0"})

    text = ""

    for text_block in all_text_blocks:
        text += text_block.get_text()
        text += "\n"

    write_to_file(text, title_block.get_text() + ".txt")

if __name__ == "__main__":
    url = input("Enter the URL of the article: ")
    get_bbc_text(url)