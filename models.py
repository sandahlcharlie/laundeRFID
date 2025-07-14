from sqlalchemy import (create_engine, Column, Integer, String, DateTime, func)
from sqlalchemy.orm import (declarative_base, Session)

DB_URL = "postgresql+psycopg://launderfid:secret@localhost:5432/launderfid"
engine = create_engine(DB_URL, echo=False, pool_pre_ping=True)
Base = declarative_base()

class WearEvent(Base):
    __tablename__ = "wear_event"
    id = Column(Integer, primary_key=True)
    nfc_uid = Column(String, nullable=False)
    scanned_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)


    if __name__ == "__main__":
        Base.metadata.create_all(engine)
        print("Table wear_event occurred.")
