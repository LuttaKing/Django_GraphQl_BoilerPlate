from .actor import CreateActor, UpdateActor
from .movies import CreateMovie, UpdateMovie
import graphene


class Mutation(graphene.ObjectType):
    create_actor = CreateActor.Field()
    update_actor = UpdateActor.Field()
    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()
