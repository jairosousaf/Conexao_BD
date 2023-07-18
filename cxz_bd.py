import mysql.connector

def conectar():
    host = 'localhost'
    usuario = 'root'
    senha = 'admin'
    banco_de_dados = 'test'
    
    conexao = mysql.connector.connect(
        host = host,
        user = usuario,
        password = senha,
        database = banco_de_dados
    )
    
    return conexao

def criar_tabela(conexao):
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS aluno(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(55),
            data_nascimento DATE,
            cidade_natal VARCHAR(55),
            bairro VARCHAR(55)
        )
    ''')

    conexao.commit()

def cadastrar_aluno(conexao, nome, data_nascimento, cidade_natal, bairro):
    cursor = conexao.cursor()
    
    inserir_query = '''
        INSERT INTO aluno (nome, data_nascimento, cidade_natal, bairro)
        VALUES (%s, %s, %s, %s)
    '''

    valores = (nome, data_nascimento, cidade_natal, bairro)
    cursor.execute(inserir_query,valores)
    conexao.commit()

def main():
    conexao = conectar()
    criar_tabela(conexao)
    
    print('---- Cadastrar Alunos - SENAC ----')
    nome = input('Nome do aluno: ')
    data_nascimento = input('Data de nascimento: (AAAA-MM-DD)')
    cidade_natal = input('Cidade Natal: ')
    bairro = input('Bairro: ')
    
    cadastrar_aluno(conexao, nome, data_nascimento, cidade_natal, bairro)
    
    print('Aluno cadastrado com sucesso!')
    
    conexao.close()
    
if __name__ == "__main__":
    main()