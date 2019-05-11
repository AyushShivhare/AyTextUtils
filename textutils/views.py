# I have created this file -AYUSH

from django.http import HttpResponse
from django.shortcuts import  render
def index(request):
   return render(request,'index.html')
def analyze(request):
    #get the text by form
    djtext=request.POST.get('text','default')

    #check box values
    removepunc=request.POST.get('analyze','off')
    capitalize=request.POST.get('capitalize','off')
    newline=request.POST.get('newline','off')
    space=request.POST.get('space','off')
    count=request.POST.get('count','off')
     # we can do it by off check whether it is off or not

    capitalized = ""
    analyzed=""
    spaced=""
    newlined=""
    str=""
   #check for removepunc
    if removepunc=='on':
    #this is the punctuation list
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        str = str + "removepunc"
        param={'purpose':str,'analyzed_text':analyzed}



    #convert to capital
    if capitalize=='on':

       if removepunc=='off':
           analyzed=djtext
       for char in analyzed:
            capitalized=capitalized+char.upper()
       if str != "":
           str = str + " and convert to capital"
       else:
           str = str + "convert to capital"
       param={'purpose':str,'analyzed_text':capitalized}


    #remove the newline
    if newline=='on':
        if(capitalize=='off'):
            capitalized=analyzed
        if(removepunc=='off'):
            capitalized=djtext
        for char in capitalized:
            if char !="\n" and char !="\r":
                newlined = newlined + char
        if str != "":
            str = str + " and remove newline"
        else:
            str = str + "remove newline"
        param = {'purpose': str, 'analyzed_text': newlined}


    #remove space
    if space=='on':

        if(newline=='off'):
            newlined=capitalized
        if(capitalize=='off'):
            newlined=analyzed
        if(removepunc=='off'):
            newlined=djtext
        for char in newlined:
            if char!=' ':
                spaced = spaced + char
        if str!="":
            str = str + " and remove space"
        else:
            str=str+"remove space"
        param = {'purpose': str, 'analyzed_text': spaced}


    # count the char
    if count=='on':
        countd =0
        for char in djtext:
            countd=countd+1
        param = {'purpose': 'count the character ', 'analyzed_text':countd}

    if(removepunc=='on' or capitalize=='on' or newline=='on' or space=='on' or count=='on'):
        return render(request, 'analyze.html', param)

    return render(request,'index.html');


def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')
