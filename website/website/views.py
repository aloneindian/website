from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request, 'home.html')

def count(request):
	data= request.GET['textname']
	data_list=data.split()
	data_len= len(data_list)
	print(data_len)
	worddict = {}
	for word in data_list:
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1
	sorted_list = sorted(worddict.items(), key=operator.itemgetter(1),reverse= True)
	return render(request,'count.html',{'textn':data, 'words':data_len, "dict":sorted_list})
