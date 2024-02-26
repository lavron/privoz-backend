INITIAL_COINS = 10
MAX_PLAYERS = 4
PRODUCT_IMAGE_PLACEHOLDER = 'https://dummyimage.com/512/6ab555/ffffff.png&text=+PRODUCT'
EVENT_IMAGE_PLACEHOLDER = 'https://dummyimage.com/512/62929E/ffffff.png&text=+++EVENT'
CARD_IMAGE_PLACEHOLDER = 'https://dummyimage.com/512/#E2DADB/000000.png&text=+++'

PHASE_CHOICES = (
    ('hire_trader', 'Hire Trader Phase'), # mutation
    ('take_event_card', 'Take Event Card Phase'),
    ('buy_products', 'Buy Products Phase'), # mutation [{product_card_id, trader_id}].
    ('reveal_week_card', 'Week Card Reveal Phase'),
    ('reveal_negative_card', 'Negative Card Reveal Phase'),
    ('sales', 'Sales Phase'),
    ('play_event_card', 'Play Event Card Phase'), # mutation player_id, event_card_id, target_type, target_id,
    ('paycheck', 'Paycheck Phase'),
)


PHASE_ORDER = {
    'hire_trader': 'take_event_card',
    'take_event_card': 'buy_products',
    'buy_products': 'reveal_week_card',
    'reveal_week_card': 'reveal_negative_card',
    'reveal_negative_card': 'sales',
    'sales': 'play_event_card',
    'play_event_card': 'paycheck',
    'paycheck': 'hire_trader',  # back to first phase
}
