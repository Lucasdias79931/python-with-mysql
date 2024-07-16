from Con import MySQLDatabase


if __name__ == "__main__":
    # Substitua com suas próprias credenciais e nome do banco de dados
    db = MySQLDatabase(host="localhost",
                       user="root",
                       password="MISERY1430",
                       database="Biblioteca")
    
    db.connect()

    # Query para selecionar id e escritor da tabela livros
    query = "SELECT id, escritor FROM livro;"
    result = db.execute_query(query)

    if result:
        for row in result:
            print(f"ID: {row[0]}, Escritor: {row[1]}")

    db.disconnect()