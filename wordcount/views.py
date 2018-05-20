from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'message':'Hola que tal!'})
#    return HttpResponse('Hello')

def count(request):
    fulltext = request.POST['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    sortedWords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {
        'fulltext':fulltext,
        'wordcount':len(wordlist),
        'worddict':worddict,
        'sortedWords':sortedWords})

def about(request):
    return render(request, 'about.html')
