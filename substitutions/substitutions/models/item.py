from substitutions.models import (DBSession, Base)

from sqlalchemy import (
    Column,
    Integer,
    Text,
    )


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    url = Column(Text)
    skuId = Column(Text)

    @classmethod
    def get(class_, count):
        return DBSession.query(Item).limit(count)

    @classmethod
    def getBySkuId(class_, skuId):
        return DBSession.query(Item).filter_by(skuId=skuId).first()

    @classmethod
    def getBySkuList(class_, skuList):
        return DBSession.query(Item).filter(Item.skuId.in_(skuList)).all()