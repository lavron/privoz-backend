from app.models import Sector

json_products = {
    "sectors": [
        {
            "sector": "vegetables",
            "products": [
                {"productId": 1, "productName": "onion", "wholesalePrice": 2, "sellingPrice": 4, "profit": 2, "quantity_card": 16, "total_profit": 32, "product_sector": "vegetables", "imageSrc": "onion.svg", "legality": "legal"},
                {"productId": 2, "productName": "zucchini", "wholesalePrice": 3, "sellingPrice": 6, "profit": 3, "quantity_card": 12, "total_profit": 36, "product_sector": "vegetables", "imageSrc": "zucchini.svg", "legality": "legal"},
                {"productId": 3, "productName": "tomato", "wholesalePrice": 5, "sellingPrice": 9, "profit": 4, "quantity_card": 10, "total_profit": 40, "product_sector": "vegetables", "imageSrc": "tomato.svg"}
            ]
        },
        {
            "sector": "fruits",
            "products": [
                {"productId": 4, "productName": "apples", "wholesalePrice": 2, "sellingPrice": 4, "profit": 2, "quantity_card": 16, "total_profit": 32, "product_sector": "fruits", "imageSrc": "apples.svg", "legality": "legal"},
                {"productId": 5, "productName": "grapes", "wholesalePrice": 3, "sellingPrice": 6, "profit": 3, "quantity_card": 12, "total_profit": 36, "product_sector": "fruits", "imageSrc": "grapes.svg", "legality": "legal"},
                {"productId": 6, "productName": "strawberries", "wholesalePrice": 5, "sellingPrice": 9, "profit": 4, "quantity_card": 10, "total_profit": 40, "product_sector": "fruits", "imageSrc": "strawberries.svg"}
            ]
        },
        {
            "sector": "dairy",
            "products": [
                {"productId": 7, "productName": "milk", "wholesalePrice": 3, "sellingPrice": 6, "profit": 3, "quantity_card": 16, "total_profit": 48, "product_sector": "dairy", "imageSrc": "milk.svg", "legality": "legal"},
                {"productId": 8, "productName": "feta cheese", "wholesalePrice": 5, "sellingPrice": 9, "profit": 4, "quantity_card": 12, "total_profit": 48, "product_sector": "dairy", "imageSrc": "feta_cheese.svg", "legality": "legal"},
                {"productId": 9, "productName": "cheese", "wholesalePrice": 7, "sellingPrice": 12, "profit": 5, "quantity_card": 10, "total_profit": 50, "product_sector": "dairy", "imageSrc": "cheese.svg"}
            ]
        },
        {
            "sector": "fish",
            "products": [
                {"productId": 10, "productName": "anchovies", "wholesalePrice": 3, "sellingPrice": 6, "profit": 3, "quantity_card": 16, "total_profit": 48, "product_sector": "fish", "imageSrc": "anchovies.svg", "legality": "legal"},
                {"productId": 11, "productName": "mackerel", "wholesalePrice": 5, "sellingPrice": 9, "profit": 4, "quantity_card": 12, "total_profit": 48, "product_sector": "fish", "imageSrc": "mackerel.svg", "legality": "legal"},
                {"productId": 12, "productName": "salmon", "wholesalePrice": 7, "sellingPrice": 12, "profit": 5, "quantity_card": 10, "total_profit": 50, "product_sector": "fish", "imageSrc": "salmon.svg"}
            ]
        },
        {
            "sector": "meat",
            "products": [
                {"productId": 13, "productName": "chicken", "wholesalePrice": 5, "sellingPrice": 10, "profit": 5, "quantity_card": 10, "total_profit": 50, "product_sector": "meat", "imageSrc": "chicken.svg", "legality": "legal"},
                {"productId": 14, "productName": "pork", "wholesalePrice": 7, "sellingPrice": 13, "profit": 6, "quantity_card": 7, "total_profit": 42, "product_sector": "meat", "imageSrc": "pork.svg", "legality": "legal"},
                {"productId": 15, "productName": "sausage", "wholesalePrice": 9, "sellingPrice": 16, "profit": 7, "quantity_card": 4, "total_profit": 28, "product_sector": "meat", "imageSrc": "sausage.svg"}
            ]
        },
        {
            "sector": "household",
            "products": [
                {"productId": 16, "productName": "gloves", "wholesalePrice": 7, "sellingPrice": 12, "profit": 5, "quantity_card": 10, "total_profit": 50, "product_sector": "household", "imageSrc": "gloves.svg", "legality": "legal"},
                {"productId": 17, "productName": "hats", "wholesalePrice": 9, "sellingPrice": 15, "profit": 6, "quantity_card": 7, "total_profit": 42, "product_sector": "household", "imageSrc": "hats.svg", "legality": "legal"},
                {"productId": 18, "productName": "quilts", "wholesalePrice": 10, "sellingPrice": 18, "profit": 8, "quantity_card": 4, "total_profit": 32, "product_sector": "household", "imageSrc": "quilts.svg"}
            ]
        },
        {
            "sector": "illegal",
            "products": [
                {"productId": 19, "productName": "cigarettes", "wholesalePrice": 4, "sellingPrice": 9, "profit": 5, "quantity_card": 18, "total_profit": 90, "product_sector": "other", "imageSrc": "cigarettes.svg", "legality": "illegal"},
                {"productId": 20, "productName": "beer", "wholesalePrice": 5, "sellingPrice": 12, "profit": 7, "quantity_card": 16, "total_profit": 112, "product_sector": "other", "imageSrc": "beer.svg", "legality": "illegal"},
                {"productId": 21, "productName": "wine", "wholesalePrice": 6, "sellingPrice": 15, "profit": 9, "quantity_card": 14, "total_profit": 126, "product_sector": "other", "imageSrc": "wine.svg", "legality": "illegal"},
                {"productId": 22, "productName": "vodka", "wholesalePrice": 7, "sellingPrice": 19, "profit": 12, "quantity_card": 12, "total_profit": 144, "product_sector": "other", "imageSrc": "vodka.svg", "legality": "illegal"},
                {"productId": 23, "productName": "drugs", "wholesalePrice": 10, "sellingPrice": 25, "profit": 15, "quantity_card": 10, "total_profit": 150, "product_sector": "other", "imageSrc": "drugs.svg", "legality": "illegal"}

            ]
        }
    ]
}

# create all the products listed in the json_products

# create all the sectors
for sector in json_products["sectors"]:
    sector_name = sector["sector"].capitalize()
    sector_obj, created = Sector.objects.get_or_create(name=sector_name)
    sector_obj.save()
