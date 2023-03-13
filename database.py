# All databases method used for the project
import sqlite3

from constants import DATABASE

def Query(query: str, *toEscape):
    conn = sqlite3.connect(DATABASE)

    result = conn.execute(query, toEscape or ())
    result = result.fetchall()

    conn.close()

    return result

def InitializeDatabases():
    Query("""
        CREATE TABLE IF NOT EXISTS dna_genes (
            geneId INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            originalText TEXT NOT NULL,
            convertedText TEXT NOT NULL
        )
    """)
    
    Query("""
        CREATE TABLE IF NOT EXISTS genes_searches (
            searchId INTEGER PRIMARY KEY AUTOINCREMENT,
            geneId INT NOT NULL,
            searchContent TEXT NOT NULL,
            inRow BOOLEAN NOT NULL DEFAULT FALSE,
            FOREIGN KEY (geneId) REFERENCES dna_genes(geneId)
        )
    """)
    
    Query("""
        CREATE TABLE IF NOT EXISTS genes_searches_indexes (
            searchId INTEGER PRIMARY KEY AUTOINCREMENT,
            positionIndex BIGINT NOT NULL
        )
    """)        

    Query("""
        INSERT INTO dna_genes (
                `name`,
                `originalText`,
                `convertedText`
            )
            VALUES (?, ?, ?)
    """, "qsd", "qsd", "qsd")

    print(Query("""SELECT * FROM dna_genes"""))