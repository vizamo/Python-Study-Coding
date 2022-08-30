import sqlite3


def open_dinners_db():
    """
    Open SQLite database for TalTech Diners database
    """
    global conn
    conn = sqlite3.connect('diners.db')
    print("Opened database successfully")


def create_canteen_table():
    """
    Create a table in the previously created database.
    CANTEEN table contains information about TalTech canteens.
    """
    conn.execute('''CREATE TABLE CANTEEN 
             (ID            INT            NOT NULL    PRIMARY KEY,
             ProviderID     INT            NOT NULL,
             Name           VARCHAR(150)   NOT NULL,
             Location       VARCHAR(250)   NOT NULL,
             time_open      INT            NOT NULL,
             time_closed    INT            NOT NULL,
             FOREIGN KEY(ProviderID) REFERENCES PROVIDER(ID)
            );''')
    print("Table CANTEEN created successfully")


def create_provider_table():
    """
    Create a table in the previously created database.
    PROVIDER table contains information about TalTech canteens providers.
    """
    conn.execute('''CREATE TABLE PROVIDER 
             (ID            INT            NOT NULL    PRIMARY KEY,
             ProviderName   VARCHAR(150)   NOT NULL
            );''')
    print("Table PROVIDER created successfully")


def insert_provider_data():
    """
    Insert into Provider table records about TalTech canteen providers
    """
    conn.execute('''INSERT INTO PROVIDER (ID, ProviderName) \
                    VALUES (1, "bitStop Kohvik OÜ");''')
    conn.execute('''INSERT INTO PROVIDER (ID, ProviderName) \
                    VALUES 
                    (2, "Rahva Toit"),
                    (3, "Baltic Restaurants Estonia AS"),
                    (4, "TTÜ Sport OÜ")
                    ;''')
    conn.commit()
    print("Records in Provider table inserted successfully")


def insert_canteen_data():
    """
    Insert into Provider table records about TalTech canteens
    """
    conn.execute('''INSERT INTO CANTEEN (ID, ProviderID, Name, Location, time_open, time_closed) \
                    VALUES (1, 1, "bitStop KOHVIK", "IT College, Raja 4c", 
                    9.30, 16.00);''')

    conn.execute('''INSERT INTO CANTEEN (ID, ProviderID, Name, Location, time_open, time_closed) \
                    VALUES 
                    (2, 2, "Economics- and social science building canteen", "Akadeemia tee 3, SOC- building", 
                    8.30, 18.30),
                    (3, 2, "Library canteen", "Akadeemia tee 1/Ehitajate tee 7", 
                    8.30, 19.00),
                    (4, 3, "Main building Deli cafe", "Ehitajate tee 5, U01 building", 
                    9.00, 16.30),
                    (5, 3, "Main building Daily lunch restaurant", "Ehitajate tee 5, U01 building", 
                    9.00, 16.30),
                    (6, 2, "U06 building canteen", "Ehitajate tee 5, U06 building", 
                    9.00, 16.00), 
                    (7, 3, "Natural Science building canteen", "Akadeemia tee 15, SCI building", 
                    9.00, 16.00),
                    (8, 3, "ICT building canteen", "Raja 15/Mäepealse 1", 
                    9.00, 16.00),
                    (9, 4, "Sports building canteen", "Männiliiva 7, S01 building", 
                    11.00, 22.00)                                   
                    ;''')
    conn.commit()
    print("Records in Canteen table inserted successfully")


def select_time_records_from_canteen():
    """
    Fetch and display from CANTEEN table information about opened canteens during given period of time
    Print human readable information about canteen as a output
    """
    cursor = conn.execute('''SELECT Name, Location, time_open, time_closed from CANTEEN 
                             WHERE time_open <= 16.15 AND time_closed >= 18.00;''')
    for row in cursor:
        print("Name = ", row[0], " in ", row[1])
        print(f"Is open from ", '%0.2f' % row[2], "to ", '%0.2f' % row[3], "\n")
    print("Operation done successfully")


def select_canteen_provider_records_from_canteen():
    """
    Fetch and display from CANTEEN table information about canteens with given food provider
    Print human readable information about canteen as a output
    """
    cursor = conn.execute('''SELECT CANTEEN.Name, CANTEEN.Location, CANTEEN.time_open, CANTEEN.time_closed, 
                             PROVIDER.ProviderName from CANTEEN
                             JOIN PROVIDER on PROVIDER.ID == CANTEEN.ProviderID
                             WHERE ProviderName == "Rahva Toit";''')
    for row in cursor:
        print("Name = ", row[0], " in ", row[1])
        print(f"Is open from ", '%0.2f' % row[2], "to ", '%0.2f' % row[3], "\n")
        print("Their food provider is ", row[4], "\n")
    print("Operation done successfully")


def close_dinners_db():
    """
    Close connection to Dinners database opened from open_dinners_db()
    """
    conn.close()
    print("Connection to database closed")


if __name__ == "__main__":
    open_dinners_db()   # Open DB connection

    create_provider_table()   # Create table Provider
    create_canteen_table()   # Create table Canteen

    insert_provider_data()   # Insert information about Providers
    insert_canteen_data()   # Insert information about Canteens

    select_time_records_from_canteen()
    select_canteen_provider_records_from_canteen()

    close_dinners_db()
