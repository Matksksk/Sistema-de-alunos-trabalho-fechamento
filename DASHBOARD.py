import tkinter as tk
from tkinter import messagebox
import banco
logado=False
azul="#014683"  
 
def janela_login():
    if logado==True:
        return
    login = tk.Toplevel()
    login.title("Login")
    login.geometry("500x300")
    login.resizable(False, False)
    login.configure(bg="#014683")

    login.grid_columnconfigure(0, weight=1)
    login.grid_columnconfigure(1, weight=1)
    login.transient(dashboard)
    login.focus_set()
    titulo=tk.Label(
        login,
        text="LOGIN",
        bg="#1476CB",
        fg="white",
        font=("Arial",25,"bold"),
        width=20
    )
    titulo.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=(15,10)
    )
    label1 = tk.Label(
        login,
        text="Usuário",
        bg="#014683",
        fg="white",
        font=("Arial",15,"bold")
    )
    label1.grid(
        row=1,
        column=0,
        columnspan=2,
        pady=(15, 5)
    )
    usuario = tk.Entry(
        login,
        width=20
        )
    usuario.grid(
        row=2,
        column=0,
        columnspan=2
    )
    label2 = tk.Label(
        login,
        text="Senha",
        bg="#014683",
        fg="white",
        font=("Arial",15,"bold")
    )
    label2.grid(
        row=3,
        column=0,
        columnspan=2,
        pady=(15, 5)
    )
    senha = tk.Entry(
        login,
        show="*",
        width=20
    )
    senha.grid(
        row=4,
        column=0,
        columnspan=2
    )
    def mostrar ():
        if var_mostrar.get():
            senha.config(show="")
        else:
            senha.config(show="*")
            
    var_mostrar=tk.BooleanVar()
    mostrar_senha=tk.Checkbutton(
        login,
        text="Mostrar senha",
        variable=var_mostrar,
        command=mostrar,
        bg="#014683",
        fg="white"
    )
    mostrar_senha.grid(
        row=5,
        column=1,
        pady=(3,0)
    )
    def verificador_login():
        erros=0
        caracteres_usuario=len(usuario.get())
        caracteres_senha=len(senha.get())
        if caracteres_usuario==0 and caracteres_senha==0:
            messagebox.showerror(" ","Insira suas informações de login")
            return
        if caracteres_usuario<3:
            messagebox.showwarning("Usuário","Mínimo de 3 caracteres")
            erros+=1
        if caracteres_senha<8:
            messagebox.showwarning("Senha inválida","*Insira uma senha de no mínimo 8 Caracteres*")
            erros+=1
        if erros==0:
            global logado
            banco.cadastrar_usuario(
                usuario.get(),
                senha.get()
            )
            logado=True
            nome=usuario.get()
            login_botao.configure(
                text=nome
              )
            login.destroy()
            messagebox.showinfo("","Login bem sucedido")
    enviar=tk.Button(
        login,
        text="Login",
        bg="#0E5EA4",
        fg="white",
        width=15,
        command=lambda:verificador_login()
    )
    enviar.grid(
        row=6,
        column=0,
        columnspan=2,
        pady=(25,5)
    )
    
def faca_login():
    messagebox.showinfo("Faça login!","Faça login para acessar recursos") 
    
