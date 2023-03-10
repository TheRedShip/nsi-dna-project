# All databases method used for the project
import sqlite3

from constants import DATABASE

def Query(query: str, *toEscape):
    pass

    conn = sqlite3.connect(DATABASE)

    result = conn.execute(query, toEscape or ())
    result = result.fetchall()

    conn.close()

    return result

def InitializeDatabases():
    Query("""
        CREATE TABLE IF NOT EXISTS dna_genes (
            geneId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            originalText TEXT NOT NULL,
            convertedText TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS genes_searches (
            searchId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            geneId INT NOT NULL,
            searchContent TEXT NOT NULL,
            inRow BOOLEAN NOT NULL DEFAULT FALSE,
            FOREIGN KEY (geneId) REFERENCES dna_genes(geneId)
        );

        CREATE TABLE IF NOT EXISTS genes_searches_indexes (
            searchId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            index BIGINT NOT NULL
        );
    """)        