from cs50 import SQL

# connect to the database
db = SQL("sqlite:///coasters.db")

# this function will grab all the unique countries from our database
def get_all_countries():
  rows = db.execute("""SELECT DISTINCT(country)
                    FROM coasters ORDER BY country""")
  return rows