from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///canteens.db', echo = True)

Base = declarative_base()


class Providers(Base):
    """
    Class, where is described PROVIDER table name and attributes
    PROVIDER table contains information about TalTech canteens providers.
    """
    __tablename__ = 'PROVIDER'

    ID = Column(Integer, primary_key=True)
    ProviderName = Column(String)
    canteen = relationship("Canteens")


def create_providers():
    """
    Create a table in the previously created database.
    Insert into PROVIDER table records about TalTech canteen providers
    """
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        provider1 = Providers(ID=1, ProviderName='bitStop Kohvik OÜ')

        session.add(provider1)

        session.add_all([
            Providers(ID=2, ProviderName='Rahva Toit'),
            Providers(ID=3, ProviderName='Baltic Restaurants Estonia AS'),
            Providers(ID=4, ProviderName='TTÜ Sport OÜ')
        ])
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class Canteens(Base):
    """
    Class, where is described CANTEEN table name and attributes
    CANTEEN table contains information about TalTech canteens.
    """
    __tablename__ = 'CANTEEN'

    ID = Column(Integer, primary_key=True)
    ProviderID = Column(Integer, ForeignKey('PROVIDER.ID'))
    Name = Column(String)
    Location = Column(String)
    time_open = Column(Integer)
    time_closed = Column(Integer)


def create_canteens():
    """
    Create a table in the previously created database.
    Insert into CANTEEN table records about TalTech canteens
    """
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        canteen1 = Canteens(ID=1, ProviderID=1, Name='bitStop KOHVIK', Location='IT College, Raja 4c',
                            time_open=9.30,
                            time_closed=16.00)

        session.add(canteen1)

        session.add_all([
            Canteens(ID=2, ProviderID=2, Name='Economics- and social science building canteen',
                     Location='Akadeemia tee 3, SOC- building',
                     time_open=8.30, time_closed=18.30),
            Canteens(ID=3, ProviderID=2, Name='Library canteen', Location='Akadeemia tee 1/Ehitajate tee 7',
                     time_open=8.30, time_closed=19.00),
            Canteens(ID=4, ProviderID=3, Name='Main building Deli cafe', Location='Ehitajate tee 5, U01 building',
                     time_open=9.00, time_closed=16.30),
            Canteens(ID=5, ProviderID=3, Name='Main building Daily lunch restaurant',
                     Location='Ehitajate tee 5, U01 building',
                     time_open=9.00, time_closed=16.30),
            Canteens(ID=6, ProviderID=2, Name='U06 building canteen', Location='Ehitajate tee 5, U06 building',
                     time_open=9.00, time_closed=16.00),
            Canteens(ID=7, ProviderID=3, Name='Natural Science building canteen',
                     Location='Akadeemia tee 15, SCI building',
                     time_open=9.00, time_closed=16.00),
            Canteens(ID=8, ProviderID=3, Name='ICT building canteen', Location='Raja 15/Mäepealse 1',
                     time_open=9.00, time_closed=16.00),
            Canteens(ID=9, ProviderID=4, Name='Sports building canteen', Location='Männiliiva 7, S01 building',
                     time_open=11.00, time_closed=22.00)
        ])
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def select_time_records_from_canteen():
    """
    Fetch and display from CANTEEN table information about opened canteens during given period of time
    Print human readable information about canteen as a output
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        result = session.query(Canteens).filter(Canteens.time_open < 16.15, Canteens.time_closed > 18.00)

        for row in result:
            print("Name = ", row.Name, " in ", row.Location)
            print(f"Is open from ", '%0.2f' % row.time_open, "to ", '%0.2f' % row.time_closed, "\n")
    except:
        session.rollback()
        raise
    finally:
        session.close()


def select_special_provider_from_canteen():
    """
    Fetch and display from CANTEEN table information about opened canteens with seleted food provider
    Print human readable information about canteen as a output
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        result = session.query(Canteens, Providers). \
             join(Providers, Providers.ID == Canteens.ProviderID). \
             filter(Providers.ProviderName == "Rahva Toit")

        for row in result:
            print("Name = ", row.Canteens.Name, " in ", row.Canteens.Location)
            print(f"Is open from ", '%0.2f' % row.Canteens.time_open, "to ",
                  '%0.2f' % row.Canteens.time_closed, "\n")
            print("Their food provider is ", row.Providers.ProviderName, "\n")
    except:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":

    # create_providers()   # Create table Provider and insert information about Providers
    # create_canteens()    # Create table Canteen and insert information about Canteens

    select_time_records_from_canteen()
    select_special_provider_from_canteen()