def cadastrar_alunos():
    if logado==False:
        faca_login()
    elif logado==True:
        cadastro = tk.Toplevel()
        cadastro.title("Cadastro")
        cadastro.geometry("700x500")
        cadastro.resizable(False, False)
        cadastro.configure(bg="#014683")

        cadastro.grid_columnconfigure(0, weight=1)
        cadastro.grid_columnconfigure(1, weight=1)
        cadastro.transient(dashboard)
        cadastro.focus_set()
        header_cadastro=tk.Frame(
            cadastro,
            height=100,
            bg="#066FCA"
            )
        header_cadastro.grid_propagate(False)
        header_cadastro.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew"
        )
        text_cadastro=tk.Label(
            header_cadastro,
            text="Cadastro de alunos",
            font=("Arial",20,"bold"),
            bg="#066FCA",
            fg="#FFFFFF")
        text_cadastro.grid(
            row=0,
            column=1,
            columnspan=2,
            padx=(15,15),
            pady=(5,5)
        )
        tk.Label(
            cadastro,
            text="Nome do aluno",
            font=("Arial",15,"bold"),
            fg="#FFFFFF",
            bg=azul
        ).grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(5,5)
        )
        nome=tk.Entry(
            cadastro,
            width=25,
        )
        nome.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=(5,5)
        )
        tk.Label(
            cadastro,
            text="RM",
            font=("Arial",15,"bold"),
            fg="#FFFFFF",
            bg=azul
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=(5,5))
        rm=tk.Entry(
            cadastro,
            width=25,
        )
        rm.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(5,5)
        )
        tk.Label(
            cadastro,
            text="Turma(DS/ADM)",
            font=("Arial",15,"bold"),
            fg="#FFFFFF",
            bg=azul
        ).grid(
            row=5,
            column=0,
            columnspan=2,
            pady=(5,5))
        turma=tk.Entry(
            cadastro,
            width=25,
        )
        turma.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=(5,5)
        )
        tk.Button(
            cadastro,
            text="Cadastrar",
            font=("Arial",10,"bold"),
            fg="#FFFFFF",
            bg=azul,
            width=20,
            command=lambda:verificador_cadastro()
        ).grid(
            row=7,
            column=0,
            columnspan=2,
            pady=(15,5)
        )
        
        def verificador_cadastro():
            nome_digitado=nome.get().strip().upper()
            rm_digitado=rm.get().strip()
            turma_digitado=turma.get().strip().upper()
            if nome_digitado=="" or rm_digitado=="" or turma_digitado=="":
                messagebox.showwarning(
                    "Cadastro Inválido",
                    "Preencha todos os campos corretamente",
                    parent=cadastro
                )
                return
            if not rm_digitado.isdigit():
                messagebox.showwarning(
                    "RM inválido",
                    "O RM deve conter apenas números",
                    parent=cadastro
                )
                return
            if turma_digitado not in ("DS","ADM"):
                messagebox.showwarning(
                    "Turma inválida",
                    "Insira apenas [DS] ou [ADM]",
                    parent=cadastro
                )
                return
            cadastrou=banco.cadastrar_aluno(
                nome_digitado,
                int(rm_digitado),
                turma_digitado
            )
            if cadastrou:
                cadastro.destroy()
                messagebox.showinfo("Sucesso","Aluno cadastrado com sucesso")
            else:
                messagebox.showwarning(
                    "RM já cadastrado",
                    "Esse RM já está cadastrado.",
                    parent=cadastro
                )


def listar_alunos():
    if logado == False:
        faca_login()
        return
    else:
        alunos = banco.listar_alunos()

        janela = tk.Toplevel()
        janela.title("Alunos cadastrados")
        janela.geometry("700x500")
        janela.resizable(False, False)
        janela.configure(bg=azul)
        janela.transient(dashboard)
        janela.focus_set()

        header_listar = tk.Frame(
            janela,
            height=100,
            bg="#066FCA"
        )
        header_listar.pack(
            fill="x"
        )
        tk.Label(
            header_listar,
            text="Lista de alunos",
            font=("Arial", 20, "bold"),
            bg="#066FCA",
            fg="#FFFFFF"
        ).pack(
            pady=25
        )
        area = tk.Frame(
            janela,
            bg=azul
        )
        area.pack(
            fill="both",
            expand=True
        )
        canvas = tk.Canvas(
            area,
            bg=azul,
            highlightthickness=0
        )
        barra = tk.Scrollbar(
            area,
            orient="vertical",
            command=canvas.yview
        )
        frame_alunos = tk.Frame(
            canvas,
            bg=azul
        )
        frame_alunos.bind(
            "<Configure>",
            lambda evento: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window(
            (0,0),
            window=frame_alunos,
            anchor="nw",
            width=680
        )
        canvas.configure(
            yscrollcommand=barra.set
        )
        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )
        barra.pack(
            side="right",
            fill="y"
        )

        if len(alunos) == 0:
            messagebox.showwarning("Erro","Nenhum aluno cadastrado")
            

        for aluno in alunos:
            nome = aluno[1]
            rm = aluno[2]
            turma = aluno[3]
            
            frame_aluno = tk.Frame(
                frame_alunos,
                bg="#FFFFFF",
                height=50
            )
            frame_aluno.pack(
                fill="x",
                padx=10,
                pady=5
            )
            tk.Label(
                frame_aluno,
                text=f"{nome} | RM: {rm} | Turma: {turma}",
                font=("Arial", 12),
                bg="#FFFFFF",
                fg="#000000"
            ).pack(
                pady=5
            )
    
