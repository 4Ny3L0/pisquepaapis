from rest_framework import serializers
from psiquepaWEB.errors_messages import ErrorsMessages


class RegisterCustomValidators:

    def name_validations(name):
        pass

    def password_validations(password):
        custom_error_message = ErrorsMessages()
        if len(password) < 8:
            raise serializers.ValidationError(ErrorsMessages.min_length)
        if len(password) > 16:
            raise serializers.ValidationError(custom_error_message.max_length)

    def user_name_validations(user_name):
        if len(user_name) < 8:
            raise serializers.ValidationError(ErrorsMessages.user_name_min)

        if len(user_name) > 25:
            raise serializers.ValidationError(ErrorsMessages.user_name_max)

    def validate_required_entries(values: dict, serializer_class):
        fields = serializer_class.Meta.fields
        for field in fields:
            exist = values.get(field)
            if exist is None:
                raise serializers.ValidationError(ErrorsMessages.field_required)
            if len(str(exist)) == 0:
                raise serializers.ValidationError(ErrorsMessages.field_is_blank)
