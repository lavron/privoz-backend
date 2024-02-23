import strawberry
from app.schema.queries.game_query import GameQuery
from app.schema.queries.box_query import BoxQuery
from app.schema.mutations.hire_trader import Mutation as HireTraderMutation
from app.schema.mutations.reset_game import Mutation as ResetGameMutation
import asyncio


# class Query(GameQuery, BoxQuery):
@strawberry.type
class Query(BoxQuery, GameQuery):
    @strawberry.field
    def respond(self) -> str:
        return "Hello, World!"

# @strawberry.type
# class Mutation():
#     pass

# @strawberry.type
# class Subscription:
#     @strawberry.subscription
#     async def count(self, target: int = 100) -> int:
#         for i in range(target):
#             yield i
#             await asyncio.sleep(0.5)

# schema = strawberry.Schema(query=Query, mutation=Mutation)
schema = strawberry.Schema(query=Query)