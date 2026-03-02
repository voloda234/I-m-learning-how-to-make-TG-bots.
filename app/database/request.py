from app.database.models import asyns_session
from app.database.models import User, AIModel, AItype, Order
from sqlalchemy import select, update, delete, desc
from decimal import Decimal


async def set_user(tg_id):
     async with asyns_session() as session:
          user = await session.scalar(select(User).where(User.tg_id == tg_id))

          if not user:
               session.add(User(tg_id=tg_id, balans='0'))
               await session.commit()


async def get_user(tg_id):
     async with asyns_session() as session:
          return await session.scalar(select(User).where(User.tg_id == tg_id))
     

async def calculate(tg_id, summ, model_name):
     async with asyns_session() as session:
          user = await session.scalar(select(User).where(User.tg_id == tg_id))
          model = await session.scalar(select(AIModel).where(AIModel.name == model_name))
          new_balance = Decimal(Decimal(user.balans) - (Decimal(model.price) * Decimal(summ)))
          await session.execute(update(User).where(User.id == user.id).values(balans = str(new_balance)))
          await session.commit()
