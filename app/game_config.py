INITIAL_COINS = 10
MAX_PLAYERS = 4
PRODUCT_IMAGE_PLACEHOLDER = 'https://dummyimage.com/512/6ab555/ffffff.png&text=+PRODUCT'
EVENT_IMAGE_PLACEHOLDER = 'https://dummyimage.com/512/62929E/ffffff.png&text=+++EVENT'
CARD_IMAGE_PLACEHOLDER = 'https://dummyimage.com/512/#E2DADB/000000.png&text=+++'

PHASE_CHOICES = (
    ('hire_trader', 'Hire Trader Phase'),
    ('event_card_purchase', 'Event Card Acquisition Phase'),
    ('product_card_acquisition', 'Product Card Acquisition Phase'),
    ('week_card_reveal', 'Week Card Reveal Phase'),
    ('negative_card_reveal', 'Negative Card Reveal Phase'),
    ('sales', 'Sales Phase'),
    ('event_card_play', 'Event Card Play Phase'),
    ('paycheck_phase', 'Paycheck Phase'),
)


PHASE_ORDER = {
    'hire_trader': 'event_card_purchase',
    'event_card_purchase': 'product_card_acquisition',
    'product_card_acquisition': 'week_card_reveal',
    'week_card_reveal': 'negative_card_reveal',
    'negative_card_reveal': 'sales',
    'sales': 'event_card_play',
    'event_card_play': 'paycheck_phase',
    'paycheck_phase': 'hire_trader',  # back to first phase
}
