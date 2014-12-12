from substitutions.models import (DBSession, Base)

from sqlalchemy import (
    Column,
    Integer,
    Text,
    Unicode
    )


class Item(Base):
    __tablename__ = 'item'
    sku_id = Column(Unicode(255), primary_key=True)
    title = Column(Text)
    product_brand = Column(Text)
    image_thumbnail_url = Column(Text)
    image_large_url = Column(Text)
    product_category = Column(Text)

    @classmethod
    def get(class_, count):
        return DBSession.query(Item).limit(count)

    @classmethod
    def getBySkuId(class_, skuId):
        return DBSession.query(Item).filter_by(sku_id=skuId).first()

    @classmethod
    def getBySkuList(class_, skuList):
        return DBSession.query(Item).filter(Item.sku_id.in_(skuList)).all()