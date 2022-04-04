from tkinter import messagebox
from django.shortcuts import render
import random

# first view
def Main_Page(request):
    return render(request, 'Main_page.html')

# result view
def Result_page(request):
    try : 
    #random output
        games=request.GET['lotto_game']
        game_count=int(games)
        lottoList=[[] for row in range(0,game_count)]

        for i in range(0,game_count):
            for a in range(0,6):
                num=random.randint(1,46)
                lottoList[i].append(num)
            del num

# Response
        return render (request,'Result_page.html',{"count": game_count, 'random_list' : lottoList })

    except ValueError :
        return render(request, 'Main_page.html')