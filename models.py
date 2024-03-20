from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    id_no = Column(Integer())

if __name__ == '__main__':
    engine = create_engine('sqlite:///schools.db')
    Base.metadata.create_all(engine)

    sessioncreator = sessionmaker(bind = engine)
    mysession = sessioncreator()

    tr1 = Teacher(name = "Mercy Nzau", id_no = 222002)
    mysession.add(tr1)
    mysession.commit()

    tr2 = Teacher(name = "Jaduong", id_no = 54321)
    mysession.add(tr2)
    mysession.commit()

    sessioncreator = sessionmaker(bind = engine)
    mysession = sessioncreator()