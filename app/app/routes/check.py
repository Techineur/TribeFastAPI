# Author Block
# -----------
# name: Tarun Neeraj
# email: tarun@techineur.com
# GitHub ID: frozenloser
# Description
# -----------
# This file contains the check functions for the route.
# The check functions are called by the main.py file.
# Required Modules
# -------------


# Importing Modules
from fastapi import APIRouter
import redis
import httpx
from redis import ResponseError
from redis import asyncio as aioredis


# Creating a router object with a tag of check
route = APIRouter(
    prefix="/check",
    tags=["check"],
    responses={404: {"description": "Not found"}},
)

@route.get("/v1/health")
async def health():
    return {"status": "ok"}

@route.get("/v1/redis")
async def redis_health():
    try:
        redis.ping()
        return {"status": "ok"}
    except ResponseError:
        return {"status": "error"}
    
