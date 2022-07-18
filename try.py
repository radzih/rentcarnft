import asyncio
from importlib.metadata import metadata
import json
from aiohttp import ClientSession
import requests

url = "https://deep-index.moralis.io/api/v2/nft/0xffed35bc5fb514098df353840e4eda01c4c7c776/1"


headers = {'X-API-Key': 'h1LSWkPDPYpxU0ON6kanXX0iXMzN50tRfpnOUGe82KAgEVjJ4b1LLGvIyOAfMNcX'}

response = requests.get(url.format(address='0x495f947276749ce646f68ac8c248420045cb7b5e'), headers=headers)
with open('test.json', 'w') as f:
    json.dump(response.json(), f, indent=4)
async def main():
    async with ClientSession(headers=headers) as session:
            async with session.get(
                f'https://deep-index.moralis.io/api/v2/nft/0xa7d8d9ef8d8ce8992df33d8b8cf4aebabd5bd270/326000067'
            ) as response:
                data = await response.json()
    print(data)
    
asyncio.run(main())