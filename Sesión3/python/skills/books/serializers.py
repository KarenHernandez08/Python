from rest_framework import serializers

from books.models import Books, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields=('id', 'first_name', 'last_name','birth_date')
        
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model= Books
        fields= '__all__'
        
    def to_representation (self, instance):
        
        response= super().to_representation(instance)
        response['author']=AuthorSerializer(instance.author).data
        return response 