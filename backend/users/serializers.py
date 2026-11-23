from djoser.serializers import UserCreatePasswordRetypeSerializer, UserSerializer


class CustomUserCreateSerializer(UserCreatePasswordRetypeSerializer):
    """Expose the optional address when a user registers through Djoser."""

    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = UserCreatePasswordRetypeSerializer.Meta.fields + ("address",)


class CustomUserSerializer(UserSerializer):
    """Return the optional address in Djoser user responses."""

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ("address",)
