import graphene
from graphene_django import DjangoObjectType
from app.models import Game, Player, Sector, ProductCard, EventCard, Trader
from app.models.event_card import EventCardDeck
from app.models.hero import Hero
from app.models.product_card import ProductCardDeck


class GameType(DjangoObjectType):
    class Meta:
        model = Game


class PlayerType(DjangoObjectType):
    class Meta:
        model = Player


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero


class SectorType(DjangoObjectType):
    class Meta:
        model = Sector


class ProductCardType(DjangoObjectType):
    class Meta:
        model = ProductCard


class EventCardType(DjangoObjectType):
    class Meta:
        model = EventCard


class ProductCardDeckType(DjangoObjectType):
    class Meta:
        model = ProductCardDeck


class EventCardDeckType(DjangoObjectType):
    class Meta:
        model = EventCardDeck


class TraderCardType(DjangoObjectType):
    class Meta:
        model = Trader


class AddTrader(graphene.Mutation):
    class Arguments:
        game_id = graphene.ID()
        user_id = graphene.ID()
        sector_id = graphene.ID()
        products_ids = graphene.List(graphene.ID)

    trader = graphene.Field(TraderCardType)

    def mutate(self, info, game_id, user_id, sector_id, products_ids):
        sector = Sector.objects.get(pk=sector_id)
        trader = Trader.objects.create(sector=sector)
        trader.products.set(ProductCard.objects.filter(pk__in=products_ids))
        trader.save()
        game = Game.objects.get(pk=game_id)
        player = game.players.get(pk=user_id)
        player.traders.add(trader)
        player.save()

        return AddTrader(trader=trader)


class DeckUnion(graphene.Union):
    class Meta:
        types = (EventCardDeckType, ProductCardDeckType)


class ShuffleDeck(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        deck_type = graphene.String()

    deck = graphene.Field(DeckUnion)

    def mutate(self, info, id, deck_type):
        deck_class_map = {
            'EventCardDeck': EventCardDeck,
            'ProductCardDeck': ProductCardDeck
        }

        if deck_type not in deck_class_map:
            raise Exception('Invalid deck type!')

        deck = deck_class_map[deck_type].objects.get(pk=id)
        deck.shuffle()
        deck.save()
        return ShuffleDeck(deck=deck)


class TakeProductCard(graphene.Mutation):
    class Arguments:
        game_id = graphene.ID()
        player_id = graphene.ID()

    product_card = graphene.Field(ProductCardType)

    def mutate(self, info, game_id, player_id):
        game = Game.objects.get(pk=game_id)
        player = game.players.get(pk=player_id)
        product_card = game.product_cards_deck.take_card()
        player.product_cards.add(product_card)
        player.save()
        return TakeProductCard(product_card=product_card)


class TakeEventCard(graphene.Mutation):
    class Arguments:
        game_id = graphene.ID()
        player_id = graphene.ID()

    event_card = graphene.Field(EventCardType)

    def mutate(self, info, game_id, player_id):
        game = Game.objects.get(pk=game_id)
        player = game.players.get(pk=player_id)
        event_card = game.event_cards_deck.take_card()
        player.event_cards.add(event_card)
        player.save()
        return TakeEventCard(event_card=event_card)


class Mutation(graphene.ObjectType):
    shuffle_deck = ShuffleDeck.Field()
    add_trader = AddTrader.Field()


class Query(graphene.ObjectType):
    games = graphene.List(GameType)
    heroes = graphene.List(HeroType)
    players = graphene.List(PlayerType)
    sectors = graphene.List(SectorType)
    product_cards = graphene.List(ProductCardType)
    event_cards = graphene.List(EventCardType)
    traders = graphene.List(TraderCardType)
    event_card_decks = graphene.List(EventCardDeckType)
    product_card_decks = graphene.List(ProductCardDeckType)

    game = graphene.Field(GameType, pk=graphene.ID())
    player = graphene.Field(PlayerType, pk=graphene.ID())
    sector = graphene.Field(SectorType, pk=graphene.ID())

    def resolve_game(self, info, pk, **kwargs):
        return Game.objects.get(pk=pk)

    def resolve_games(self, info, **kwargs):
        return Game.objects.all()

    def resolve_players(self, info, **kwargs):
        return Player.objects.all()

    def resolve_player(self, info, game_id, player_id, **kwargs):
        game = Game.objects.get(pk=game_id)
        return game.players.get(pk=player_id)

    def resolve_heroes(self, info, **kwargs):
        return Player.objects.all()

    def resolve_sectors(self, info, **kwargs):
        return Sector.objects.all()



    def resolve_product_cards(self, info, **kwargs):
        return ProductCard.objects.all()

    def resolve_event_cards(self, info, **kwargs):
        return EventCard.objects.all()

    def resolve_traders(self, info, **kwargs):
        return Trader.objects.all()

    def resolve_event_card_decks(self, info, **kwargs):
        return EventCardDeck.objects.all()

    def resolve_product_card_decks(self, info, **kwargs):
        return ProductCardDeck.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)
