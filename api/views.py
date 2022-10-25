from django.shortcuts import render
from .forms import CommentForm
from .models import Comment

# Create your views here.
def home (request):
    message = 'Veuillez saisir votre commentaire.'
    data = Comment.objects.all().values()
    context = {'form' : CommentForm, 'message' : message, 'data' : data}
    return render(request, 'index.html', context)

