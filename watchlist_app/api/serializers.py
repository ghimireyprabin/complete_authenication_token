from watchlist_app.models import StreamPlatform,Review, WatchList
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Review
        # fields='__all__'
        exclude=['watchlist']
        

class WatchListSerializer(serializers.ModelSerializer):
    review= serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=WatchList
        # fields='__all__'
        exclude=['platform']
        
class StreamPlatformSerializers(serializers.ModelSerializer):
    watchlist=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=StreamPlatform
        fields='__all__'
        



