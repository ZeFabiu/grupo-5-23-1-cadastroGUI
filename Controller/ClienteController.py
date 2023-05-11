from View.ClienteView import ClienteView
from Model.Cliente import Cliente
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {} #lista de objetos Cliente

    def inicia(self):
        self.__telaCliente.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Cadastrar':
                
                duplicado = False
                codigo = values["codigo"]
                nome = values['nome']
                if (codigo != '') and (nome != ''):
                    if codigo.isdigit():
                        for chave_cliente in self.__clientes.keys():
                            if chave_cliente == codigo:
                                duplicado = True
                        if duplicado == False:
                            self.__clientes[codigo] = nome
                            resultado = "Cliente cadastrado!"
                        else:
                            resultado = "Cliente duplicado, insira um código válido!"
                    else:
                        resultado = "O código deve ser um inteiro!"
                else:
                    resultado = "Preencha os dois campos!"

            elif event == 'Consultar':
                
                codigo = values['codigo']
                if codigo.isdigit():
                    if codigo in self.__clientes.keys():
                        resultado = f"Nome: {self.__clientes[codigo]}, Código: {codigo}"
                    else:
                        resultado = "Cadastro não encontrado"
                else:
                    resultado = "Código deve ser um número inteiro!"
            
            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()


    def busca_codigo(self, codigo):
        try:
            return self.__clientes[codigo]
        except KeyError:
            raise KeyError

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, codigo, nome):
        self.__clientes[codigo] = Cliente(codigo, nome)
    
    def busca_nome(self, nome):
        for key, val in self.__clientes.items():
            if val.nome == nome:
                return key 

        raise LookupError
