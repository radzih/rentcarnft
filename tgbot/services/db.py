from datetime import datetime
from decimal import Decimal
import logging
from typing import Type
from uuid import  UUID
from pydantic import BaseModel
from asgiref.sync import sync_to_async
from enum import Enum
from admin_panel.database.models import CarModel, NFTCar, User

class Language(Enum):
    EN = 'en'
    RU = 'ru'
    IT = 'it'
    

class Car(BaseModel):
    name: str
    address: str
    token_id: int
    owned: bool
    part: int
    secret_code: UUID
    model: str | None = None
    picture_path: str 
    url: str
    rent_days: int | None = None
    earned_money: Decimal | None = None


@sync_to_async
def add_user_to_db(user_id: int) -> User:
    user = User(telegram_id=user_id)
    user.save()
    return user

@sync_to_async
def get_user(telegram_id: int) -> User:
    try:
        return User.objects.get(telegram_id=telegram_id)
    except User.DoesNotExist:
        return None

@sync_to_async 
def get_user_language(user_id: int) -> Type[Language]:
    return User.objects.get(telegram_id=user_id).language

@sync_to_async
def get_secret_codes() -> list[UUID]:
    return list(map(
        UUID, NFTCar.objects.all().values_list('secret_code', flat=True)))

@sync_to_async
def get_avaible_nft_cars() -> list[Car]:
    cars_objects = NFTCar.objects.filter(owned=False)
    cars = []
    for car in cars_objects:
        cars.append(
            Car(
                name=car.name,
                address=car.address,
                token_id=car.token_id,
                owned=car.owned,
                part=car.part,
                secret_code=car.secret_code,
                model=car.model.name,
                picture_path=car.picture.path,
                url=f'https://opensea.io/assets/ethereum/{car.address}/{car.token_id}'
            )
        )
    return cars
    
@sync_to_async
def get_bought_cars() -> list[CarModel]:
    car_models = CarModel.objects.all()
    bought_cars = []
    for car_model in car_models:
        cars = NFTCar.objects.filter(model=car_model).values_list('owned', flat=True)
        logging.info(cars)
        if all(cars):
            bought_cars.append(car_model)
    return bought_cars
            
@sync_to_async
def get_nft(nft_secret_code: UUID) -> NFTCar:
    return NFTCar.objects.get(secret_code=nft_secret_code)           
           
@sync_to_async
def db_add_nft_to_user(user: User, car: NFTCar, owner_addr: str):
    car.owner_addr = owner_addr
    car.owned = True
    car.save()  
    user.owned_cars.add(car)
    
@sync_to_async
def get_user_nfts(user_id: int) -> list[NFTCar]:
    return list(User.objects.get(telegram_id=user_id).owned_cars.all())

@sync_to_async
def add_rent_day(car_model_id: int, earnings: Decimal):
    car_model = CarModel.objects.get(id=car_model_id)
    for car_nft in NFTCar.objects.filter(model=car_model):
        car_nft.rent_days += 1
        car_nft.earned_money += earnings/car_nft.part
        car_nft.save()
        
@sync_to_async
def get_car(car_id: int):
    car = NFTCar.objects.get(id=car_id)
    return Car(
        name=car.name,
        address=car.address,
        token_id=car.token_id,
        owned=car.owned,
        part=car.part,
        secret_code=car.secret_code,
        model=car.model.name,
        picture_path=car.picture.path,
        url=f'https://opensea.io/assets/ethereum/{car.address}/{car.token_id}',
        rent_days=car.rent_days,
        earned_money=car.earned_money
    )
    
@sync_to_async
def get_car_model(car_model_id: int):
    car_model = CarModel.objects.get(id=car_model_id)
    return car_model

@sync_to_async
def get_amount_of_money_to_be_paid(user_id: int):
    user = User.objects.get(telegram_id=user_id)
    money_to_be_paid = 0
    user_cars: list[NFTCar] = user.owned_cars.all()
    for nftcar in user_cars:
        money_to_be_paid += nftcar.earned_money - nftcar.paid_out
    return money_to_be_paid

@sync_to_async
def change_carnft_owner(car: NFTCar, new_owner_addr: str):
    for user in User.objects.all():
        if user.owned_cars.filter(id=car.id).exists():
            user.owned_cars.remove(car)
            user.save()
            car.owned = False
            car.owner_addr = new_owner_addr
            car.save()
            
@sync_to_async
def get_owner_wallet(user_id: int):
    user: User = User.objects.get(telegram_id=user_id)
    user_nft_owner_addresses = user.owned_cars.all(
        ).values_list('owner_addr', flat=True)
    if len(set(user_nft_owner_addresses)) != 1:
        logging.info('Error: car is still owned by owner')
        return None
    return user_nft_owner_addresses[0]

@sync_to_async
def add_paid_out_money(user_id: int):
    user: User = User.objects.get(telegram_id=user_id)
    for nft in user.owned_cars.all():
        nft.paid_out = nft.earned_money
        nft.save()
        
@sync_to_async
def update_user_last_request(user_id: int):
    user = User.objects.get(telegram_id=user_id)
    user.last_request = datetime.now()
    user.save()

@sync_to_async
def change_user_language(user_id: int, language: Type[Language]):
    user: User = User.objects.get(telegram_id=user_id)
    logging.info(language)
    user.language = language
    user.save()