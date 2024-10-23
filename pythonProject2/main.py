from operator import truediv

import cianparser

moscow_parser = cianparser.CianParser(location="Москва")
data = moscow_parser.get_newobjects()
additional_settings = {
    "start_page":1,
    "end_page": 2,
    "is_by_homeowner": True,
    "min_price": 1000000,
    "max_price": 1000000000,
    "min_balconies": 1,
    "have_loggia": True,
    "min_house_year": 1990,
    "max_house_year": 2024,
    "min_floor": 3,
    "max_floor": 20,
    "min_total_floor": 5,
    "max_total_floor": 20,
    "house_material_type": 1,
    "metro": "Московский",
    "metro_station": "ВДНХ",
    "metro_foot_minute": 1000,
    "flat_share": 2,
    "only_flat": True,
    "only_apartment": True,
    "sort_by": "price_from_min_to_max",
}
with_saving_csv = true