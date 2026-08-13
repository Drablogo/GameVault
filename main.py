from database.schema import Schema
from database.seed import Seed


def main():

    schema = Schema()
    schema.create_tables()

    seed = Seed()
    seed.populate()


if __name__ == "__main__":
    main()