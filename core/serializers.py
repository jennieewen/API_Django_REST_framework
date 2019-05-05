from rest_framework import serializers
from .models import (
    Customer,
    Profession,
    DataSheet,
    Document
)

class ProfessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profession
        fields = (
            'id', 'description', 'status')


class DataSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSheet
        fields = (
            'id', 'description', 'historical_data')

    # function that does the exact same thing as  data_sheet = serializers.StringRelatedField()
    # def get_data_sheet(self, obj):
    #     return obj.data_sheet.description

# Serializers define the API representation.
class CustomerSerializer(serializers.ModelSerializer):
    num_professions = serializers.SerializerMethodField()
    data_sheet = DataSheetSerializer()
    professions = ProfessionSerializer(many=True)
    #professions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customer
        fields = (
            'id', 'name', 'address', 'professions', 'data_sheet',
            'active', 'status_message', 'num_professions')

    # writing serializer create() method to replace create() in views and handle manytomany/onetoone relationships
    def create(self, validated_data):

        # onetoone
        data_sheet = validated_data['data_sheet']
        del validated_data['data_sheet']
        dataSheet = DataSheet.objects.create(**data_sheet)
        customer = Customer.objects.create(**validated_data)
        customer.data_sheet = dataSheet

        # manytomany
        professions = validated_data['professions']
        del validated_data['professions']
        # create professions
        for profession in professions:
            prof = Profession.objects.create(**profession)
            customer.professions.add(prof)

        customer.save()

        return customer


    def get_num_professions(self, obj): #obj is the customer instantiated
        return obj.num_professions()


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = (
            'id', 'dtype', 'doc_number', 'customer')

