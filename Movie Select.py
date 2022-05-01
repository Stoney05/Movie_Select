import sqlite3

conn = sqlite3.connect('movie.db')

conn.execute('''CREATE TABLE MOVIE
         (ID INT PRIMARY KEY     NOT NULL,
         Movie_name           TEXT    NOT NULL,
         Lead_actor            TEXT     NOT NULL,
         Lead_actress        TEXT       NOT NULL,
         Year_of_release        INT     NOT NULL,
         Director_name      TEXT        NOT NULL);''')
conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (1, 'Beast', 'Vijay', 'Pooja Hegde', 2022, 'Nelson')");
conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (2, 'Annatthe', 'Rajini', 'Nayanthara', 2021, 'Siva')");
conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (3, 'Valimai', 'Ajith', 'Huma Qureshi', 2021, 'H Vinoth')");
conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (4, 'Pushpa', 'Allu Arjun', 'Rashmika', 2021, 'Sukumar')");
conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (5, 'KGF2', 'Yash', 'Srinidhi Shetty', 2022, 'Prashanth Neel')");


conn.commit()
conn.close()



print(" 1. Beast \n 2. Annatthe \n 3. Valimai \n 4. Pushpa \n 5. KGF2")
choice = int(input("Enter your choice: "))

value = conn.execute("SELECT * from MOVIE WHERE ID is "+str(choice))
for val in value:
    A = val[0]
    B = val[1]
    C = val[2]
    D = val[3]
    E = val[4]
    F = val[5]
print("Movie ID      : ",A)
print("Movie Name    : ",B)
print("Lead Actor    : ",C)
print("Lead Actress  : ",D)
print("Released Year : ",E)
print("Director      : ",F)