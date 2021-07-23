import sqlite3
import os

from discord import user
class sql():

    """
    0 Member Role
    1 Welcome Channel
    2 Logs Channel
    3 Muted Role
    """


    # Create new server table
    def create(serverName: str):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        ex = cur.execute(f"""CREATE TABLE '{serverName}'(
        MemberRole INTEGER,
        WelcomeID INTEGER,
        LogsID INTEGER,
        MutedID INTEGER
        )
        """)
        print(f"Executed Table For Server: {serverName}")
        conn.commit()
        conn.close()
    
    def createSwearWordsTable(serverName: str):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        ex = cur.execute(f"""CREATE TABLE '{serverName}-swearwords'(word TEXT NOT NULL)
        """)
        print(f"Executed Swear Words Table For Server: {serverName}")
        conn.commit()
        conn.close()
    
    def addSwearWords(serverName: str, swearword: str):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        ex = cur.execute(f"""INSERT INTO '{serverName}-swearwords'(word) VALUES('{swearword}')""")
        print(f"Added {swearword} to {serverName}")
        conn.commit()
        conn.close()
    
    def getallswearwords(serverName):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM '{serverName}-swearwords'")
        record = cur.fetchall()

        words = []
        for i in range(len(record)):
            words.append(record[i][0])
        
        return words
    # Gets the table information from specefeid server id
    def getTableForServer(serverName):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM '{serverName}'")
        record = cur.fetchall()

        for i in record:
            return f"Member Role ID: {str(i[0])}\nWelcome Channel ID: {str(i[1])}\nLogs Channel ID: {str(i[2])}\nMuted Role ID: {str(i[3])}"

    # Gets a specific attrabute from a specified server id
    def getAttributeFromServer(serverName, queryName):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        try:
            cur.execute(f"SELECT {queryName} FROM '{serverName}'")
            record = cur.fetchall()
            return record[0]
        except sqlite3.Error as er:
            return f"**Sql Error**: {er}"
    
    # Checks if the tale does exist based of server id
    def validateServerTable(serverName):
        try:
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM '{serverName}'")
            return True
        except sqlite3.OperationalError:
            return False
    
    # Adds all the vales to the table
    def addValue(serverName, MemberRole, WelcomeID, LogsID, MutedID):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO '{serverName}' (MemberRole, WelcomeID, LogsID, MutedID)
        VALUES ({MemberRole}, {WelcomeID}, {LogsID}, {MutedID})""")
        print(f"Entered Values Into Table: " + str(serverName))
        conn.commit()
        conn.close()
    
    
    def clearDB():
        os.remove("database.db")
        with open("database.db", "w") as s:
            pass
        return "Done!"

    def getSpecific(serverID, number):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM '{serverID}'")
        record = cur.fetchall()

        for i in record:
            return i[number]
    
    def removeSwearWords(serverName: str, swearword: str):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        ex = cur.execute(f"""DELETE FROM '{serverName}-swearwords' WHERE word='{swearword}'""")
        print(f"Removed {swearword}")
        conn.commit()
        conn.close()

    def createWarningsTable(serverName: str):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        ex = cur.execute(f"""CREATE TABLE '{serverName}-warnings'(userID INTEGER NOT NULL, reason TEXT NOT NULL)
        """)
        print(f"Executed Warnings Table For Server: {serverName}")
        conn.commit()
        conn.close()

    def addWarnings(serverName: str, userID: str, reason: str):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        ex = cur.execute(f"""INSERT INTO '{serverName}-warnings'(userID, reason) VALUES('{userID}', '{reason}')""")
        print(f"Added {userID} to {serverName}")
        conn.commit()
        conn.close()
    
    def getallwarnings(serverName, userID):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        record = cur.execute(f"SELECT * FROM '{serverName}-warnings' WHERE userID = '{userID}'").fetchall()

        words = []
        for i in range(len(record)):
            words.append(f"User: {record[i][0]} || Warn: {record[i][1]}")
        
        return words
    
    
    
