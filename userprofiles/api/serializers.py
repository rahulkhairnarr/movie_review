from rest_framework import serializers
from django.contrib.auth import get_user_model

# from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  get_user_model()

        fields = ['email','username','password']
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }

    def get_id(self,obj):
        request = self.context.get("request")
        user_id = request.user.id
        return