from .actor import ActorQuery
from .movies import MovieQuery


class Query(ActorQuery, MovieQuery):
    pass
