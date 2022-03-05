from opensea import OpenseaAPI

# If I have an API key, use this method here!
# api = OpenseaAPI(apikey="YOUR APIKEY")
api = OpenseaAPI()

guppyCollection = api.collection(collection_slug='guppygang')
