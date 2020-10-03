# project name - Text utilities.
# creator - Nithish vasala
# date - 02/sep/2020

from django.http import HttpResponse
from django.shortcuts import render
import base64

def index2(request):
    return render(request, 'index2.html')


def about(request):
    return render(request, 'about.html')
   

def contactus(request):
    return render(request, 'contactus.html')
   
def services(request):
    new_text = request.POST.get('text1','default')
    print(new_text)
    remove_punc = request.POST.get('remove_punc', 'default')
    print(remove_punc)
    UpperCase = request.POST.get('UpperCase','default')
    print(UpperCase)
    newline_remover = request.POST.get('newline_remover','default')
    print(newline_remover)
    extra_space_remover = request.POST.get('extra_space_remover','default')
    print(extra_space_remover)
    char_counter = request.POST.get('char_counter','default')
    print(char_counter)
    font_increase = request.POST.get('font_increase','default')
    print(font_increase)

    if remove_punc == 'on':
        analyzed = ""
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in new_text:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {'purpose' : '''Punctuation's Removed''', 'analyzed_text' : analyzed}
        new_text = analyzed
        #return render(request, 'analyze2.html', params)
    
    if(UpperCase == "on"):
        analyzed = ""
        for char in new_text:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Convert to UPPERCASE', 'analyzed_text' : analyzed}
        new_text = analyzed
        #return render(request, 'analyze2.html', params)
    
    if(newline_remover == "on"):
        analyzed = ""
        for char in new_text:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose' : 'New Line Remover', 'analyzed_text' : analyzed}
        new_text = analyzed
        #return render(request, 'analyze2.html', params)
    
    if(extra_space_remover == "on"):
        analyzed = ""
        analyzed = " ".join(new_text.split())
        params = {'purpose' : 'Extra space remover', 'analyzed_text' : analyzed}
        new_text = analyzed
        #return render(request, 'analyze2.html', params)

    if(char_counter == "on"):
        analyzed = ""
        count = 0
        for char in new_text:
            if char !=" " or char ==" ":
                count = count + 1
                analyzed = count
        params = {'purpose' : 'Character Counter in the string', 'analyzed_text' : analyzed}

    if (font_increase == "on"):
        analyzed = ""
        analyzed = base64.b64encode(new_text.encode('utf-8',errors = 'strict'))
        params = {'purpose': 'Font size Increase', 'analyzed_text': analyzed}
        new_text = analyzed

    if( remove_punc !='on' and UpperCase != "on" and newline_remover !="on" and extra_space_remover !="on" and char_counter != "on" and font_increase !="on"):
        return render(request, 'services.html')

    return render(request, 'analyze2.html', params)

