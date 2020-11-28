import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from core.models import Movie


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
# Create a Query type


class MovieQuery(ObjectType):
    movie = graphene.Field(MovieType, id=graphene.Int())
    movies = graphene.List(MovieType)

    def resolve_movies(self, info, **kwargs):
        return Movie.objects.all()

    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Movie.objects.get(pk=id)

        return None
