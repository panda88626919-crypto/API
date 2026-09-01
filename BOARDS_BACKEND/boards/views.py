from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.db.models import Count
from rest_framework.views import APIView
from .serializers import BoardsSerializer, TopicSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
# Create your views here.

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardsSerializer




# def boards_list(requests):
#     boards = Board.objects.all()
#     data = {'Results':list(boards.values("pk", "name", "description"))}
#     return JsonResponse(data)

# class BoardList(generics.ListCreateAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardsSerializer


# class BoardList(APIView):
#     def get(self, request):
#         boards = Board.objects.all()
#         data = BoardsSerializer(boards, many=True).data
#         return Response(data)

#     def post(self, request):
#         serializer = BoardsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardTopics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'id'

# class BoardTopics(APIView):
#     def get(self, request, board_id):
#         board = get_object_or_404(Board, pk=board_id)
#         topics = board.topics.order_by('-created_dt').annotate(comments = Count('posts'))
#         data = TopicSerializer(topics, many=True).data
#         return Response(data)

#     def post(self, request, board_id):
#         serializer = TopicSerializer(data=request.data)
#         topic_details = request.data
#         if serializer.is_valid():
#             topic = serializer.save()
#             post_serializer = PostSerializer(data={"message": topic_details['message'], "topic": topic.pk,
#                 "created_by": topic.created_by, "created_dt": topic.created_dt, "updated_by": topic.updated_by, "updated_by": topic.updated_by})
#             if post_serializer.is_valid():
#                 post_serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BoardDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardsSerializer
#     lookup_url_kwarg = 'board_id'


# class BoardDetails(APIView):
#     def get(self, request, board_id):
#         board = get_object_or_404(Board, pk=board_id)
#         data = BoardsSerializer(board).data
#         return Response(data)






# def board_topics(request, board_id):
#     board = get_object_or_404(Board, pk=board_id)
#     topics = board.topics.order_by('-created_dt').annotate(comments = Count('posts'))
#     data = {"Results":{
#         "name": board.name,
#         "description": board.description
#     },"topics": list(topics.values("pk", "subject", "board", "created_by", "created_dt"))
#     }
#     return JsonResponse(data)
