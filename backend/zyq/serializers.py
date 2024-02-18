from rest_framework import serializers
from .models import regional_sample, video, user, SaveFile, lineChart, pieChart, rule_table, decisionTree_img
from .models import forset
from .models import Blog
from .models import poplar
from .models import treeTmp
from .models import Qx


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ('id', 'name', 'age', 'sex', 'url')

class QxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Qx
        fields = '__all__'




class regional_sampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = regional_sample
        fields = '__all__'


class forsetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = forset
        fields = '__all__'


class poplarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = poplar
        fields = ('place', 'block', 'clone', 'rep', 'height','diameter','url')


class videoSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = ('id', 'name', 'video', 'url')

class lineChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = lineChart
        fields = ('id', 'name', 'image', 'url')

class pieChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = pieChart
        fields = ('id', 'name', 'image', 'url')

class treeTmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = treeTmp
        fields = ('place', 'block', 'clone', 'rep', 'height','diameter','url')

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields =('username', 'password','email','phone','sex')

class SaveFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SaveFile
        fields =('create_time', 'name','file_url','id','url')

class rule_tableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = rule_table
        fields = '__all__'

class decisionTree_imgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = decisionTree_img
        fields = '__all__'