from database.schema import Schema


def main():
    schema = Schema()
    schema.create_tables()

    print("Database created successfully!")


if __name__ == "__main__":
    main()