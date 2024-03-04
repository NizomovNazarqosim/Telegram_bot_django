from .models import Staff, Position
from rest_framework import serializers

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ("staff_id", "staff_name", "staff_surname", "staff_birthday","staff_position")


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ("position_id", "position_title")
