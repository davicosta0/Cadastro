import json

def exibir_menu():
    print("\n=== Sistema de Cadastro ===")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Apagar usuário")
    print("4. Sair")

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    email = input("Digite o e-mail: ")

    usuario = {"nome": nome, "senha": senha, "email": email}

    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    except FileNotFoundError:
        usuarios = []

    usuarios.append(usuario)

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

    print("Usuário cadastrado com sucesso!")


def listar_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
            if not usuarios:
                print("Nenhum usuário cadastrado.")
                return
            print("\n=== Lista de Usuários ===")
            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. Nome: {usuario['nome']}, E-mail: {usuario['email']}")
    except FileNotFoundError:
        print("Nenhum usuário cadastrado.")

def apagar_usuario():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
            if not usuarios:
                print("Nenhum usuário cadastrado.")
                return
    except FileNotFoundError:
        print("Nenhum usuário cadastrado.")
        return

    listar_usuarios()
    try:
        indice = int(input("Digite o número do usuário que deseja apagar: ")) - 1
        if 0 <= indice < len(usuarios):
            usuario_removido = usuarios.pop(indice)
            with open("usuarios.json", "w") as arquivo:
                json.dump(usuarios, arquivo, indent=4)
            print(f"Usuário '{usuario_removido['nome']}' apagado com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            apagar_usuario()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()