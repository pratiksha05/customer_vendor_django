from apps.users.serializers.tokenSerializer import MyTokenObtainPairSerializer


def get_my_token(user_detail):
    my_token = MyTokenObtainPairSerializer()
    data = my_token.validate(user_detail)
    return data