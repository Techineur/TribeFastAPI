from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class RoleScope(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    role_id: int = Field(default=None, foreign_key="role.id")
    scope_id: int = Field(default=None, foreign_key="scope.id")

    role: Optional["Role"] = Relationship(back_populates="roles")
    scope: Optional["Scope"] = Relationship(back_populates="scope")


class Scope(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    roles: List["Role"] = Relationship(back_populates="scope", link_model=RoleScope)


class Role(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    users: List["User"] = Relationship(back_populates="role")
    scope: List["Scope"] = Relationship(back_populates="roles", link_model=RoleScope)




class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    phone_number: str
    password: str
    is_active: bool = True
    roleID: int = Field(default=None, foreign_key="role.id")

    role: Optional["Role"] = Relationship(back_populates="users")

class BlacklistTokens(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    token: str
    expires: datetime
    revoked: bool = False
