import tkinter as tk
from tkinter import messagebox
logado=False

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
    login.transient()
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
    def fazer_login():
        global logado
        messagebox.showinfo("Login","Login realizado com sucesso") 
        login_botao.configure(
            text=usuario.get()
        )
        login.destroy
    enviar=tk.Button(
        login,
        text="Login",
        bg="#0E5EA4",
        fg="white",
        width=15,
        command=fazer_login
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
        cadastro.geometry("500x300")
        cadastro.resizable(False, False)
        cadastro.configure(bg="#014683")

        cadastro.grid_columnconfigure(0, weight=1)
        cadastro.grid_columnconfigure(1, weight=1)
        cadastro.transient()
        cadastro.focus_set()
        nome=tk.Entry
        pass

def listar_alunos():
    if logado==False:
        faca_login()
    pass

def pesquisar_aluno():
    if logado==False:
        faca_login()
    pass

def calcular_media():
    if logado==False:
        faca_login()
    pass

def sair():
    dashboard.destroy

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