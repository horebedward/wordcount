from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    fulltext = fulltext.lower()
    count1 = fulltext.split()
    worddictionary = {}
    for word in count1:
        if word in worddictionary:
            worddictionary[word] +=1

        else:
            worddictionary[word] = 1
    sortlist = sorted(worddictionary.items(),key = operator.itemgetter(1),reverse=False)
    return render(request, 'count.html',{'fulltext':fulltext,'count1':len(count1),'worddictionary':sortlist})

def about(request):
    return render(request, 'about.html')