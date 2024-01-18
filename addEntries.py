from dbSetup import createdb, Cofounders, Teams
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def fetch(session):
    cofounders = session.query(Cofounders).all()
    for cofounder in cofounders:
        print(cofounder.name)
        for team in cofounder.teams:
            print(f'- {team.team}')



if __name__ == "__main__":

    createdb()


    engine = create_engine('postgresql://graphql:demotest@localhost/postgres')
    Session = sessionmaker(bind = engine)
    session = Session()

    # Doing the data entry for new data points

    # cofounder = Cofounders(name='suyash', designation='ceo')
    # team = Teams(team='galaxeye', leads = cofounder)
    # session.add(cofounder)
    # session.add(team)
    # session.commit()

    # fetching the data from database

    fetch(session)
