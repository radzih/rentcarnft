from pathlib import Path
from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
from dotenv import load_dotenv

# Load environment variables into this file
# load_dotenv()

# # This PRIVATE KEY is coming from your environment variables. Make sure to never put it in a tracked file or share it with anyone.
# PRIVATE_KEY = '19502b5726a304be86aa83d4b04dda1ce2856bb394ac38c4d19ccdd464c0e660'

# # Set the network you want to operate on, or add your own RPC URL here
# NETWORK = "rinkeby"

# # Finally, you can create a new instance of the SDK to use
# sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, NETWORK)

# NFT_COLLECTION_ADDRESS = "0x250e674ec63df4273c493c419d9f1e44035cbdac"
# nft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)


# nft_collection.mint(NFTMetadataInput.from_json({
#     "name": "Cool NFT",
#     "description": "Minted with the Python SDK!",
#     "image": "ipfs://QmdFeKxt6FJUNvaGgzYuYNRbpNWyHxP2PFzjsgPf1eD2Jf"
# }))

# print(nft_collection.balance())
print( Path(__file__).parent)