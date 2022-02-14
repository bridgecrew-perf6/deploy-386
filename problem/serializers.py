from urllib import request
from rest_framework import serializers
from .models import *
from comment.serializers import CommentSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class ProblemSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = Problem
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        action = self.context.get('action')
        if action == 'list':
            representation['replies'] = instance.replies.count()
            representation['comments'] = instance.comments.count()
        elif action == 'retrieve':
            representation['images'] = ImageSerializer(
                instance.images.all(), many=True
            ).data
        representation['replies'] = ReplySerializer(
            instance.replies.all(), many=True
        ).data
        representation['comments'] = CommentSerializer(
            instance.replies.all(), many=True
        ).data
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        image_data = request.FILES
        problem = Problem.objects.create(
            author = request.user,
            **validated_data
        )
        for image in image_data.getlist('image'):
            Image.objects.create(
                image=image,
                problem=problem
            )
        return problem
        # MULTIVALUESDICT - прочитать!!!
    

class ReplySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Reply
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get('request')
        reply = Reply.objects.create(
            author = request.user,
            **validated_data
        )
        return reply


#TODO: Swagger
#TODO: Salary
#TODO: Model Signals
#TODO: Восстановление пароля
