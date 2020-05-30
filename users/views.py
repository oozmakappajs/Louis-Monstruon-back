from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Users, Orders, Address, AddressUsers
from .serializers import UsersSerializer, OrdersSerializer, AddressSerializer, AddressUsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class AddressUserViewSet(viewsets.ModelViewSet):
    serializer_class = AddressUsersSerializer
    queryset = AddressUsers.objects.all()


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_user(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # get details of a single user
    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data)
    # delete a single user
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single user
    if request.method == 'PUT':
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_users(request):
    # get all users
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
    # insert a new record for a user
    if request.method == 'POST':
        data = {
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email_verified': bool(request.data.get('email_verified')),
            'registrationDate': bool(request.data.get('registrationDate')),
            'phone': request.data.get('phone'),
        }
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