def pesquisar_aluno():
    if logado==False:
        faca_login()
        return
    pesquisa = tk.Toplevel()
    pesquisa.title("Pesquisa de aluno")
    pesquisa.geometry("700x500")
    pesquisa.resizable(False, False)
    pesquisa.configure(bg="#014683")

    pesquisa.grid_columnconfigure(0, weight=1)
    pesquisa.grid_columnconfigure(1, weight=1)
    pesquisa.transient(dashboard)
    pesquisa.focus_set()
    header_pesquisa = tk.Frame(
        pesquisa,
        height=100,
        bg="#066FCA"
    )
    header_pesquisa.grid_propagate(False)
    header_pesquisa.grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="ew"
    )
    titulo_frame_pesquisa = tk.Label(
        header_pesquisa,
        text="Pesquisa de aluno",
        font=("Arial",20,"bold"),
        bg="#066FCA",
        fg="#FFFFFF"
    )
    titulo_frame_pesquisa.grid(
        row=0,
        column=1,
        columnspan=2,
        padx=(15,15)
    )
    tk.Label(
        pesquisa,
        text="Aluno",
        font=("Arial",15,"bold"),
        width=20,
        bg="#066FCA",
        fg="#FFFFFF"
    ).grid(
        row=2,
        column=0,
        columnspan=2     
    )
    nome=tk.Entry(
        pesquisa,
        width=20
    )
    nome.grid(
        row=3,
        column=0,
        columnspan=2,
        pady=(5,5)
    )
    tk.Label(
        pesquisa,
        text="Rm",
        font=("Arial",15,"bold"),
        width=20,
        bg="#066FCA",
        fg="#FFFFFF").grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(5,5)
        )
    rm=tk.Entry(
        pesquisa,
        width=20
    )
    rm.grid(
        row=5,
        column=0,
        columnspan=2,
        pady=(5,5)
    )
    tk.Button(
        pesquisa,
        text="Pesquisar",
        font=("Arial",15,"bold"),
        command=lambda:pesquisa_aluno(),
        width=15,
        bg="#066FCA",
        fg="#FFFFFF"
    ).grid(
        row=6,
        column=0,
        columnspan=2,
        pady=(15,5)
        )
    def pesquisa_aluno():
        nome_pesquisado=nome.get()
        rm_pesquisado=rm.get()
        resultado=banco.pesquisar_alunos(nome_pesquisado,rm_pesquisado)
        if resultado=="Aluno não encontrado":
            messagebox.showerror("Erro","Aluno não encontrado",parent=pesquisa)
        else:
            messagebox.showinfo(
                "Aluno encontrado",
                f"Nome:{resultado[1]}\nRm:{resultado[2]}",
                parent=pesquisa
            )

def ler_notas(entradas):
    valores=[]
    for entrada in entradas:
        texto=entrada.get().strip().replace(",",".")
        if texto=="":
            raise ValueError("Preencha as 4 notas")
        try:
            valor=float(texto)
        except ValueError:
            raise ValueError("Digite apenas números nas notas")
        if not (0<=valor<=10):
            raise ValueError("As notas devem estar entre 0 e 10")
        valores.append(valor)
    return valores

