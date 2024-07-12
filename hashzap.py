#titulo
#botao 'iniciar chat'
    #abrir popup/modal/alerta
        #titulo: bem vindo ao hashzap
        #campo de texto para nome
        #botao entrar no chat
            #sumir com o titulo e botao inicial
            #fechar o popup
            #criar o chat (com a mensagem  de nome do usuario entrou no chat)
            #embaixo do chat:
                #campo de texto
                #botao
                    #vai aparecer a msg no chat com o nome do usuario

#importar o flet

import flet as ft
#criar a função principal do sistema 
def main(pagina):
    #criar alguma coisa
    #criar o titulo
    titulo = ft.Text('Hashzap')
    

    titulo_janela = ft.Text('Bem vindo ao Hashzap')
    campo_nome_usuario = ft.TextField(label='Escreva seu nome no chat')
    texto_mensagem = ft.TextField(label='Escreva sua mensagem')
    
    def enviar_mensagem(evento):
        #enviar a msg no chat
        texto = f'{campo_nome_usuario.value}: {texto_mensagem.value}'
        pagina.pubsub.send_all(texto)
        texto_mensagem.value = ''
           # usuario: mensagem
            #limpar campo de msg
        pagina.update()
    
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    chat = ft.Column()
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])
    def entrar_chat(evento):
        #sumir com o titulo e botao inicial
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        #fechar o popup
        janela.open = False
        #criar o chat (com a mensagem  de nome do usuario entrou no chat)
        #criar o campo de texto
        #criar botao enviar
        pagina.add(chat)
        pagina.add(linha_mensagem)
        #escrever a msg: usuário entrou no chat
        
        texto_entrou_chat = f'{campo_nome_usuario.value} entrou no chat'
        pagina.pubsub.send_all(texto_entrou_chat)
        pagina.update()
        
    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)

    janela = ft.AlertDialog(
         title=titulo_janela,
         content=campo_nome_usuario,
         actions=[botao_entrar]                   
                            )

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
    botao_iniciar = ft.ElevatedButton('Iniciar conversa', on_click=abrir_popup)
    #colocar na pagina 
    #adiconar o titulo na pagina 
    pagina.add(titulo)
    pagina.add(botao_iniciar)
#executar o sistema 

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel) #criar o tunel de comunicação 
ft.app(main, view=ft.WEB_BROWSER)