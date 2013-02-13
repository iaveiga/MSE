'''
MetaSearchEngine
'''

import sqlite3


'''
Carga la base de datos y retorna un cursor
'''
def loadDB():
    conn = sqlite3.connect("Engines.db")
    print "Base cargada correctamente"
    c = conn.cursor()
    return c


def loadEngines():
    cursor = loadDB()
    engines = []
    
    for row in cursor.execute("SELECT url from ENGINE"):
        engines.append(row)
    return engines

def results(query):
    
