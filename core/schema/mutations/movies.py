import graphene
from graphene_django.types import DjangoObjectType
from core.models import Movie


class MovieType1(DjangoObjectType):
    class Meta:
        model = Movie
# Create a Query type


class MovieInput(graphene.InputObjectType):
    id = graphene.ID()
    year = graphene.Int()


class CreateMovie(graphene.Mutation):
    class Arguments:
        input = MovieInput(required=True)

    ok = graphene.Boolean()
    movie = graphene.Field(MovieType1)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        movie_instance = Movie(
            title=input.title,
            year=input.year
        )
        movie_instance.save()
        return CreateMovie(ok=ok, movie=movie_instance)


class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = MovieInput(required=True)

    ok = graphene.Boolean()
    movie = graphene.Field(MovieType1)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        movie_instance = Movie.objects.get(pk=id)
        if movie_instance:
            ok = True
            movie_instance.title = input.title
            movie_instance.year = input.year
            movie_instance.save()
            return UpdateMovie(ok=ok, movie=movie_instance)
        return UpdateMovie(ok=ok, movie=None)
