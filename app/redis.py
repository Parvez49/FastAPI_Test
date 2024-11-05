import redis
from fastapi import Depends

# Create a Redis client
def get_redis():
    return redis.Redis(host='redis', port=6379, db=0)

# Dependency
def get_redis_client():
    return get_redis()
