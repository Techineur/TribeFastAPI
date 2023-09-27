import functools
import json
import logging
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Dict
from typing import Iterable
from typing import List
from typing import Tuple
from typing import Union

import redis
import httpx
from redis import ResponseError
from redis import asyncio as aioredis
from fastapi import BackgroundTasks
from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException

from app.config import Settings
from app.routes.check import route as check_route
from app.db.redisStore import route as redis_route
from app.db.dbConfig import create_db_and_tables




log = logging.getLogger(__name__)
config = Settings()
app = FastAPI(title=config.title)
app.include_router(check_route)
app.include_router(redis_route)

redis = redis.from_url(config.redis_url, decode_responses=True)

create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}

