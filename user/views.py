from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from .models import User as UserModel
from .models import UserType as UserTypeModel


class UserView(APIView): # CBV 방식
    # permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능 (설정하지 않았을 때 기본값)
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    # 사용자 정보 조회
    def get(self, request):
        return Response({'message': 'get method!!'})
    
    # 회원가입
    def post(self, request):
        return Response({'message': 'post method!!'})

    # 회원 정보 수정
    def put(self, request):
        return Response({'message': 'put method!!'})

    # 회원 탈퇴
    def delete(self, request):
        return Response({'message': 'delete method!!'})


class UserApiView(APIView):
    permission_classes = [permissions.AllowAny]

    # 로그인과 회원가입
    def post(self, request):
        email = request.data.get('email', '')

        password = request.data.get('password', '')
        hashed_password = make_password(password)

        user = authenticate(request, email=email, password=hashed_password)
        print(user)
        if not user:
            type = request.data.get('type', '')
            get_type = UserTypeModel.objects.get(type=type)

            UserModel.objects.create(
                email = email,
                password = hashed_password,
                type = get_type
            )
            
            return Response({"message": "회원가입 성공!!"})

        else:
            login(request, user)
            return Response({"message": "로그인 성공!!"})        

    # 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"message": "로그아웃 성공"})