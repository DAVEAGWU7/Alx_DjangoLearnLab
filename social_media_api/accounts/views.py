from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()   

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(user_to_follow)
        return Response({'detail': 'User followed'})


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()   

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({'detail': 'User unfollowed'})
