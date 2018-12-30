from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


def index(request):




    response_arma= requests.get('https://steamcharts.com/app/107410')
    response_forhonor = requests.get('https://steamcharts.com/app/304390')


    soup = BeautifulSoup(response_arma.text, "html.parser")
    numbers_arma = soup.find('span', class_='num').get_text()


    soup = BeautifulSoup(response_forhonor.text, 'html.parser')
    numbers_forhonor = soup.find('span', class_='num').get_text()

    content = {'numbers_forhonor' : numbers_forhonor, 'numbers_arma' : numbers_arma}
    return render(request, 'roast/index.html', content)