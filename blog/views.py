from django.shortcuts import render

posts = [
	{
		'author': 'Chuks Onye',
		'title': 'Blog post 1',
		'content': 'First post content',
		'date_posted': 'August 10 2020',
	},
	{
		'author': 'Chuks Onye2',
		'title': 'Blog post 2',
		'content': 'Second post content',
		'date_posted': 'August 19 2020',
	},
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})

