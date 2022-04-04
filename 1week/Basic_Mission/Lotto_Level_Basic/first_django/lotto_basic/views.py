from django.shortcuts import render
import random

# first view
def Main_Page(request):

#random output
    lottoList=list()
    
    for a in range(0,6):
        num=random.randint(1,46)
        lottoList.append(num)
        del num


# Response
    return render (request,'Main_page.html',{'random_list' : lottoList })