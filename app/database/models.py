from sqlalchemy import ForeignKey, String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from datetime import datetime


engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3',
                             echo=True)

asyns_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id =  mapped_column(BigInteger)
    balans:  Mapped[str] = mapped_column(String(15))


class AItype(Base):
    __tablename__ = 'ai_types'

    id: Mapped[int] = mapped_column(primary_key=True)
    name:  Mapped[str] = mapped_column(String(25))


class AIModel(Base):
    __tablename__ = 'ai_models'

    id: Mapped[int] = mapped_column(primary_key=True)
    name:  Mapped[str] = mapped_column(String(25))
    ai_type:  Mapped[int] = mapped_column(ForeignKey('ai_types.id'))
    price:  Mapped[str] = mapped_column(String(25))


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    status:  Mapped[str] = mapped_column(String(50))
    user:  Mapped[int] = mapped_column(ForeignKey('users.id'))
    amout:  Mapped[str] = mapped_column(String(15))
    created_at: Mapped[datetime]
    order:  Mapped[str] = mapped_column(String(100))


async def asyns_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
