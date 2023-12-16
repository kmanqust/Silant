from rest_framework import serializers
from .models import TO_output, Machine, Reklamacia_output

class TO_outputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TO_output
        fields = ('Zav_number_machine', 'Type_TO', 'Date_TO', 'Operating_time', 'Number_work_order', 'Date_work_order', 'Organization_TO')

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('Number', 'Model_of_equipment', 'Zav_number_machine', 'Engine_model',
                  'Zav_number_engine', 'Transmission_model', 'Zav_number_transmission', 'Drive_axle_model',
                  'Zav_number_drive_axle', 'Steering_axle_model', 'Zav_number_steering_axle', 'Date_shipment',
                  'Buyer', 'Consignee', 'Delivery_address', 'Configuration', 'Service_company')

class Reklamatica_outputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reklamacia_output
        fields = ('Zav_number', 'Date_otkaz', 'Operating_time', 'Node_otkaz', 'Description_otkaz', 'Way', 'Used', 'Date', 'Time')