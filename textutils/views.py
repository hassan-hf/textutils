import os
from django.shortcuts import render
from django.http import HttpResponse

#def index(request):

#    return render(request,"index.html")
#def about(request):
#    return render(request,"index.html")

def index(request):
    return render(request,"index.html" )

def analyze(request):
    dtext= request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')

    if removepunc =='on':
        punctuation= '''!@#$%^&*()_+-=[]\|{};'":<>,./?'''
        analyzed=""
        for char in dtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    elif(fullcaps=='on'):
        analyzed=""
        for char in dtext:
            analyzed =analyzed + char.upper()
        params = {'purpose':'Changed to uppercase', 'analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    elif(newlineremover=='on'):
        analyzed=""
        for char in dtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose':'New line Removed', 'analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    elif(extraspaceremover == 'on'):
        analyzed =""
        for index,char in enumerate(dtext):
            if not(dtext[index]==" " and dtext[index+1]==" "):
                analyzed = analyzed + char
        params={'purpose':'Extra Space Remover','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)


    else:
        return HttpResponse("Error")



def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')

def phone(request):
    return render(request,'phone.html')
def email(request):
    return render(request,'email.html')


