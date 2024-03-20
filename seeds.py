from models import create_engine, sessionmaker, Base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from faker import Faker

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

fakedata = Faker()

# if __name__ == '__main__':

print('Seeding Teachers')
for i in range(10):
    teacher = Teacher(name=fakedata.name())
    # id_no = Teacher(id_no =fakedata.id_no())
    mysession.add(teacher)
    # mysession.add(id_no)
    # id_no = random.randrange(10000, 50000)
    mysession.commit()

mysession.commit()
print("All teachers seeded ")