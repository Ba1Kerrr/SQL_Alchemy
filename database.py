from sqlalchemy import create_engine,text,insert


engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/sqlalchemy_tuts", 
    echo=False)


def create_Database(database,count_columns,first_column,first_type):
    with engine.connect() as conn:
            result = conn.execute(text(f"""
                CREATE TABLE {database}(
                    {first_column} {first_type}
                    )
        """))
            conn.commit
    for i in range(count_columns):
        column = input(f"Enter column {i}")
        type = input(f"Enter type {i}")
        with engine.connect() as conn:
            result = conn.execute(text(f"""
                ALTER TABLE {database} ADD {column} {type}
        """))
    conn.commit()


#select my databae
def select_values():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM auth"))
        for row in result:
            x = row[0]
    return row
 

#insert data to my database
def insert_values():
    with engine.connect() as conn:
        result = insert(conn).values(43,'Alex','54321@gmail.com','12345')
        conn.commit()

create = create_Database("name",2,"age","INTEGER") #Database(database,count_columns,first_column,first_type)
ins = insert_values()
select = select_values()
create()