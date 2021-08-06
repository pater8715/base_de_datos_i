from tkinter import *
from tkinter import messagebox
from app_conection_bbdd import *

class GUI(Frame):
    def __init__(self, master, db_name):
        super().__init__(master)
        self.__master = master
        self.app_config(self.master,300,300,"Aplication GRUD")
        self.connect = Connection(db_name)
        self.create_menu_items()
        self.create_form()
        self.create_button()


    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    def app_config(self, m,w,h,t): # menu, width , height, title
        self.master.title(t)
        self.menu_bar=Menu(m)
        self.master.config(menu=self.menu_bar, width=w, height=h)


    def create_menu_items(self):
        # Creamos los items de la opcion Archivo del menú
        self.file_items = Menu(self.menu_bar, tearoff=0)
        self.file_items.add_command(label='Conectar', command=lambda: self.connect.connect())
        self.file_items.add_command(label='Crear DB', command=lambda: self.connect.create_db())
        self.file_items.add_command(label='Salir', command= self.exit_app)
        #-------------------------------------------------------------
        self.crud_items = Menu(self.menu_bar, tearoff=0)
        self.crud_items.add_command(label='Crear')#Create
        self.crud_items.add_command(label='Leer')#Read
        self.crud_items.add_command(label='Actualizar')#Update
        self.crud_items.add_command(label='Eliminar')#Delete
        #-------------------------------------------------------------
        self.edit_items = Menu(self.menu_bar, tearoff=0)
        self.edit_items.add_command(label="Limpiar campos")

        # se crean las opciones del menú y se añaden los items en cascada
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_items)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_items)
        self.menu_bar.add_cascade(label="CRUD", menu=self.crud_items)

    def create_form(self):
        self.my_form=Frame(self.master)
        self.my_form.pack()
        # creamos las entradas de texto o textimput
        self.text_imput_id=Entry(self.my_form)
        self.text_imput_id.grid(row=0, column=1, padx=10, pady=10)
        #-------------------------Nombre------------------
        self.text_imput_name = Entry(self.my_form)
        self.text_imput_name.grid(row=1, column=1, padx=10, pady=10)
        self.text_imput_name.config(fg="red", justify="right") #configuramos el color y la justificacion del texto
        # Creamos los label para indicar la imformacion a almacenar en  cada textimput
        self.label_name = Label(self.my_form, text="Identificación")
        self.label_name.grid(row=0, column=0,padx=10, pady=10)
        #-------------------------Nombre------------------
        self.label_name = Label(self.my_form, text="Nombre")
        self.label_name.grid(row=1, column=0, padx=10, pady=10)

    def create_button(self):
        self.my_buttons=Frame(self.master)
        self.my_buttons.pack()
        self.button_create=Button(self.my_buttons, text="Crear")
        self.button_create.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        #--------------------------------------------------------------
        self.button_read = Button(self.my_buttons, text="Leer")
        self.button_read.grid(row=1, column=1, sticky="e", padx=5, pady=5)
        #--------------------------------------------------------------
        self.button_update = Button(self.my_buttons, text="Actualizar")
        self.button_update.grid(row=1, column=2, sticky="e", padx=5, pady=5)
        # --------------------------------------------------------------
        self.button_delete = Button(self.my_buttons, text="Eliminar")
        self.button_delete.grid(row=1, column=3, sticky="e", padx=5, pady=5)

    def exit_app(self):
        exit = messagebox.askquestion("Salir", "Desea salir de la aplicación")
        if exit=="yes":
            self.master.destroy()

if __name__ == '__main__':
    app = Tk() # variable que contiene la interface principal
    myapp = GUI(app,"pruebas") # llamado de la clase
    myapp.mainloop() # iniciamos la aplicacion
