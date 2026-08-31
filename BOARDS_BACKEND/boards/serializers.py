from rest_framework import serializers
from .models import *

class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    boards = BoardsSerializer(many=True, read_only=True)
    board_name = serializers.CharField(source="board.name", required=False)
    creator_name = serializers.CharField(source="created_by.username", required=False)
    class Meta:
            model = Topic
            fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True, required=False)
    class Meta:
            model = Post
            fields = '__all__'
