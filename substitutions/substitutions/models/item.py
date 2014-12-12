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
    img = Column(Text)
    skuId = Column(Text)
    dollars = Column(Integer)
    cents = Column(Integer)

    def __init__(self, skuId, title, img):
        self.skuId = skuId
        self.title = title
        self.img = img
        self.dollars = 3
        self.cents = 88

    @classmethod
    def get(class_, count):
        return DBSession.query(Item).limit(count)

    @classmethod
    def getBySkuId(class_, skuId):
        return DBSession.query(Item).filter_by(skuId=skuId).first()

    @classmethod
    def getBySkuList(class_, skuList):
        return DBSession.query(Item).filter(Item.skuId.in_(skuList)).all()