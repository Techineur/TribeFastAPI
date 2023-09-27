# Author Block
# -----------
# name: Tarun Neeraj
# email: tarun@techineur.com
# GitHub ID: frozenloser
# Description
# -----------
# This file contains the endpoints for the auth route.


# Importing Modules
from app.db.models import User, Role, Scope, RoleScope
from app.db.dbConfig import engine
from app.config import config
from app.db.redisStore import redis

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer, OAuth2, SecurityScopes
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel

from typing import Optional, List
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlmodel import Session, select, insert, update

# Creating a router object with a tag of auth
route = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

