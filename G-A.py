import sqlite3

MASTER_PASSWORD = "123456"

conn = sqlite3.connect ('passwords.db') 

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXITS users (
        service TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
);
''')

def menu ():
    print ("**********")
    print("* i : inserir nova senha*")
    print("* l : listar serviços salvos*")
    print("* r : recuperar uma senha *")
    print(" s : sair                  *")

while True:
    menu()
    op = input (" oque deseja fazer?")
    if op not in ['l', 'i','r','s']:
        print('Opção inválida')
        continue

    if op == 's' :
        break

    conn.close()