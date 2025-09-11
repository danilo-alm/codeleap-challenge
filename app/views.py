from rest_framework import generics, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Post, Reaction
from .serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer, ReactionCreateSerializer, ReactionUpdateSerializer


class PostListCreateView(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	permission_classes = [AllowAny]

	def get_serializer_class(self):
		if self.request.method == "POST":
			return PostCreateSerializer
		return PostSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		post = serializer.save()
		output = PostSerializer(post)
		return Response(output.data, status=status.HTTP_201_CREATED)


class PostDetailView(mixins.UpdateModelMixin,
					 mixins.DestroyModelMixin,
					 generics.GenericAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [AllowAny]

	def get(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = PostSerializer(instance)
		return Response(serializer.data)

	def patch(self, request, *args, **kwargs):
		self.serializer_class = PostUpdateSerializer
		self.partial_update(request, *args, **kwargs)
		instance = self.get_object()
		return Response(PostUpdateSerializer(instance).data)

	def delete(self, request, *args, **kwargs):
		self.destroy(request, *args, **kwargs)
		return Response(status=status.HTTP_204_NO_CONTENT) 


class ReactView(mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Reaction.objects.all()
    serializer_class = ReactionCreateSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        self.serializer_class = ReactionUpdateSerializer
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)