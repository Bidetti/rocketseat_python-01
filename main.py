contatos_agendas = {}

class Contato:
    def __init__(self, nome=None, telefone=None, email=None, favorito=False):
        self._id = len(contatos_agendas) + 1
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

    def add_contato(self, nome, telefone, email, favorito=False):
        try:
            contatos_agendas[nome] = {'telefone': telefone, 'email': email, 'favorito': favorito}
            return True
        except Exception as e:
            print(f'Erro ao adicionar contato: {e}')
            return False

    def lista_contatos(self):
        try:
            print('--- Contatos ---')
            if not contatos_agendas:
                print('Nenhum contato na agenda!')
                return False
            for contato in sorted(contatos_agendas.items(), key=lambda x: x[1]['favorito'], reverse=True):
                print(f'Nome: {contato[0]}, Telefone: {contato[1]["telefone"]}, Email: {contato[1]["email"]}, Favorito: {"✓" if contato[1]["favorito"] else "✗"}')
            print('--- Fim da lista ---')
            return True
        except Exception as e:
            print(f'Erro ao listar contatos: {e}')
            return False

    def edit_contato(self, nome, telefone, email, favorito=False):
        try:
            contatos_agendas[nome] = {'telefone': telefone, 'email': email, 'favorito': favorito}
            return True
        except Exception as e:
            print(f'Erro ao editar contato: {e}')
            return False

    def add_favorito(self, nome):
        try:
            contatos_agendas[nome]['favorito'] = True
            return True
        except Exception as e:
            print(f'Erro ao adicionar favorito: {e}')
            return False

    def remove_favorito(self, nome):
        try:
            contatos_agendas[nome]['favorito'] = False
            return True
        except Exception as e:
            print(f'Erro ao remover favorito: {e}')
            return False

    def lista_favoritos(self):
        try:
            print('--- Contatos Favoritos ---')
            for contato in sorted(contatos_agendas.items(), key=lambda x: x[1]['favorito'], reverse=True):
                if contato[1]['favorito']:
                    print(f'Nome: {contato[0]}, Telefone: {contato[1]["telefone"]}, Email: {contato[1]["email"]}, Favorito: {"✓" if contato[1]["favorito"] else "✗"}')
            print('--- Fim da lista ---')
            return True
        except Exception as e:
            print(f'Erro ao listar favoritos: {e}')
            return False

    def remove_contato(self, nome):
        try:
            contatos_agendas.pop(nome)
            return True
        except Exception as e:
            print(f'Erro ao remover contato: {e}')
            return False


def main():
    agenda = Contato()
    first_time = True
    while True:
        if not first_time:
            input('\nPressione Enter para continuar...')
        else:
            first_time = False
        print(
        '\n--- Agenda de Contatos ---\nLista de comandos:\n1 - Adicionar contato\n2 - Listar contatos\n3 - Editar '
        'contato\n4 - Adicionar contato favorito\n5 - Remover contato favorito\n6 - Listar contatos favoritos\n7 - '
        'Remover contato\n8 - Sair')
        comando = input('Digite o comando: ')
        if comando == '1':
            nome = input('Digite o nome: ')
            telefone = input('Digite o telefone: ')
            email = input('Digite o email: ')
            favorito = input('É favorito? (S/N): ')
            if favorito.upper() == 'S':
                favorito = True
            else:
                favorito = False
            agenda.add_contato(nome, telefone, email, favorito)
        elif comando == '2':
            agenda.lista_contatos()
        elif comando == '3':
            nome = input('Digite o nome do contato que deseja editar: ')
            telefone = input('Digite o novo telefone: ')
            email = input('Digite o novo email: ')
            favorito = input('É favorito? (S/N): ')
            if favorito.upper() == 'S':
                favorito = True
            else:
                favorito = False
            agenda.edit_contato(nome, telefone, email, favorito)
        elif comando == '4':
            agenda.lista_contatos()
            nome = input('Digite o nome do contato que deseja adicionar aos favoritos: ')
            agenda.add_favorito(nome)
        elif comando == '5':
            agenda.lista_favoritos()
            nome = input('Digite o nome do contato que deseja remover dos favoritos: ')
            agenda.remove_favorito(nome)
        elif comando == '6':
            agenda.lista_favoritos()
        elif comando == '7':
            agenda.lista_contatos()
            nome = input('Digite o nome do contato que deseja remover: ')
            agenda.remove_contato(nome)
        elif comando == '8':
            break
        else:
            print('Comando inválido!')

if __name__ == '__main__':
    main()