from rest_framework import serializers
from test_app.models import Machines

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machines
        fields = ('event_id','status_1','status_2','dt_ts')