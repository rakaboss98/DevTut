import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from dbSetup import Cofounders, Teams

class CofoundersType(SQLAlchemyObjectType):
    class Meta:
        model = Cofounders

class TeamsType(SQLAlchemyObjectType):
    class Meta:
        model = Teams

class Query(graphene.ObjectType):
    all_cofounders = graphene.List(CofoundersType)

    def resolve_all_cofounders(self, info):
        query = CofoundersType.get_query(info)
        return query.all()

schema = graphene.Schema(query=Query)

if __name__ == "__main__":
    query_string = '{ allCofounders { name, teams { team }}}'
    result = schema.execute(query_string)
    print(result.data['allCofounders'])