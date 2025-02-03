from redisvl.index import SearchIndex
from redis.asyncio import Redis
import os


async def configure_redis():
    redis_url = os.getenv('REDIS_URL')
    index = SearchIndex.from_yaml('./redisInit/redis.yml')
    index.connect(redis_url=redis_url)
    
    index.create()
    return index

