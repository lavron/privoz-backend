import graphene

from app.schema.types import PlayerType, GameQueueType, SectorType
from rx import Observable
from rx.subjects import Subject


class PlayerUpdated(graphene.ObjectType):
    player = graphene.Field(PlayerType)


class QueueUpdated(graphene.ObjectType):
    queue = graphene.Field(GameQueueType)


class SectorUpdated(graphene.ObjectType):
    sector = graphene.Field(SectorType)


class ErrorUpdated(graphene.ObjectType):
    error = graphene.String()


player_updates = Subject()
queue_updates = Subject()
sector_updates = Subject()



class Subscription(graphene.ObjectType):
    player_updated = graphene.Field(PlayerUpdated)
    queue_updated = graphene.Field(QueueUpdated)
    sector_updated = graphene.Field(SectorUpdated)

    def resolve_player_updated(root, info):
        return Observable.create(define_observable_func(player_updates))

    def resolve_queue_updated(root, info):
        return Observable.create(define_observable_func(queue_updates))

    def resolve_sector_updated(root, info):
        return Observable.create(define_observable_func(sector_updates))


def define_observable_func(updates):
    def observable_func(observer):
        def on_update(value):
            observer.on_next(value)

        updates.subscribe(on_update)


def update_player(player):
    player_updates.on_next(PlayerUpdated(player=player))


def update_queue(queue):
    queue_updates.on_next(QueueUpdated(queue=queue))


def update_sector(sector):
    sector_updates.on_next(SectorUpdated(sector=sector))
