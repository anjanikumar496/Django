from ..models import *
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response



#
# class PostListView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
#
# class PostCreateView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
#
#     def create(self, request, *args, **kwargs):
#         super(PostCreateView, self).create(request, args, kwargs)
#         response = {"status_code": status.HTTP_200_OK,
#                     "message": "Successfully created",
#                     "result": request.data}
#         return Response(response)
#
#
#
#
# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
#
#     def retrieve(self, request, *args, **kwargs):
#         super(PostDetailView, self).retrieve(request, args, kwargs)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         data = serializer.data
#         response = {"status_code": status.HTTP_200_OK,
#                     "message": "Successfully retrieved",
#                     "result": data}
#         return Response(response)
#
#     def patch(self, request, *args, **kwargs):
#         super(PostDetailView, self).patch(request, args, kwargs)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         data = serializer.data
#         response = {"status_code": status.HTTP_200_OK,
#                     "message": "Successfully updated",
#                     "result": data}
#         return Response(response)
#
#     def delete(self, request, *args, **kwargs):
#         super(PostDetailView, self).delete(request, args, kwargs)
#         response = {"status_code": status.HTTP_200_OK,
#                     "message": "Successfully deleted"}
#         return Response(response)



class PostLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.LoginSerializer
    def create(self, request, *args, **kwargs):
        message = "Successfully created"
        if User.objects.all().filter(username=request.data.dict().get('username')).first():
            message = "Username Already Exists"
            response = {"status_code": status.HTTP_409_CONFLICT,
                        "message": message,
                        "result": request.data}
        else:
            super(PostLoginView, self).create(request, args, kwargs)
            response = {"status_code": status.HTTP_200_OK,
                        "message": message,
                        "result": request.data}
        return Response(response)