def calcular_media():
    if logado==False:
        faca_login()
    else:
        alunos=banco.listar_alunos()
        notas_salvas=banco.listar_notas()
        calculo_media = tk.Toplevel()
        calculo_media.title("Alunos cadastrados")
        calculo_media.geometry("700x500")
        calculo_media.resizable(False, False)
        calculo_media.configure(bg=azul)
        calculo_media.transient(dashboard)
        calculo_media.focus_set()

        pendentes={}

        def salvar_tudo():
            if not pendentes:
                messagebox.showwarning(
                    "Nada a salvar",
                    "Confirme as notas de pelo menos um aluno.",
                    parent=calculo_media
                )
                return
            try:
                banco.guardar_notas_lote(pendentes)
            except Exception as erro:
                messagebox.showerror(
                    "Erro",
                    f"Não foi possível salvar: {erro}",
                    parent=calculo_media
                )
                return
            messagebox.showinfo(
                "Sucesso",
                f"Notas de {len(pendentes)} aluno(s) salvas com sucesso",
                parent=calculo_media
            )
            calculo_media.destroy()

        tk.Button(
            calculo_media,
            text="Salvar tudo",
            font=("Arial",12,"bold"),
            fg="#FFFFFF",
            bg="#066FCA",
            width=20,
            command=lambda:salvar_tudo()
        ).pack(
            side="bottom",
            pady=10
        )

        area_canva = tk.Frame(
            calculo_media,
            bg=azul
        )
        area_canva.pack(
            fill="both",
            expand=True
        )
        canvas = tk.Canvas(
            area_canva,
            bg=azul
        )
        barra = tk.Scrollbar(
            area_canva,
            orient="vertical",
            command=canvas.yview
        )
        frame_alunos = tk.Frame(
            canvas,
            bg=azul
        )
        frame_alunos.bind(
            "<Configure>",
            lambda evento: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window(
            (0,0),
            window=frame_alunos,
            anchor="nw",
            width=680
        )
        canvas.configure(
            yscrollcommand=barra.set
        )
        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )
        barra.pack(
            side="right",
            fill="y"
        )
        for aluno in alunos:
            aluno_id = aluno[0]
            nome = aluno[1]
            rm = aluno[2]

            frame_media = tk.Frame(
                frame_alunos,
                bg="#066FCA",
                height=70
            )
            frame_media.pack(
                fill="x",
                padx=15,
                pady=5
            )

            frame_media.grid_columnconfigure(0, weight=3)
            frame_media.grid_columnconfigure(1, weight=1)
            frame_media.grid_columnconfigure(2, weight=1)
            frame_media.grid_columnconfigure(3, weight=1)
            frame_media.grid_columnconfigure(4, weight=1)
            frame_media.grid_columnconfigure(5, weight=1)
            frame_media.grid_columnconfigure(6, weight=1)

            tk.Label(
                frame_media,
                text=f"{nome} | RM: {rm}",
                font=("Arial", 12, "bold"),
                bg="#066FCA",
                fg="white",
                anchor="w"
            ).grid(
                row=0,
                column=0,
                padx=10,
                pady=10,
                sticky="ew"
            )

            nota1 = tk.Entry(frame_media, width=8)
            nota1.grid(row=0, column=1, padx=5)
            nota2 = tk.Entry(frame_media, width=8)
            nota2.grid(row=0, column=2, padx=5)
            nota3 = tk.Entry(frame_media, width=8)
            nota3.grid(row=0, column=3, padx=5)
            nota4 = tk.Entry(frame_media, width=8)
            nota4.grid(row=0, column=4, padx=5)
            label_media = tk.Label(
                frame_media,
                width=8,
                text="-",
                bg="#FFFFFF",
                fg="#000000",
                relief="solid",
                bd=1
            )
            label_media.grid(
                row=0,
                column=5,
                padx=5
            )

            entradas=[nota1,nota2,nota3,nota4]

            if aluno_id in notas_salvas:
                salvas=notas_salvas[aluno_id]
                for entrada,valor in zip(entradas,salvas[:4]):
                    entrada.insert(0,f"{valor:g}")
                label_media.configure(
                    text=f"{salvas[4]:.2f}"
                )

            botao_confirmar = tk.Button(
                frame_media,
                width=10,
                text="Confirmar"
            )
            botao_confirmar.grid(
                row=0,
                column=6,
                padx=5
            )

            def atualizar_media(
                evento=None,
                aluno_id=aluno_id,
                entradas=entradas,
                label_media=label_media,
                botao_confirmar=botao_confirmar
            ):
                try:
                    notas=ler_notas(entradas)
                    media=sum(notas)/4
                    label_media.configure(
                        text=f"{media:.2f}"
                    )
                except ValueError:
                    notas=None
                    label_media.configure(
                        text="-"
                    )
                if pendentes.get(aluno_id)!=notas:
                    pendentes.pop(aluno_id,None)
                    botao_confirmar.configure(
                        text="Confirmar"
                    )

            def confirmar(
                aluno_id=aluno_id,
                entradas=entradas,
                botao_confirmar=botao_confirmar
            ):
                try:
                    notas=ler_notas(entradas)
                except ValueError as erro:
                    messagebox.showerror(
                        "Erro",
                        str(erro),
                        parent=calculo_media
                    )
                    return
                pendentes[aluno_id]=notas
                botao_confirmar.configure(
                    text="Confirmado"
                )

            botao_confirmar.configure(
                command=confirmar
            )
            for entrada in entradas:
                entrada.bind(
                    "<KeyRelease>",
                    atualizar_media
                )
         

