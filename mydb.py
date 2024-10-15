import MySQLdb

dataBase = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password@123'
)


cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE theDBco")

print("All done")