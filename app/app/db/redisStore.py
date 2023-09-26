# Author Block
# -----------
# name: Tarun Neeraj
# email: tarun@techineur.com
# GitHub ID: frozenloser
# Description
# -----------
# This file contains the required api endpoints to store and retrieve information from Redis.


# Importing Modules

from fastapi import APIRouter
import redis
from redis import ResponseError


# Create a router object with a tag of RedisStore
route = APIRouter(
    prefix="/redis",
    tags=["Redis"],
    responses={404: {"description": "Not found"}},
)

@route.get("/v1/redis/keys")
async def redis_keys():
    try:
        keys = redis.keys()
        return {"keys": keys}
    except ResponseError:
        return {"status": "error"}
    
@route.get("/v1/redis/{key}")
async def redis_get(key: str):
    try:
        value = redis.get(key)
        return {"value": value}
    except ResponseError:
        return {"status": "error"}

@route.post("/v1/redis/{key}")
async def redis_set(key: str, value: str):
    try:
        redis.set(key, value)
        return {"status": "ok"}
    except ResponseError:
        return {"status": "error"}
    
# add description to the endpoint
@route.delete("/v1/redis/{key}")
async def redis_delete(key: str):
    try:
        redis.delete(key)
        return {"status": "ok"}
    except ResponseError:
        return {"status": "error"}
