import requests
import os
from words import w_questions
import re

class Text_without_words:
    def __init__(self, text_without_words, list_of_removed_words):
        self.text_without_words =  text_without_words
        self.list_of_removed_words = list_of_removed_words

    def get_text_without_words(self):
        return self.text_without_words
    
    def get_list_of_words(self):
        return self.list_of_removed_words

def get_text(filename):
    folder_path = 'texts'

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = os.path.join(folder_path, filename)

    with open(filename, "r") as file:
        text = file.read()
    return text

def number_the_empty_spaces(text):
    counter = 1

    pattern = re.compile(r'_+')

    def replacement(match):
        nonlocal counter
        result = f' {counter}.{"_" * len(match.group())}'
        counter += 1
        return result

    # Use the sub() function with the replacement function
    result_string = pattern.sub(replacement, text)

    return result_string

def remove_words(text, words):
    list_of_words = text.split(" ")
    for w in list_of_words:
        if w in words:
            text = text.replace(" " + w + " ", "._______ ")


    # for word in words:
    #     text = text.replace(" " + word + " ", " " + str(counter)+ "._______ ")
    #     counter += 1
    return number_the_empty_spaces(text)

def divide_paragraphs(text):
    list_of_strings = text.split("\n")

    for l in list_of_strings:
        print(l)
        print("STOP")

def generate_list_of_words(text, words):
    list_of_words = []

    list_from_text = text.split(" ")
    for w in list_from_text:
        if w in words:
            list_of_words.append(w)

    return list_of_words

def generate_text_without_words(name):
    text = get_text(name)
    list = w_questions()  
    list_of_removed_words = generate_list_of_words(text, list)  

    return Text_without_words(remove_words(text, list), list_of_removed_words)

def check_input(list_of_words):
    print("Write the words that are missing")
    counter = 1
    for word in list_of_words:
        user_input = input(str(counter) + ". ")
        if user_input == word:
            print("Correct")
        else:
            print("Incorrect")
            print("The correct word is: " + word)
        counter += 1

def run_use_of_language(name):
    text = generate_text_without_words(name)
    print(text.get_text_without_words())
    check_input(text.get_list_of_words())

def generate_text(name):
    text = get_text(name)
    list = w_questions()
    text = remove_words(text, list)
    print(text)
    # divide_paragraphs(text)

if __name__ == "__main__":
    # generate_text("bbc_text.txt")
    run_use_of_language("bbc_text.txt")
