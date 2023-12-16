from django.db import models

class Model_of_equipment(models.Model):
    Name = models.CharField(max_length=200, primary_key = True)
    Description = models.CharField(max_length=200)

class Engine_model(models.Model):
    Name = models.CharField(max_length=200, primary_key = True)
    Description = models.CharField(max_length=200)

class Transmission_model(models.Model):
    Name = models.CharField(max_length=200, primary_key = True)
    Description = models.CharField(max_length=200)

class Drive_axle_model(models.Model):
    Name = models.CharField(max_length=200, primary_key = True)
    Description = models.CharField(max_length=200)

class Steering_axle_model(models.Model):
    Name = models.CharField(max_length=200, primary_key = True)
    Description = models.CharField(max_length=200)

class Service_company(models.Model):
    Name = models.CharField(max_length=200, primary_key = True)
    Description = models.CharField(max_length=200)

class Type_TO(models.Model):
    Name = models.CharField(max_length=200, primary_key = True)
    Description = models.CharField(max_length=200)

class Node_otkaz(models.Model):
    Name = models.CharField(max_length=200, primary_key = True)
    Description = models.CharField(max_length=200)

class Way(models.Model):
    Name = models.CharField(max_length=200, primary_key = True)
    Description = models.CharField(max_length=200)

class Machine(models.Model):
    Number = models.IntegerField(blank=True, null=True)
    Model_of_equipment = models.ForeignKey(Model_of_equipment, on_delete=models.CASCADE)
    Zav_number_machine = models.IntegerField(primary_key=True)
    Engine_model = models.ForeignKey(Engine_model, on_delete=models.CASCADE)
    Zav_number_engine = models.CharField(max_length=200, blank=True, null=True)
    Transmission_model = models.ForeignKey(Transmission_model, on_delete=models.CASCADE)
    Zav_number_transmission = models.CharField(max_length=200, blank=True, null=True)
    Drive_axle_model = models.ForeignKey(Drive_axle_model, on_delete=models.CASCADE)
    Zav_number_drive_axle = models.CharField(max_length=200, blank=True, null=True)
    Steering_axle_model = models.ForeignKey(Steering_axle_model, on_delete=models.CASCADE)
    Zav_number_steering_axle = models.CharField(max_length=200, blank=True, null=True)
    Date_shipment = models.DateField(blank=True, null=True)
    Buyer = models.CharField(max_length=1000, blank=True, null=True)
    Consignee = models.CharField(max_length=1000, blank=True, null=True)
    Delivery_address = models.CharField(max_length=1000, blank=True, null=True)
    Configuration = models.CharField(max_length=1000, blank=True, null=True)
    Service_company = models.ForeignKey(Service_company, on_delete=models.CASCADE)

class TO_output(models.Model):
    Zav_number_machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    Type_TO = models.ForeignKey(Type_TO, on_delete=models.CASCADE)
    Date_TO = models.DateField(blank=True, null=True)
    Operating_time = models.IntegerField(blank=True, null=True)
    Number_work_order = models.CharField(max_length=200, blank=True, null=True)
    Date_work_order = models.DateField(blank=True, null=True)
    Service_company = models.ForeignKey(Service_company, on_delete=models.CASCADE)

class Reklamacia_output(models.Model):
    Zav_number_machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    Date_otkaz = models.DateField(blank=True, null=True)
    Operating_time = models.IntegerField(blank=True, null=True)
    Node_otkaz = models.ForeignKey(Node_otkaz, on_delete=models.CASCADE)
    Description_otkaz = models.CharField(max_length=200, blank=True, null=True)
    Way = models.ForeignKey(Way, on_delete=models.CASCADE)
    Used = models.CharField(max_length=200, blank=True, null=True)
    Date = models.DateField(blank=True, null=True)
    Time = models.IntegerField(blank=True, null=True)