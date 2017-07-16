from rest_framework import serializers

from dusken.models import DuskenUser
from dusken.utils import generate_username
from dusken.api.serializers.cards import MemberCardSerializer
from dusken.api.serializers.memberships import MembershipSerializer


class DuskenUserSerializer(serializers.ModelSerializer):
    cards = MemberCardSerializer(source='member_cards', many=True)
    memberships = MembershipSerializer(many=True)
    has_valid_membership = serializers.SerializerMethodField(method_name='has_valid_membership')
    last_valid_membership = serializers.SerializerMethodField()

    def has_valid_membership(self, obj):
        return obj.has_valid_membership()

    def get_last_valid_membership(self, obj):
        membership = obj.get_last_valid_membership()
        return membership.pk if membership else None

    class Meta:
        model = DuskenUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number',
                  'date_of_birth', 'legacy_id', 'place_of_study', 'cards',
                  'memberships', 'has_valid_membership', 'last_valid_membership')
        read_only_fields = ('id', 'username', 'cards', 'memberships')
        write_only_fields = ('password',)


class NewDuskenUserSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not data.get('username', ''):
            data['username'] = generate_username(data['first_name'], data['last_name'])

        return data

    class Meta:
        model = DuskenUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number')
        read_only_fields = ('id', 'username',)
        write_only_fields = ('password',)
