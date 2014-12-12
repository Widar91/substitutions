import math
from substitutions.models import (DBSession, Base)

from sqlalchemy import (
    Column,
    Integer,
    Text,
    Unicode,
    Float
    )


class Item(Base):
    __tablename__ = 'item'
    sku_id = Column(Unicode(255), primary_key=True)
    title = Column(Text)
    product_brand = Column(Text)
    image_thumbnail_url = Column(Text)
    image_large_url = Column(Text)
    product_category = Column(Text)
    unit_price = Column(Text)

    @property
    def dollars(self):
        if not self.unit_price:
            return '0'


        return self.unit_price.split('.')[0]

    @property
    def cents(self):
        if not self.unit_price:
            return  '00'

        split = self.unit_price.split('.')
        if len(split) <= 1:
            return '00'
        
        return split[1]

    @classmethod
    def get(class_, count):
        return DBSession.query(Item).limit(count)

    @classmethod
    def getBySkuId(class_, skuId):
        return DBSession.query(Item).filter_by(sku_id=skuId).first()

    @classmethod
    def getBySkuList(class_, skuList):
        return DBSession.query(Item).filter(Item.sku_id.in_(skuList)).all()