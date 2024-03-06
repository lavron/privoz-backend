INITIAL_COINS = 10
MAX_PLAYERS = 4
PRODUCT_CARDS_DRAW_COUNT = 7
GAME_ROUNDS = 7

PRODUCT_IMAGE_PLACEHOLDER = 'https://dummyimage.com/512/6ab555/ffffff.png&text=+PRODUCT'
EVENT_IMAGE_PLACEHOLDER = 'https://dummyimage.com/512/62929E/ffffff.png&text=+++EVENT'
CARD_IMAGE_PLACEHOLDER = 'https://dummyimage.com/512/#E2DADB/000000.png&text=+++'

PHASE_CHOICES = (
    ('DRAW_PRODUCT_CARDS', 'Draw Product Cards Phase'),
    ('GET_TRADER', 'Hire Trader Phase'), # mutation
    ('SALES', 'Sales Phase'),
    ('PAYCHECK', 'Paycheck Phase'),
)


PHASE_ORDER = {
    'DRAW_PRODUCT_CARDS': 'GET_TRADER',
    'GET_TRADER': 'SALES',
    'SALES': 'PAYCHECK',
    'PAYCHECK': 'DRAW_PRODUCT_CARDS',
}

PHASES_COUNT = 7
DRAW_PRODUCT_CARDS_COUNT = 7

TRADER_SALARY = 1
