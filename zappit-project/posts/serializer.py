from rest_framework import serializers
from .models import Post,Vote

class Postserializer(serializers.ModelSerializer):

    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.username')

    class Meta :
        model = Post
        fields = ['id','title', 'url', 'poster','poster_id' ,'created'] 

class Voteserializer(serializers.ModelSerializer):

   
    class Meta :
        model = Vote
        fields = ['id', ] 