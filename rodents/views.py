from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Cage
from .serializers import CageSerializer
from rest_framework import viewsets


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'rodents/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'rodents/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


def about(request):
    return render(request, 'rodents/about.html', {'title': 'About'})


class CageViewSet(viewsets.ModelViewSet):

    serializer_class = CageSerializer
    queryset = Cage.objects.all()


# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


# class CageListView(ListAPIView):
#     queryset = Cage.objects.all()
#     serializer_class = CageSerializer


# class CageDetailView(RetrieveAPIView):
#     queryset = Cage.objects.all()
#     serializer_class = CageSerializer


# class CageCreateView(CreateAPIView):
#     queryset = Cage.objects.all()
#     serializer_class = CageSerializer


# class CageUpdateView(UpdateAPIView):
#     queryset = Cage.objects.all()
#     serializer_class = CageSerializer


# class CageDestroyView(DestroyAPIView):
#     queryset = Cage.objects.all()
#     serializer_class = CageSerializer
