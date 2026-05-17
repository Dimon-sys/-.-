from re import *

#Российские номера
rus_light = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\s?\d{2,3}' # легковой
rus_mia = r'[АВЕКМНОРСТУХ]\d{3}\s?\d{2,3}' # синий (МВД)
rus_motocycle_or_trailer = r'[АВЕКМНОРСТУХ]{2}\d{4}\s?\d{2,3}' # прицеп / мотоцикл
rus_taxi = r'[АВЕКМНОРСТУХ]{2}\d{3}\s?\d{2,3}' # такси
rus_transit = r'Т\d{3,4}\s?\d{2,3}' # транзит
rus_old = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\s?\d{1,2}' # старый формат
#Зарубежные номера
foreign = r'^(?=[A-Z0-9 -]{4,12}$)[A-Z]{1,3}[ -]?\d{1,4}(?:[ -]?[A-Z]{0,3})?(?:\s?\d{1,3})?$'


COMBINED_PLATE_PATTERN = compile(
    rf'^(?:{rus_light}|{rus_mia}|{rus_motocycle_or_trailer}|{rus_taxi}|{rus_transit}|{rus_old}|{foreign})$', IGNORECASE
)


def is_plate(plate):
    return bool(COMBINED_PLATE_PATTERN.match(plate.upper()))

print(is_plate(input()))