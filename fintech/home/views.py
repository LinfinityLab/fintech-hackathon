from django.shortcuts import render
import nltk
from nltk import word_tokenize, pos_tag
import string

# Create your views here.

def index(request):
    template_name = "home/index.html"
    nlp("What is the value of Apple stock?")
    return render(request, template_name)

def nlp(text):
    valid_letters = string.letters + ' '
    stripped_text = ''.join([char if char in valid_letters else '' for char in text])
    tokens = word_tokenize(stripped_text)
    tags = pos_tag(tokens)
    print stripped_text
    print tokens
    print tags
