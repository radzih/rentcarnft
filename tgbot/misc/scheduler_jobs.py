from decimal import Decimal
from aiohttp import ClientSession

from admin_panel.database.models import NFTCar
from tgbot.config import Config

from tgbot.services.db import add_rent_day, change_carnft_owner

async def get_owner_nft(token_address: str, token_id: str, config: Config):
    headers = {'X-API-Key': config.misc.moralis_api_token}
    async with ClientSession(headers=headers) as session:
        async with session.get(
            f'https://deep-index.moralis.io/api/v2/nft/{token_address}/{token_id}'
        ) as response:
            data = await response.json()
            return data.get('owner_of')
        
async def add_rent_day_job(car_model_id: int, earnings: Decimal):
    await add_rent_day(car_model_id, earnings)
    
async def check_owner(car: NFTCar, config: Config):
    owner_addr = await get_owner_nft(car.address, car.token_id, config)
    if owner_addr == car.owner_addr:
        return
    await change_carnft_owner(car, owner_addr)
    
    
    
    
    