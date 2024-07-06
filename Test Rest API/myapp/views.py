from django.shortcuts import render,redirect
import requests

# Create your views here.
def index(request):
	if request.method=="POST":
		url = "http://localhost:8001/api/books"
		querystring = {
			'title':request.POST['title'],
			'author':request.POST['author'],
			'isbn':request.POST['isbn'],
			'publisher':request.POST['publisher'],
			}
		response = requests.post(url,json=querystring)
		print(response.text)
		return redirect('fetch-data')
	else:
		return render(request,'index.html')

def fetch_data(request):
	url = "http://localhost:8001/api/books"
	response = requests.get(url)
	data=response.json()
	l=[]
	for i in data:
		#l1=[]
		#l1.append(i['id'])
		#l1.append(i['title'])
		#l1.append(i['author'])
		#l1.append(i['isbn'])
		#l1.append(i['publisher'])
		#l.append(l1)
		l.append(i)
	print(l)
	msg="Data fetched Successfully"
	return render(request,'index.html',{'l':l})
