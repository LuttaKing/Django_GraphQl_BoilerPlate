import graphene
from core.schema.queries import Query as CoreQuery
from core.schema.mutations import Mutation as CoreMutation


class Query(CoreQuery, graphene.ObjectType):
    pass


class Mutation(CoreMutation):
    pass
