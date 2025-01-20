from graphene import relay, Schema, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from catalogue.models import Author, Category, Book


class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = ('alias','date_of_birth', 'produced_books')
        interfaces = (relay.Node, )


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            # 'related_books',
            # 'book__name': ['exact'],
        }
        interfaces = (relay.Node,)


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        filter_fields = {
            'name': ['exact', 'istartswith'], 
            'category': ['exact'], 
            'category__name': ['exact'], 
            # 'author': ['exact'],
            # 'author__name': ['exact'], 
            }
        interfaces = (relay.Node,)


class Query(ObjectType):
    book = relay.Node.Field(BookNode)
    all_book = DjangoFilterConnectionField(BookNode)
    # author = relay.Node.Field(AuthorNode)
    # all_author = DjangoFilterConnectionField(AuthorNode)
    category = relay.Node.Field(CategoryNode)
    all_category = DjangoFilterConnectionField(CategoryNode)
        

schema = Schema(query=Query)