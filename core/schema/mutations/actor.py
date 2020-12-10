import graphene
from graphene_django.types import DjangoObjectType
from core.models import Actor
from graphene_file_upload.scalars import Upload


class ActorType1(DjangoObjectType):
    class Meta:
        model = Actor


class ActorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    pic = Upload(required=True)


class CreateActor(graphene.Mutation):
    class Arguments:
        input = ActorInput(required=True)

    ok = graphene.Boolean()
    actor = graphene.Field(ActorType1)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        actor_instance = Actor(name=input.name, pic=input.pic)
        actor_instance.save()
        return CreateActor(ok=ok, actor=actor_instance)


class UpdateActor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ActorInput(required=True)

    ok = graphene.Boolean()
    actor = graphene.Field(ActorType1)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        actor_instance = Actor.objects.get(pk=id)
        if actor_instance:
            ok = True
            actor_instance.name = input.name
            actor_instance.save()
            return UpdateActor(ok=ok, actor=actor_instance)
        return UpdateActor(ok=ok, actor=None)
