from app.models import Sector, EventCard

json_event_cards = [
    {
        "id": "ev_card_fntr",
        "title": "Federal Police",
        "description": "Confiscate illegal goods plus a fine.",
        "fortune": "negative",
        "quantity_ingame": 7,
        "quantity_active": 5,
        "position_in_game": "deck",
        "goal_action": "sector",
        "goal_item": "trader",
        "effect": [{"confiscation": "true"}, {"fine": [5]}, {"trader_action": "hold"}]
    },
    {
        "id": "ev_card_mkt",
        "title": "Mafia ('brothers') Karabas and Stas",
        "description": "2 coins of donations for each seller.",
        "fortune": "negative",
        "quantity_ingame": 7,
        "quantity_active": 7,
        "position_in_game": "deck",
        "goal_action": "sector",
        "goal_item": "trader",
        "effect": [{"confiscation": "false"}, {"fine": [2]}]
    },
    {
        "id": "ev_card_pstr",
        "title": "Prosecutor's Office",
        "description": "Confiscation of illegal goods plus a fine.",
        "fortune": "negative",
        "quantity_ingame": 7,
        "quantity_active": 7,
        "position_in_game": "deck",
        "goal_action": "sector",
        "goal_item": "trader",
        "effect": [{"confiscation": "true"}, {"fine": [2]}, {"trader_action": "hold"}]
    },
    {
        "id": "ev_card_ses",
        "title": "Sanitary Epidemiological Station",
        "description": "2 coins of donations for each seller.",
        "fortune": "negative",
        "quantity_ingame": 7,
        "quantity_active": 7,
        "position_in_game": "deck",
        "goal_action": "sector",
        "goal_item": "trader",
        "effect": [{"confiscation": "false"}, {"fine": [2]}]
    },
    {
        "id": "ev_card_ff",
        "title": "Firefighters",
        "description": "2 coins of donations for each seller.",
        "fortune": "negative",
        "quantity_ingame": 7,
        "quantity_active": 7,
        "position_in_game": "deck",
        "goal_action": "sector",
        "goal_item": "trader",
        "effect": [{"confiscation": "false"}, {"fine": [2]}]
    },
    {
        "id": "ev_card_lpo",
        "title": "Local Police Officer",
        "description": "2 coins of donations for each seller.",
        "fortune": "negative",
        "quantity_ingame": 7,
        "quantity_active": 7,
        "position_in_game": "deck",
        "goal_action": "sector",
        "goal_item": "trader",
        "effect": [{"confiscation": "true"}, {"fine": [2]}, {"trader_action": "hold"}]
    },
    {
        "id": "ev_card_bgg",
        "title": "Beggars",
        "description": "-1 to the selling price.",
        "fortune": "negative",
        "quantity_ingame": 7,
        "quantity_active": 7,
        "position_in_game": "deck",
        "goal_action": "sector",
        "goal_item": "product",
        "effect": [{"price_fine": [1]}]
    },
    {
        "id": "ev_card_add",
        "title": "Addicts (Narcos)",
        "description": "-1 to the selling price.",
        "fortune": "negative",
        "quantity_ingame": 7,
        "quantity_active": 7,
        "position_in_game": "deck",
        "goal_action": "sector",
        "goal_item": "product",
        "effect": [{"price_fine": [1]}]
    },
    {
        "id": "ev_card_pst",
        "title": "Priests (Monks)",
        "description": "2 coins of donations for each seller.",
        "fortune": "negative",
        "quantity_ingame": 7,
        "quantity_active": 7,
        "position_in_game": "deck",
        "goal_action": "sector",
        "goal_item": "product",
        "effect": [{"price_fine": [2]}]
    },
    {
        "id": "ev_card_up",
        "title": "Underworld Protection",
        "description": "Protection.",
        "fortune": "positive",
        "quantity_ingame": 21,
        "quantity_active": 18,
        "position_in_game": "deck",
        "goal_action": "trader",
        "goal_item": "trader",
        "effect": [{"Illigal_protection": "true"}, {"trader_action": "free"}]
    },
    {
        "id": "ev_card_rc",
        "title": "Regular Customer",
        "description": "Profit +2 coins.",
        "fortune": "positive",
        "quantity_ingame": 14,
        "quantity_active": 14,
        "position_in_game": "deck",
        "goal_action": "trader",
        "goal_item": "product",
        "effect": [{"extra_price": [2]}]
    },
    {
        "id": "ev_card_tabp",
        "title": "Transport Arrived and Brought People",
        "description": "Profit +1 from each seller.",
        "fortune": "positive",
        "quantity_ingame": 14,
        "quantity_active": 14,
        "position_in_game": "deck",
        "goal_action": "trader",
        "goal_item": "product",
        "effect": [{"extra_price": [1]}]
    },
    {
        "id": "ev_card_prtrs",
        "title": "Porters",
        "description": "Goods +1 from the market for free.",
        "fortune": "positive",
        "quantity_ingame": 14,
        "quantity_active": 14,
        "position_in_game": "deck",
        "goal_action": "trader",
        "goal_item": "product",
        "effect": [{"extra_product": [1]}]
    }
]


# create EventCards from json_event_cards


def set_effects(event_card, target_item, effect, save=False):
    if target_item == "trader":
        if "confiscation" in effect:
            event_card.confiscation = bool(effect.get("confiscation", 'false') == 'true')
        if "fine" in effect:
            event_card.trader_extra_profit = -effect.get("fine", [0])[0]
        if "trader_action" in effect:
            event_card.trader_is_active = bool(effect.get("trader_action", 'false') == "free")
        if "Illigal_protection" in effect:
            event_card.protection = bool(effect.get("Illigal_protection", 'false') == "true")
    elif target_item == "product":
        if "price_fine" in effect:
            event_card.product_extra_profit = -effect.get("price_fine")[0]
        if "extra_price" in effect:
            event_card.player_extra_profit = effect.get("extra_price")[0]
    if save:
        event_card.save()


for card in json_event_cards:
    event_card, created = EventCard.objects.get_or_create(
        name=card["title"].capitalize(),
        description=card["description"],

        fortune=card["fortune"],
        target=card["goal_action"],
        # item=card["goal_item"],
    )

    for effect in card["effect"]:
        set_effects(event_card, card["goal_item"], effect, True)

    print("👉🏻event_card", event_card.__dict__)
