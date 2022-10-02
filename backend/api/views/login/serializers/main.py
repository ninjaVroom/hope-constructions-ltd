
from django.db.models import Q
from rest_framework import serializers
from django.contrib.auth.models import User
from Libraries.functions.serializer.request_data.to_dict import request_data_to_dict
from Libraries.functions.serializer.response.error import error_response
from Libraries.functions.passwords.unhash import verify_pswd


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(label='Email Address', write_only=True, required=True)
    password = serializers.CharField(label='Password', write_only=True,
                                     style={'input_type': 'password'}, trim_whitespace=False
                                     )

    def to_internal_value(self, data):
        # print({"to_internal_value-data": data})
        new_data = request_data_to_dict(data)

        # password_confirm = new_data.get('password-confirm')
        # new_data['password_confirm'] = password_confirm

        # new_data.pop('password-confirm', None)

        return super().to_internal_value(new_data)

    def validate(self, attrs):
        # print({"validate-attrs": attrs})
        new_attrs = request_data_to_dict(attrs)

        email: str | None = new_attrs.get('email')
        password: str | None = new_attrs.get('password')
        # password_confirm: str | None = new_attrs.get('password_confirm')

        valid_accounts = []
        
        if email:
            if password:
                user = self.Meta.model.objects.filter(email = email)
                
                if user.exists():
                    for account in user:
                        dbPassword = str(account.password)
                        
                        # if verify_pswd(password, dbPassword):
                        #     if account not in valid_accounts:
                        #         valid_accounts.append(account)   
                        valid_accounts.append(account)                    
                else:
                    raise serializers.ValidationError(
                        detail=error_response([
                            "User account not found"
                        ]), code=''
                    ) 
            else:
                raise serializers.ValidationError(
                    detail=error_response([
                        "password* field is required"
                    ]), code=''
                )
        else:
            raise serializers.ValidationError(
                detail=error_response([
                    "Either one of the following fields are required",
                    "email*",
                ]), code=''
            )

        if len(valid_accounts) > 0:
            valid_account = valid_accounts[0]
        else:
            raise serializers.ValidationError(
                detail=error_response([
                    "account and password combination not found"
                ]), code=''
            )

        new_attrs['account'] = valid_account
        return super().validate(new_attrs)
        
    def validate_empty_values(self, data):
        # print({"validate_empty_values-data": data})
        new_data = request_data_to_dict(data)
        return super().validate_empty_values(new_data)

    class Meta:
        model = User
        fields = ("username",)
