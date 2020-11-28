import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from core.models import Actor


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor


class ActorQuery(ObjectType):
    actor = graphene.Field(ActorType, id=graphene.Int())
    actors = graphene.List(ActorType)

    def resolve_actor(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Actor.objects.get(pk=id)

        return None

    def resolve_actors(self, info, **kwargs):
        return Actor.objects.all()
