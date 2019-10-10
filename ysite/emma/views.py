from django.shortcuts import render

# Create your views here.
def main_page(request):
	return render(request, 'emma/main_page.html', {})

def js_page(request):
	return render(request, 'emma/js_page.html', {})