from rest_framework import serializers
from .models import AppStat


class AppStatSerializer(serializers.ModelSerializer):
    os = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super(AppStatSerializer, self).__init__(*args, **kwargs)

        if self.context['request'].GET.get('group_by') and self.instance:
            fields_not_needed = set(self.fields) - set(self.instance[0])

            for field in fields_not_needed:
                self.fields.pop(field)

    @staticmethod
    def get_os(obj):
        if isinstance(obj, AppStat):
            return obj.get_os_display()
        elif obj['os'] == AppStat.ANDROID:
            return "android"
        elif obj['os'] == AppStat.IOS:
            return "ios"

    class Meta:
        model = AppStat
        fields = '__all__'