def sair():
    dashboard.destroy()

dashboard=tk.Tk() 
dashboard.title("Sistema de alunos")
dashboard.geometry("1200x700")
dashboard.resizable(True,True)
dashboard.configure(bg="#F4F4F4")
dashboard.grid_columnconfigure(0, weight=0)
dashboard.grid_columnconfigure(1, weight=1)
dashboard.grid_rowconfigure(0, weight=0)
dashboard.grid_rowconfigure(1, weight=1)
frame_titulo=tk.Frame(
   dashboard,
    bg="#336bc4",
    height=100
)
frame_titulo.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="ew",
)
frame_titulo.pack_propagate(False)
tk.Label(
    frame_titulo,
    text="Sistema de Alunos",
    font=("Arial",25,"bold"),
    bg="#336bc4",
    fg="#FFFFFF"
).pack(
    side="left",
    padx=20
)
login_botao=tk.Button(
    frame_titulo,
    text="Login",
    font=("Arial",15,"bold"),
    bg="#336bc4",
    fg="#FFFFFF",
    command=lambda:janela_login()
)
login_botao.pack(
    side="right",
    padx=20
)
sidebar = tk.Frame(
    dashboard,
    width=220,
    bg="#014683",
    )
sidebar.grid(
    row=1,
    column=0,
    sticky="ns"
)
sidebar.pack_propagate(False)
tk.Label(
    sidebar,
    text="MENU",
    font=("Arial", 20, "bold"),
    fg="#FFFFFF",
    bg="#014683"
).pack(
    side="top",
    pady=(15,20),
    padx=(5,5)
)
tk.Button(
    sidebar,
    text="Cadastrar alunos",
    font=("Arial",15,"bold"),
    bg="#336bc4",
    fg="#FFFFFF",
    width=20,
    command=lambda:cadastrar_alunos()
).pack(
    pady=(15,20),
    padx=(5,5)
)
tk.Button(
    sidebar,
    text="Listar alunos",
    font=("Arial",15,"bold"),
    bg="#336bc4",
    fg="#FFFFFF",
    width=20,
    command=lambda:listar_alunos()
).pack(
    pady=(15,20),
    padx=(5,5)
)
tk.Button(
    sidebar,
    text="Pesquisar aluno",
    font=("Arial",15,"bold"),
    bg="#336bc4",
    fg="#FFFFFF",
    width=20,
    command=lambda:pesquisar_aluno()
).pack(
    pady=(15,20),
    padx=(5,5)
)
tk.Button(
    sidebar,
    text="Calcular média",
    font=("Arial",15,"bold"),
    bg="#336bc4",
    fg="#FFFFFF",
    width=20,
    command=lambda:calcular_media()
).pack(
    pady=(15,20),
    padx=(5,5)
)
tk.Button(
    sidebar,
    text="Sair",
    font=("Arial",15,"bold"),
    bg="#336bc4",
    fg="#FFFFFF",
    width=20,
    command=lambda:sair()
).pack(
    pady=(15,20),
    padx=(5,5)
)


dashboard.mainloop()