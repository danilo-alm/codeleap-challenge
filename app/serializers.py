from rest_framework import serializers
from .models import Post, Reaction


class PostSerializer(serializers.ModelSerializer):
	likes = serializers.SerializerMethodField()
	dislikes = serializers.SerializerMethodField()

	class Meta:
		model = Post
		fields = ("id", "username", "created_datetime", "title", "content", "likes", "dislikes")
		read_only_fields = ("id", "created_datetime")

	def get_likes(self, obj: Post) -> int:
		return obj.reactions.filter(value=1).count()

	def get_dislikes(self, obj: Post) -> int:
		return obj.reactions.filter(value=-1).count()


class PostCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ("username", "title", "content")


class PostUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ("title", "content")


class ReactionCreateSerializer(serializers.ModelSerializer):
	post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

	class Meta:
		model = Reaction
		fields = ("post", "username", "value")

	def validate_value(self, value: int) -> int:
		if value not in (-1, 1):
			raise serializers.ValidationError("value must be -1 (dislike) or 1 (like)")
		return value


class ReactionUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reaction
		fields = ("value",)
	
	def validate_value(self, value: int) -> int:
		if value not in (-1, 1):
			raise serializers.ValidationError("value must be -1 (dislike) or 1 (like)")
		return value


class ReactionDeleteSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=150) 