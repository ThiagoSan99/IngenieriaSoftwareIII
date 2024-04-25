import datetime
import pywhatkit
from dialogocontra_ui import *
from dialogonombre_ui import *
from interfaz import *
from PySide6 import QtCore
from PySide6.QtCore import*
from PySide6.QtWidgets import*
from PySide6.QtGui import*
from functools import partial
import sys
import os
import time
import pickle
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
basedir = os.path.dirname(__file__)
from acceso import Conexion

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.page_inicio_sesion()
        self.page_home()
        self.page_inicio_admin()
        self.fila_rece = 0
        self.base_datos = Conexion()
        self.cursor = self.base_datos.conexion.cursor()
        self.cursor.execute("SELECT * FROM Table_Recursos")
        self.myresult = self.cursor.fetchall()
        self.user_admin = 'Admin'
        self.contra_admin = "123admin"
        self.lista_recursos = list()
        self.lista_recetas = list()
        self.lista_proveedores = list()
        self.num = len(self.myresult)
        self.ui.lbl_numero_recurso.setText(str(self.num))
        self.colum_recur = 0
        self.fila_recur = 0
        self.fila_prove = 0
        self.colum_prove = 0
        self.cursor.execute("SELECT * FROM Table_Proovedores")
        self.myresult = self.cursor.fetchall()
        self.index_pro = len(self.myresult)
        self.cursor.execute("SELECT * FROM Table_Recetas")
        self.myresult = self.cursor.fetchall()
        self.index_rec = len(self.myresult)
        self.ruta = ""
        self.ruta1 = ""
        self.actualizar_grid()
        self.actualizar_grid_rece()
        self.actualizar_grid_prove()
        self.llenar_combo()
        self.llenar_combo_prov()
        self.llenar_combo_rec()
        self.presionado = False
        self.usu = ''
        self.id_usu = ''
        self.rece = ''
        self.id_rece = ''
        self.afecc = ''
        self.nom_rec = ''
        self.nom_ciu = ''
        self.correo_usu = ''
        self.contenido = ''
        self.num_usu = ''
        #IMAGENES------------------------------------------------------------------------------------------
        self.setWindowIcon(QIcon(os.path.join(basedir,"image","logo1.png")))
        self.ui.lbl_user.setPixmap(QPixmap(os.path.join(basedir,"image","usuario.png")))
        self.ui.lbl_user_regis.setPixmap(QPixmap(os.path.join(basedir,"image","usuario.png")))
        self.ui.lbl_user_recu.setPixmap(QPixmap(os.path.join(basedir,"image","usuario.png")))
        self.ui.lbl_img6.setScaledContents(True)



        #--------------------------------------------------------------------------------------------------
        
        #BOTONTES------------------------------------------------------------------------------------------
        self.ui.btn_registrarse.clicked.connect(self.page_registro)
        self.ui.btn_recuperar.clicked.connect(self.page_recuperar)
        self.ui.btn_cerrar_sesion.clicked.connect(self.page_inicio_sesion)
        self.ui.btn_cerrar_sesion_admin.clicked.connect(self.page_inicio_sesion)
        self.ui.btn_regresar_recu_inicio.clicked.connect(self.page_inicio_sesion)
        self.ui.btn_regresar_regis_inicio.clicked.connect(self.page_inicio_sesion)
        
        self.ui.btn_home.clicked.connect(self.page_home)
        self.ui.btn_recursos.clicked.connect(self.page_recursos)
        self.ui.btn_recetas.clicked.connect(self.page_recetas)
        self.ui.btn_provedores.clicked.connect(self.page_proveedores)
        self.ui.btn_nosotros.clicked.connect(self.page_nosotros)
        self.ui.btn_regresar_recurso.clicked.connect(self.page_recursos)
        self.ui.btn_regresar_receta.clicked.connect(self.page_recetas)
        self.ui.btn_iniciar_sesion.clicked.connect(self.inicio_sesion)
        self.ui.btn_registrar.clicked.connect(self.registro_cliente)
        self.ui.btn_historial.clicked.connect(self.page_historial)
        self.ui.btn_Menu.clicked.connect(lambda: self.mover_menu(self.ui.frame_lateral))
        self.ui.ln_user_inicio.returnPressed.connect(self.inicio_sesion)
        self.ui.ln_password_inicio.returnPressed.connect(self.inicio_sesion)

        self.ui.btn_nombre_mod.clicked.connect(self.actualizar_nombre)
        self.ui.btn_correo_mod.clicked.connect(self.actualizar_Correo)
        self.ui.btn_password_mod.clicked.connect(self.actualizar_contra)
        self.ui.btn_telefono_mod.clicked.connect(self.actualizar_telefono)
        
        self.ui.btn_Menu_admin.clicked.connect(lambda: self.mover_menu(self.ui.frame_lateral_admin))
        self.ui.btn_recursos_admin.clicked.connect(self.page_recursos_admin)
        self.ui.btn_recetas_admin.clicked.connect(self.page_recetas_admin)
        self.ui.btn_provedores_admin.clicked.connect(self.page_prove_admin)
        self.ui.btn_inicio_admin.clicked.connect(self.page_inicio_admin)
        self.ui.btn_ingresar_recu.clicked.connect(self.page_recursos_admin)
        self.ui.btn_ingresar_rece.clicked.connect(self.page_recetas_admin)
        self.ui.btn_ingresar_prove.clicked.connect(self.page_prove_admin)
        self.ui.btn_modificar_recu.clicked.connect(self.page_modificiar_recu)
        self.ui.btn_modificar_rece.clicked.connect(self.page_modificiar_rece)
        self.ui.btn_modificar_prove.clicked.connect(self.page_modificiar_prove)
        self.ui.btn_regresar_recu_home.clicked.connect(self.page_inicio_admin)
        self.ui.btn_regresar_rece_home.clicked.connect(self.page_inicio_admin)
        self.ui.btn_regresar_prove_home.clicked.connect(self.page_inicio_admin)
        self.ui.btn_regresar_recu_home.clicked.connect(self.page_inicio_admin)
        self.ui.btn_regresar_modrecu_home.clicked.connect(self.page_inicio_admin)
        self.ui.btn_regresar_modrece_home.clicked.connect(self.page_inicio_admin)
        self.ui.btn_regresar_modprove_home.clicked.connect(self.page_inicio_admin)
        self.ui.btn_select_img_recurso.clicked.connect(lambda: self.seleccionar_img(self.ui.lbl_img_recurso_admin))
        self.ui.btn_guardar_recurso.clicked.connect(self.guardar_recurso)
        self.ui.btn_select_img_receta.clicked.connect(lambda: self.seleccionar_img(self.ui.lbl_img_receta_admin))
        self.ui.btn_guardar_recetas.clicked.connect(self.guardar_receta)
        self.ui.btn_guardar_prove.clicked.connect(self.guardar_prove)
        self.ui.btn_modificar_recurso.setEnabled(False)
        self.ui.btn_eliminar_recur.setEnabled(False)
        self.ui.btn_select_img_recurso_mod.setEnabled(False)
        self.ui.btn_buscar_recu_mod.clicked.connect(self.mostrar_recurso)
        self.ui.btn_modificar_recurso.clicked.connect(self.modificar_recurso)
        self.ui.btn_eliminar_recur.clicked.connect(self.eliminar_recu)
        self.ui.btn_select_img_recurso_mod.clicked.connect(lambda: self.seleccionar_img(self.ui.lbl_img_recurso_admin_mod))
        self.ui.btn_select_img_receta_mod.clicked.connect(lambda: self.seleccionar_img(self.ui.lbl_img_receta_admin_mod))
        self.ui.btn_select_img_receta_mod.setEnabled(False)
        self.ui.btn_eliminar_rece.setEnabled(False)
        self.ui.btn_modificar_recetas.setEnabled(False)
        self.ui.btn_buscar_rece_mod.clicked.connect(self.mostrar_receta)
        self.ui.btn_actualizacion.clicked.connect(self.page_actualizar_info)
        self.ui.btn_modificar_recetas.clicked.connect(self.modificar_receta)
        self.ui.btn_eliminar_rece.clicked.connect(self.eliminar_receta)
        self.ui.btn_modificar_provedores.clicked.connect(self.modificar_prov)
        self.ui.btn_buscar_prove_mod.clicked.connect(self.mostrar_prov)
        self.ui.btn_eliminar_prove.clicked.connect(self.eliminar_prov)
        self.ui.btn_verificar_contra.clicked.connect(self.recuperar_contra)
        self.ui.pushButton_19.clicked.connect(self.calificar_rece)
        self.ui.pushButton_20.clicked.connect(self.calificar_rece)
        self.ui.pushButton_21.clicked.connect(self.calificar_rece)
        self.ui.pushButton_22.clicked.connect(self.calificar_rece)
        self.ui.pushButton_23.clicked.connect(self.calificar_rece)
        self.ui.btn_buscar.clicked.connect(self.guardar_historial)
        self.ui.btn_regresar_buscar_home.clicked.connect(self.page_home)
        self.ui.cbox_filtro_receta.currentTextChanged.connect(self.filtrar_rece)
        self.ui.cbox_filtro_prove.currentTextChanged.connect(self.filtrar_prove)
        self.ui.btn_historial.clicked.connect(self.mostrar_historial)
        self.ui.pushButton_26.clicked.connect(self.envia_wssp)
        self.ui.pushButton_27.clicked.connect(self.enviar_correo)
        #---------------------------------------------------------------------------------------------------
        
        #QLINEEDIT------------------------------------------------------------------------------------------
        self.ui.ln_password_inicio.setEchoMode(QLineEdit.Password)
        self.ui.ln_pass_new.setEchoMode(QLineEdit.Password)
        self.ui.ln_pass_confirm.setEchoMode(QLineEdit.Password)
        self.ui.ln_Password.setEchoMode(QLineEdit.Password)
        self.ui.ln_Confirm.setEchoMode(QLineEdit.Password)
        
        self.ui.ln_Nombre.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]*")))
        self.ui.ln_cod.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z0-9]*")))
        self.ui.ln_tel.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        self.ui.ln_correo.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")))
        self.ui.ln_Username.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z0-9]*")))
        self.ui.ln_Password.setValidator(QRegularExpressionValidator(QRegularExpression("[^\s]*")))
        self.ui.ln_Confirm.setValidator(QRegularExpressionValidator(QRegularExpression("[^\s]*")))
        self.ui.ln_correo_recu.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")))
        self.ui.ln_user_recu.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z0-9]*")))
        self.ui.ln_pass_new.setValidator(QRegularExpressionValidator(QRegularExpression("[^\s]*")))
        self.ui.ln_pass_confirm.setValidator(QRegularExpressionValidator(QRegularExpression("[^\s]*")))
        ##RECURSOS
        self.ui.ln_idrecurso_admin.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        self.ui.ln_nombrecomun_admin.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]*")))
        self.ui.ln_nombrecient_admin.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]*")))
        self.ui.ln_idrecurso_admin_mod.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        self.ui.ln_nombrecomun_admin_mod.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]*")))
        self.ui.ln_nombrecient_admin_mod.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]*")))
        ##RECETAS
        self.ui.ln_nombre_receta.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]*")))
        self.ui.ln_id_receta.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        self.ui.ln_nombre_receta_mod.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]*")))
        self.ui.ln_id_receta_mod.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        ##PROVEDORES
        self.ui.ln_nombre_prove.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]*")))
        self.ui.ln_id_prove.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        self.ui.ln_direc_prove.setValidator(QRegularExpressionValidator(QRegularExpression(".*")))
        self.ui.ln_tele_prove.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        self.ui.ln_correo_prove.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")))
        self.ui.ln_nombre_prove_mod.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]*")))
        self.ui.ln_id_prove_mod.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        self.ui.ln_direc_prove_mod.setValidator(QRegularExpressionValidator(QRegularExpression(".*")))
        self.ui.ln_tele_prove_mod.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        self.ui.ln_correo_prove_mod.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")))
        #---------------------------------------------------------------------------------------------------
        
    #FUNCIONES----------------------------------------------------------------------------------------------
    def page_user(self):
        self.ui.paginas_usuarios.setCurrentIndex(0)
        
    def page_registro(self):
        self.ui.paginas_usuarios.setCurrentIndex(1)
    
    def page_recuperar(self):
        self.ui.paginas_usuarios.setCurrentIndex(2)
        
    def page_inicio_sesion(self):
        self.ui.paginas_usuarios.setCurrentIndex(3)
        
    def page_admin(self):
        self.ui.paginas_usuarios.setCurrentIndex(4)
        
    def page_home(self):
        self.ui.paginas_menu.setCurrentIndex(0)
    
    def page_recursos(self):
        self.ui.paginas_menu.setCurrentIndex(1) 
    
    def page_info_recursos(self):
        self.ui.paginas_menu.setCurrentIndex(2)
        
    def page_recetas(self):
        self.ui.paginas_menu.setCurrentIndex(3)
        
    def page_info_recetas(self):
        self.ui.paginas_menu.setCurrentIndex(4)    
        
    def page_proveedores(self):
        self.ui.paginas_menu.setCurrentIndex(5) 
        
    def page_nosotros(self):
        self.ui.paginas_menu.setCurrentIndex(6)
        
    def page_buscar(self):
        self.ui.paginas_menu.setCurrentIndex(7)
    
    def page_actualizar_info(self):
        self.ui.paginas_menu.setCurrentIndex(8)
        
    def page_historial(self):
        self.ui.paginas_menu.setCurrentIndex(9)

    def page_inicio_admin(self):
        self.ui.paginas_menu_admin.setCurrentIndex(0)
        #Recursos
        self.ui.lbl_num_recu_mod.clear()
        self.ui.ln_idrecurso_admin_mod.clear()
        self.ui.ln_nombrecomun_admin_mod.clear()
        self.ui.ln_nombrecient_admin_mod.clear()
        self.ui.text_descripcion_recurso_mod.clear()
        self.ui.text_usos_recurso_mod.clear()
        self.ui.text_contradic_recurso_mod.clear()
        self.ui.lbl_img_recurso_admin_mod.clear()
        
    def page_recursos_admin(self):
        self.ui.paginas_menu_admin.setCurrentIndex(1)
        
    def page_recetas_admin(self):
        self.ui.paginas_menu_admin.setCurrentIndex(2)
        
    def page_prove_admin(self):
        self.ui.paginas_menu_admin.setCurrentIndex(3)
        
    def page_modificiar_recu(self):
        self.ui.paginas_menu_admin.setCurrentIndex(4)
        
    def page_modificiar_rece(self):
        self.ui.paginas_menu_admin.setCurrentIndex(5)
        
    def page_modificiar_prove(self):
        self.ui.paginas_menu_admin.setCurrentIndex(6)

    def inicio_sesion(self):
        self.mostrar_info_home()
        b1 = self.verificar_qline(self.ui.ln_user_inicio)
        b2 = self.verificar_qline(self.ui.ln_password_inicio)
        if b1 == True and b2 == True:
            usuario = self.ui.ln_user_inicio.text()
            contraseña = self.ui.ln_password_inicio.text()
            if self.user_admin == self.ui.ln_user_inicio.text() and self.contra_admin == self.ui.ln_password_inicio.text():
                choice = self.MensajeBox('Éxito','La sesion ha iniciado correctamente')
                self.page_admin()
                self.page_inicio_admin()
                self.ui.ln_user_inicio.clear()
                self.ui.ln_password_inicio.clear()
            else:
                veri = self.base_datos.busca_usuario(usuario)
                if veri is not None :
                    veri1 = self.base_datos.busca_contraseña(contraseña)
                    if veri1 is not None:
                        choice = self.MensajeBox('Éxito','La sesion ha iniciado correctamente')
                        bd = '''SELECT * FROM Usuarios Where UserName = ?'''
                        sql = self.base_datos.conexion.cursor()
                        self.usu = usuario
                        sql.execute(bd, (usuario,))
                        myresult = sql.fetchone()
                        self.id_usu = myresult[1]
                        self.correo_usu = myresult[5]
                        self.num_usu = myresult[4]
                        self.ui.ln_user_inicio.clear()
                        self.ui.ln_password_inicio.clear()
                        self.ui.lbl_id_mod.setText(usuario)
                        self.page_user()
                        self.page_home()
                        self.ui.cbox_filtro_receta.setCurrentIndex(0)
                        self.ui.cbox_filtro_prove.setCurrentIndex(0)

                    else:
                        choice = self.MensajeBox('Éxito','Error, contraseña no coincide',QMessageBox.Warning)
                        self.ui.ln_password_inicio.clear()
                else:
                    choice = self.MensajeBox('Éxito','Error, Usuario no coincide',QMessageBox.Warning)
        else:
            choice = self.MensajeBox('Éxito','Error, hace falta un campo',QMessageBox.Warning)
        
    def registro_cliente(self):
        self.base_datos = Conexion()
        codigo = self.ui.ln_cod.text()
        nombre = self.ui.ln_Nombre.text()
        celular = self.ui.ln_tel.text()
        correo = self.ui.ln_correo.text()
        usuario = self.ui.ln_Username.text()
        contraseña = self.ui.ln_Password.text()
        contra = self.ui.ln_Confirm.text()
        if codigo != '' and nombre != '' and celular != '' and correo != '' and usuario != '' and contraseña != '' and contra != '':
            if self.validar_correo(self.ui.ln_correo):
                if contraseña == contra:
                    veri = self.base_datos.busca_codigo(codigo)
                    if veri is None and veri != codigo:
                        veri = self.base_datos.busca_usuario(usuario)
                        if veri is None and veri != usuario:
                            self.base_datos.ingresarUsuario(nombre, codigo, usuario, contraseña, celular, correo)
                            self.ui.ln_cod.clear()
                            self.ui.ln_Nombre.clear()
                            self.ui.ln_tel.clear()
                            self.ui.ln_correo.clear()
                            self.ui.ln_Username.clear()
                            self.ui.ln_Password.clear()
                            self.ui.ln_Confirm.clear()
                            self.base_datos.conexion.close()
                            choice = self.MensajeBox('Éxito','Los datos han sido guardados exitosamente')
                        else:
                            choice = self.MensajeBox('Error', "Error, el usuario ya está registrado, digite uno distinto",QMessageBox.Warning)
                            self.ui.ln_Username.clear()
                            self.base_datos.conexion.close()
                                
                    else:
                        choice = self.MensajeBox('Error', "Error, el codigo ya está registrado, digite uno distinto", QMessageBox.Warning)
                        self.ui.ln_cod.clear()
                        
                        self.base_datos.conexion.close()
                                            
                else:
                    choice = self.MensajeBox('Error', "Error, La contraseña no coincide", QMessageBox.Warning) 
                    self.base_datos.conexion.close()
                    self.ui.ln_Password.clear()
                    self.ui.ln_Confirm.clear()
            else:
               choice = self.MensajeBox('Error', "Error, Correo no válido", QMessageBox.Warning) 
               self.ui.ln_correo.clear()
        else:
            choice = self.MensajeBox('Error', "Error, hace falta un campo", QMessageBox.Warning)
            self.base_datos.conexion.close()  

    def actualizar_nombre(self,id):
        dialogo = DialogoDatos()
        dialogo.line_actualizacion.setPlaceholderText('Digite el nombre')
        dialogo.line_actualizacion.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z ]*")))
        
        resp = dialogo.exec()
        t = dialogo.line_actualizacion.text()
        c = self.ui.lbl_id_mod.text()
        if resp == QDialog.Accepted:
            if t != '':
                self.base_datos.actualizar_nombre(t,c)
                choice = QMessageBox.information(self, 'Éxito', "El nombre datos han sido actualizados")
            else:
                choice = QMessageBox('Error', "Error, el campo esta vacio", QMessageBox.Warning)

    def actualizar_Correo(self):
        dialogo = DialogoDatos()
        dialogo.line_actualizacion.setPlaceholderText('Digite el Correo')
        dialogo.line_actualizacion.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")))
        resp = dialogo.exec()
        t = dialogo.line_actualizacion.text()
        c = self.ui.lbl_id_mod.text()
        if resp == QDialog.Accepted:
            if t != '':
                self.base_datos.actualizar_correo(t,c)
                choice = QMessageBox.information(self, 'Éxito', "El correo han sido actualizados")
            else:
                choice = QMessageBox('Error', "Error, el campo esta vacio", QMessageBox.Warning)
    
    def actualizar_telefono(self):
        dialogo = DialogoDatos()
        dialogo.line_actualizacion.setPlaceholderText('Digite el telefono')
        dialogo.line_actualizacion.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        resp = dialogo.exec()
        t = dialogo.line_actualizacion.text()
        c = self.ui.lbl_id_mod.text()
        if resp == QDialog.Accepted:
            if t != '':
                self.base_datos.actualizar_telefono(t,c)
                choice= QMessageBox.information(self, 'Éxito', "El telefono han sido actualizados")
            else:
                choice = QMessageBox('Error', "Error, el campo esta vacio", QMessageBox.Warning)

    def actualizar_contra(self):
        dialogo = DialogoContraseña()
        dialogo.line_contra_act.setValidator(QRegularExpressionValidator(QRegularExpression("[^\s]*")))
        dialogo.line_contra_nueva.setValidator(QRegularExpressionValidator(QRegularExpression("[^\s]*")))
        dialogo.line_contra_veri.setValidator(QRegularExpressionValidator(QRegularExpression("[^\s]*")))
        dialogo.line_contra_act.setEchoMode(QLineEdit.Password)
        dialogo.line_contra_nueva.setEchoMode(QLineEdit.Password)
        dialogo.line_contra_veri.setEchoMode(QLineEdit.Password)
        resp = dialogo.exec()
        if resp == QDialog.Accepted:
            if dialogo.line_contra_act.text() != '' and dialogo.line_contra_nueva.text() != '' and dialogo.line_contra_veri.text()!= '':
                c = self.ui.lbl_id_mod.text()
                t = dialogo.line_contra_act.text()
                veri = self.base_datos.busca_usuario(c)

                if veri is not None :

                    veri1 = self.base_datos.busca_contraseña(t)

                    if veri1 is not None:

                        if dialogo.line_contra_nueva.text() == dialogo.line_contra_veri.text():
                            t = dialogo.line_contra_nueva.text()
                            self.base_datos.actualizar_contraseña(t,c)

                            choice= QMessageBox.information(self, 'Éxito', "La contraseña ha sido actualizada")
                    
                        else:

                            choice = QMessageBox.question(self, 'Error', "Las contraseñas no coinciden, ¿Desea continuar?", QMessageBox.Yes | QMessageBox.No)
                            dialogo.line_contra_nueva.clear()
                            dialogo.line_contra_veri.clear()
                            if choice == QMessageBox.Yes:
                                self.actualizar_contra()

                    else:

                        choice = QMessageBox.question(self, 'Error', "La contraseña no coincide con el ususario, ¿Desea continuar?", QMessageBox.Yes | QMessageBox.No)
                        dialogo.line_contra_act.clear()
                        if choice == QMessageBox.Yes:
                            self.actualizar_contra()
                        
            else:
                choice = QMessageBox.question(self, 'Error', "Hace falta un campo, ¿Desea continuar?", QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                            self.actualizar_contra()
            
    def verificar_qline(self,qline):
        b = False
        text=qline.text()
        if text:
            b = True
        else:
            b = False
        return b
    
    def MensajeBox(self,title,mesage,icon=QMessageBox.Information,buttons=QMessageBox.Ok):
        MensajeBox = QMessageBox()
        MensajeBox.setWindowTitle(title)
        MensajeBox.setWindowIcon(QIcon(os.path.join(basedir,'image','logo1.png')))
        MensajeBox.setText(mesage)
        MensajeBox.setIcon(icon)
        MensajeBox.setStandardButtons(buttons)
        choice = MensajeBox.exec()
        return choice  
    
    def mover_menu(self,frame):
        if True:
            width = frame.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animation = QPropertyAnimation(frame, b'minimumWidth')
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(extender)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            
    def guardar_recurso(self):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recursos")
        myresult = cursor.fetchall()
        numero_recurso = self.num
        id_recurso = self.ui.ln_idrecurso_admin.text()
        nombre_comun = self.ui.ln_nombrecomun_admin.text()
        nombre_cientifico = self.ui.ln_nombrecient_admin.text()
        descrip_recurso = self.ui.text_descripcion_recurso.toPlainText()
        usos_recurso = self.ui.text_usos_recurso.toPlainText()
        contra_recurso = self.ui.text_contradic_recurso.toPlainText()
        img = self.ui.lbl_img_recurso_admin.pixmap()
        if self.tiene_img(self.ui.lbl_img_recurso_admin) and  id_recurso!=""  and  nombre_comun != "" and nombre_cientifico != "" and descrip_recurso != "" and usos_recurso != "" and contra_recurso != "":
            if self.base_datos.busca_recurso(id_recurso) is not None:
                choice = self.MensajeBox('Error', "Id ya registrado", QMessageBox.Warning)
                self.ui.ln_idrecurso_admin.clear()
            else:
                
                self.base_datos.ingresarRecurso(numero_recurso, id_recurso, nombre_comun, nombre_cientifico, descrip_recurso, usos_recurso, contra_recurso, self.ruta)
                self.agregar_recursos(self.num)
                choice = self.MensajeBox('Éxito','Los datos han sido guardados exitosamente')
                self.ui.ln_idrecurso_admin.clear()
                self.ui.ln_nombrecomun_admin.clear()
                self.ui.ln_nombrecient_admin.clear()
                self.ui.text_descripcion_recurso.clear()
                self.ui.text_usos_recurso.clear()
                self.ui.text_contradic_recurso.clear()
                self.ui.lbl_img_recurso_admin.clear()
                self.num +=1
                self.ui.lbl_numero_recurso.setText(str(self.num))
                
        else:
            choice = self.MensajeBox('Error', "Error, hace falta un campo", QMessageBox.Warning)
            
    def guardar_receta(self):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recetas")
        myresult = cursor.fetchall()
        nombre = self.ui.ln_nombre_receta.text()
        id_rece = self.ui.ln_id_receta.text()
        afec = self.ui.cbox_agr_rece.currentText()
        img = self.ui.lbl_img_receta_admin.pixmap()
        ingredientes = self.ui.text_ingredi_recetas.toPlainText()
        preparacion = self.ui.text_prepa_recetas.toPlainText()
        contra = self.ui.text_contra_recetas.toPlainText()
        calificacion = 0
        if self.tiene_img(self.ui.lbl_img_receta_admin) and nombre != "" and ingredientes != "" and preparacion != "" and contra != "" and afec != "":
           if self.base_datos.busca_receta(id_rece) is not None:
                choice = self.MensajeBox('Error', "Id ya registrado", QMessageBox.Warning)
                self.ui.ln_id_receta.clear()
           else:
                self.base_datos.ingresarReceta(nombre, id_rece, afec, ingredientes, preparacion, contra, calificacion ,self.ruta )
                self.agregar_receta(self.index_rec)
                choice = self.MensajeBox('Éxito','Los datos han sido guardados exitosamente')
                self.ui.ln_nombre_receta.clear()
                self.ui.ln_id_receta.clear()
                self.ui.cbox_agr_rece.setCurrentIndex(0)
                self.ui.lbl_img_receta_admin.clear()
                self.ui.text_ingredi_recetas.clear()
                self.ui.text_prepa_recetas.clear()
                self.ui.text_contra_recetas.clear()
                self.index_rec +=1
                self.actualizar_grid_rece()
                self.ui.cbox_mod_rec.clear()
                self.llenar_combo_rec()
        else:
            choice = self.MensajeBox('Error', "Error, hace falta un campo", QMessageBox.Warning)
            
    def guardar_prove(self):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recetas")
        myresult = cursor.fetchall()
        nombre = self.ui.ln_nombre_prove.text()
        id_prove = self.ui.ln_id_prove.text()
        info = self.ui.text_info_prove.toPlainText()
        direccion = self.ui.ln_direc_prove.text()
        tele = self.ui.ln_tele_prove.text()
        correo = self.ui.ln_correo_prove.text()
        if nombre != "" and id_prove != "" and info != "" and direccion != "" and tele != "" and correo != "":

            if self.validar_correo(self.ui.ln_correo_prove):

                if self.base_datos.busca_prov(id_prove) is not None:
                    choice = self.MensajeBox('Error', "Proveedor ya se ecncuentra registrado", QMessageBox.Warning)
                    self.ui.ln_id_prove.clear()
                else:
                    
                    self.base_datos.ingresarProveedor(nombre,info, direccion, tele, correo, id_prove)
                    self.agregar_prove(self.index_pro)
                    choice = self.MensajeBox('Éxito','Los datos han sido guardados exitosamente')
                    self.ui.ln_nombre_prove.clear()
                    self.ui.ln_id_prove.clear()
                    self.ui.text_info_prove.clear()
                    self.ui.ln_direc_prove.clear()
                    self.ui.ln_tele_prove.clear()
                    self.ui.ln_correo_prove.clear()
                    self.index_pro += 1
                    self.ui.comboBox.setCurrentIndex(0)
                    self.ui.comboBox.clear()
                    self.llenar_combo_prov()
                    self.actualizar_grid_prove()
            else:
                choice = self.MensajeBox('Error', "Error, Correo no válido", QMessageBox.Warning) 
                self.ui.ln_correo.clear()
        else:
            choice = self.MensajeBox('Error', "Error, hace falta un campo", QMessageBox.Warning)
            
    def validar_correo(self, line):
        if line.validator().validate(line.text(), 0)[0] == QValidator.Acceptable:
            return  True
        else:
            return False

    def modificar_prov(self):
        nombre = self.ui.ln_nombre_prove_mod.text()
        id_prove = self.ui.ln_id_prove_mod.text()
        info = self.ui.text_info_prove_mod.toPlainText()
        direccion = self.ui.ln_direc_prove_mod.text()
        tele = self.ui.ln_tele_prove_mod.text()
        correo = self.ui.ln_correo_prove_mod.text()
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute(f"SELECT * FROM Table_Proovedores Where Id_Provedor = {id_prove}")
        myresult = cursor.fetchall()
        if nombre != '' and id_prove != '' and info != '' and direccion != '' and tele !='' and correo !='':
            choice = self.MensajeBox('Aviso', "¿Desea Modificar?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
            if choice== QMessageBox.Yes:
                sql = '''UPDATE Table_Proovedores set Nombre=?, Info=?, Direccion=?, Telefono=?, Correo=? WHERE Id_Provedor = ?'''
                cursor.execute(sql, (nombre,info,direccion,tele,correo, id_prove))
                choice = self.MensajeBox('Éxito','Los datos han sido Modificados exitosamente')
                self.ui.ln_nombre_prove_mod.clear()
                self.ui.ln_id_prove_mod.clear()
                self.ui.text_info_prove_mod.clear()
                self.ui.ln_direc_prove_mod.clear()
                self.ui.ln_tele_prove_mod.clear()
                self.ui.ln_correo_prove_mod.clear()
                self.ui.comboBox.setCurrentIndex(0)
                bd.conexion.commit()
                self.ui.comboBox.clear()
                self.actualizar_grid_prove()
                self.llenar_combo_prov()
                
                    
        else:
            choice = self.MensajeBox('Error', "Error, hace falta un campo", QMessageBox.Warning)

    def eliminar_prov(self):
        id_prove = self.ui.ln_id_prove_mod.text()
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute(f"SELECT * FROM Table_Proovedores Where Id_Provedor = {id_prove}")
        myresult = cursor.fetchall()
        choice = self.MensajeBox('Aviso', "¿Desea Eliminar?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            sql = '''DELETE FROM Table_Proovedores WHERE Id_Provedor = ?'''
            cursor.execute(sql, (id_prove,))
            choice = self.MensajeBox('Éxito','Recurso eliminado exitosamente')
            self.ui.ln_nombre_prove_mod.clear()
            self.ui.ln_id_prove_mod.clear()
            self.ui.text_info_prove_mod.clear()
            self.ui.ln_direc_prove_mod.clear()
            self.ui.ln_tele_prove_mod.clear()
            self.ui.ln_correo_prove_mod.clear()
            self.ui.comboBox.setCurrentIndex(0)
            bd.conexion.commit()
            self.ui.comboBox.clear()
            self.llenar_combo_prov()
            self.actualizar_grid_prove()
            
    def mostrar_recurso(self):
        self.presionado = False
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recursos")
        myresult = cursor.fetchall()
        index = self.ui.cbox_recurso.currentIndex()-1
        if index != -1:
            self.ui.btn_modificar_recurso.setEnabled(True)
            self.ui.btn_eliminar_recur.setEnabled(True)
            self.ui.btn_select_img_recurso_mod.setEnabled(True)  
            self.ui.lbl_img_recurso_admin_mod.setPixmap(QPixmap(myresult[index][7]))
            self.ui.lbl_num_recu_mod.setText(myresult[index][0])
            self.ui.ln_idrecurso_admin_mod.setText(str(myresult[index][1]))
            self.ui.ln_nombrecomun_admin_mod.setText(myresult[index][2])
            self.ui.ln_nombrecient_admin_mod.setText(myresult[index][3])
            self.ui.text_descripcion_recurso_mod.setText(myresult[index][4])
            self.ui.text_usos_recurso_mod.setText(myresult[index][5])
            self.ui.text_contradic_recurso_mod.setText(myresult[index][6])
            self.ui.cbox_recurso.setCurrentIndex(0)
        else:
            choice = self.MensajeBox('Error', "Error, Elija un recurso", QMessageBox.Warning)
    
    def mostrar_receta(self):
        self.presionado = False
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recetas")
        myresult = cursor.fetchall()
        index = self.ui.cbox_mod_rec.currentIndex()-1
        if index != -1:
            self.ui.btn_modificar_recetas.setEnabled(True)
            self.ui.btn_eliminar_rece.setEnabled(True)
            self.ui.btn_select_img_receta_mod.setEnabled(True)  
            self.ui.lbl_img_receta_admin_mod.setPixmap(QPixmap(myresult[index][7]))
            self.ui.ln_nombre_receta_mod.setText(myresult[index][0])
            self.ui.ln_id_receta_mod.setText(myresult[index][1])
            self.ui.text_afec_receta_mod.setText(myresult[index][2])
            self.ui.text_ingredi_recetas_mod.setText(myresult[index][3])
            self.ui.text_prepa_recetas_mod.setText(myresult[index][4])
            self.ui.text_contra_recetas_mod.setText(myresult[index][5])

        else:
            choice = self.MensajeBox('Error', "Error, Elija una receta", QMessageBox.Warning)

    def mostrar_prov(self):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Proovedores")
        myresult = cursor.fetchall()
        index = self.ui.comboBox.currentIndex()-1
        if index != -1:
            self.ui.btn_modificar_provedores.setEnabled(True)
            self.ui.btn_eliminar_prove.setEnabled(True)
            self.ui.ln_nombre_prove_mod.setText(myresult[index][0])
            self.ui.ln_id_prove_mod.setText(myresult[index][5])
            self.ui.text_info_prove_mod.setText(myresult[index][1])
            self.ui.ln_direc_prove_mod.setText(myresult[index][2])
            self.ui.ln_tele_prove_mod.setText(myresult[index][3])
            self.ui.ln_correo_prove_mod.setText(myresult[index][4])
        else:
            choice = self.MensajeBox('Error', "Error, Elija un recurso", QMessageBox.Warning)
 
    def modificar_recurso(self):
        num = self.ui.lbl_num_recu_mod.text()
        id_recu = self.ui.ln_idrecurso_admin_mod.text()
        nombre_co =  self.ui.ln_nombrecomun_admin_mod.text()
        nombre_cien = self.ui.ln_nombrecient_admin_mod.text()
        descrip = self.ui.text_descripcion_recurso_mod.toPlainText()
        uso = self.ui.text_usos_recurso_mod.toPlainText()
        contra = self.ui.text_contradic_recurso_mod.toPlainText()
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute(f"SELECT * FROM Table_Recursos Where Id_Recurso = {id_recu}")
        myresult = cursor.fetchall()
        self.ruta = myresult[0][7]
        if self.tiene_img(self.ui.lbl_img_recurso_admin_mod) and  id_recu!=""  and  nombre_co != "" and nombre_cien != "" and descrip != "" and uso != "" and contra != "":
            choice = self.MensajeBox('Aviso', "¿Desea Modificar?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.Yes:
                choice1 = self.MensajeBox('Aviso', "¿Desea Modificar la imagen?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
                if choice1== QMessageBox.Yes:
                    self.ui.btn_select_img_recurso_mod.clicked.connect(self.presionadooo)
                    sql = '''UPDATE Table_Recursos set Dir_Imagen = ?,Num_Recurso = ?, Nombre_Comun = ?,
                    Nombre_Cientifico = ?, Descripcion = ?, Usos = ?, Contradicciones = ? WHERE Id_Recurso = ?'''
                    cursor.execute(sql, (self.ruta1, num, nombre_co,nombre_cien,descrip,uso,contra, id_recu))
                    choice = self.MensajeBox('Éxito','Los datos han sido Modificados exitosamente')
                else:
                    sql = '''UPDATE Table_Recursos set Num_Recurso = ?, Nombre_Comun = ?,
                    Nombre_Cientifico = ?, Descripcion = ?, Usos = ?, Contradicciones = ? WHERE Id_Recurso = ?'''
                    cursor.execute(sql, (num, nombre_co,nombre_cien,descrip,uso,contra, id_recu))
                    choice = self.MensajeBox('Éxito','Los datos han sido Modificados exitosamente')
                self.presionado = False
                self.ui.lbl_img_recurso_admin_mod.clear()
                self.ui.lbl_num_recu_mod.clear()
                self.ui.ln_idrecurso_admin_mod.clear()
                self.ui.ln_nombrecomun_admin_mod.clear()
                self.ui.ln_nombrecient_admin_mod.clear()
                self.ui.text_descripcion_recurso_mod.clear()
                self.ui.text_usos_recurso_mod.clear()
                self.ui.text_contradic_recurso_mod.clear()
                self.ui.btn_modificar_recurso.setEnabled(False)
                self.ui.btn_eliminar_recur.setEnabled(False)
                self.ui.btn_select_img_recurso_mod.setEnabled(False)
                bd.conexion.commit()
                self.ui.cbox_recurso.clear()
                self.llenar_combo()
                self.actualizar_grid()
        else:
            choice = self.MensajeBox('Error', "Error, hace falta un campo", QMessageBox.Warning)
    
    def presionadooo(self):
        self.presionado=True

    def eliminar_recu(self):
        
        id_recu = self.ui.ln_idrecurso_admin_mod.text()
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute(f"SELECT * FROM Table_Recursos Where Id_Recurso = {id_recu}")
        
        myresult = cursor.fetchall()
        choice = self.MensajeBox('Aviso', "¿Desea Eliminar?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            sql = '''DELETE FROM Table_Recursos WHERE Id_Recurso = ?'''
            cursor.execute(sql, (id_recu,))
            choice = self.MensajeBox('Éxito','Recurso eliminado exitosamente')
            
            self.ui.lbl_img_recurso_admin_mod.clear()
            self.ui.lbl_num_recu_mod.clear()
            self.ui.ln_idrecurso_admin_mod.clear()
            self.ui.ln_nombrecomun_admin_mod.clear()
            self.ui.ln_nombrecient_admin_mod.clear()
            self.ui.text_descripcion_recurso_mod.clear()
            self.ui.text_usos_recurso_mod.clear()
            self.ui.text_contradic_recurso_mod.clear()
            self.ui.btn_modificar_recurso.setEnabled(False)
            self.ui.btn_eliminar_recur.setEnabled(False)
            self.ui.btn_select_img_recurso_mod.setEnabled(False)
            self.fila_recur = self.ui.grid_agregar_recur.rowCount()
            self.colum_recur = self.ui.grid_agregar_recur.columnCount()
            bd.conexion.commit()
            self.actualizar_grid()
            self.ui.cbox_recurso.clear()
            self.llenar_combo()

    def modificar_receta(self):
        nombre = self.ui.ln_nombre_receta_mod.text()
        id_re = self.ui.ln_id_receta_mod.text()
        img = self.ui.lbl_img_receta_admin_mod.pixmap()
        afec = self.ui.text_afec_receta_mod.toPlainText()
        ingre = self.ui.text_ingredi_recetas_mod.toPlainText()
        prepa = self.ui.text_prepa_recetas_mod.toPlainText()
        contra = self.ui.text_contra_recetas_mod.toPlainText()
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute(f"SELECT * FROM Table_Recetas Where Id_Receta = {id_re}")
        myresult = cursor.fetchall()
        self.ruta = myresult[0][7]
        cal = myresult[0][6]
        if self.tiene_img(self.ui.lbl_img_receta_admin_mod) and nombre != "" and id_re != "" and afec != "" and ingre != "" and prepa != "" and contra != "":
            choice = self.MensajeBox('Aviso', "¿Desea Modificar?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.Yes:
                choice1 = self.MensajeBox('Aviso', "¿Desea Modificar la imagen?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
                if choice1== QMessageBox.Yes:
                    sql = '''UPDATE Table_Recetas set Dir_img = ?,Nombre = ?, Afecciones = ?,
                    Ingredientes = ?, Preparacion = ?, Contradicciones = ? WHERE Id_Receta = ?'''
                    cursor.execute(sql, (self.ruta1, nombre, afec, ingre, prepa ,contra, id_re))
                    choice = self.MensajeBox('Éxito','Los datos han sido Modificados exitosamente')
                else:
                    sql = '''UPDATE Table_Recetas set Dir_img = ?, Nombre = ?, Afecciones = ?,
                    Ingredientes = ?, Preparacion = ?, Contradicciones = ? WHERE Id_Receta = ?'''
                    cursor.execute(sql, (self.ruta,nombre, afec, ingre, prepa ,contra, id_re))
                    choice = self.MensajeBox('Éxito','Los datos han sido Modificados exitosamente')


                self.ui.ln_nombre_receta_mod.clear()
                self.ui.ln_id_receta_mod.clear()
                self.ui.lbl_img_receta_admin_mod.clear()
                self.ui.text_afec_receta_mod.clear()
                self.ui.text_ingredi_recetas_mod.clear()
                self.ui.text_prepa_recetas_mod.clear()
                self.ui.text_contra_recetas_mod.clear()
                self.ui.btn_select_img_receta_mod.setEnabled(False)
                self.ui.btn_eliminar_rece.setEnabled(False)
                self.ui.btn_modificar_recetas.setEnabled(False)
                self.ui.cbox_mod_rec.setCurrentIndex(0)
                bd.conexion.commit()
                self.actualizar_grid_rece()
                self.ui.cbox_mod_rec.clear()
                self.llenar_combo_rec()
        else:
            choice = self.MensajeBox('Error', "Error, hace falta un campo", QMessageBox.Warning)
            
    def eliminar_receta(self):
        id_rece = self.ui.ln_id_receta_mod.text()
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute(f"SELECT * FROM Table_Recetas Where Id_Receta = {id_rece}")
        myresult = cursor.fetchall()
        choice = self.MensajeBox('Aviso', "¿Desea Eliminar?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            sql = '''DELETE FROM Table_Recetas WHERE Id_Receta = ?'''
            cursor.execute(sql, (id_rece,))
            choice = self.MensajeBox('Éxito','Recurso eliminado exitosamente')
            self.ui.ln_nombre_receta_mod.clear()
            self.ui.ln_id_receta_mod.clear()
            self.ui.lbl_img_receta_admin_mod.clear()
            self.ui.text_afec_receta_mod.clear()
            self.ui.text_ingredi_recetas_mod.clear()
            self.ui.text_prepa_recetas_mod.clear()
            self.ui.text_contra_recetas_mod.clear()
            self.ui.btn_select_img_receta_mod.setEnabled(False)
            self.ui.btn_eliminar_rece.setEnabled(False)
            self.ui.btn_modificar_recetas.setEnabled(False)
            self.ui.cbox_mod_rec.setCurrentIndex(0)
            bd.conexion.commit()
            self.actualizar_grid_rece()
            self.ui.cbox_mod_rec.clear()
            self.llenar_combo_rec()
    
    def seleccionar_img(self,lbl):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Seleccionar Imagen', '', 
        'Imagenes (*.png *.jpg *.jpeg *.bmp *.gif)')
        if file_name:
            img = QPixmap(file_name)
            lbl.setPixmap(img)
            self.ruta = file_name
            self.ruta1 = file_name
        else:
            return None
        
    def tiene_img(self,lbl):
        if lbl.pixmap().isNull():
            return False
        else:
            return True
              
    def agregar_recursos(self,i):  
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recursos")
        myresult = cursor.fetchall()
        for index in range(len(myresult)):
            if self.esta_ocupado(self.fila_recur,self.colum_recur) == False and i == index:
                frame_pri = QFrame(self.ui.scrollAreaWidgetContents_2)
                frame_pri.setMinimumSize(QSize(350, 220))
                frame_pri.setMaximumSize(QSize(350, 220))
                frame_pri.setFrameShape(QFrame.StyledPanel)
                frame_pri.setFrameShadow(QFrame.Raised)
                vbox = QVBoxLayout(frame_pri)
                vbox.setSpacing(0)
                vbox.setContentsMargins(0, 0, 0, 0)
                frame_img = QFrame(frame_pri)
                frame_img.setFrameShape(QFrame.StyledPanel)
                frame_img.setFrameShadow(QFrame.Raised)
                hbox = QHBoxLayout(frame_img)
                space1 = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                hbox.addItem(space1)
                lbl_img = QLabel(frame_img)
                lbl_img.setScaledContents(True)
                lbl_img.clear()
                lbl_img.setMinimumSize(QSize(120, 120))
                lbl_img.setMaximumSize(QSize(120, 120))
                hbox.addWidget(lbl_img)
                space2 = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                hbox.addItem(space2)
                vbox.addWidget(frame_img)
                frame_info = QFrame(frame_pri)
                frame_info.setFrameShape(QFrame.StyledPanel)
                frame_info.setFrameShadow(QFrame.Raised)
                hbox1 = QHBoxLayout(frame_info)
                lbl_info = QLabel(frame_info)
                lbl_info.clear()
                lbl_info.setMinimumSize(QSize(120, 58))
                lbl_info.setMaximumSize(QSize(120, 58))
                hbox1.addWidget(lbl_info)
                btn_info = QPushButton(frame_info)
                btn_info.setObjectName(f'btn_info_{self.fila_recur}_{self.colum_recur}_{i}')
                btn_info.setMinimumSize(QSize(100, 42))
                btn_info.setMaximumSize(QSize(100, 42))
                btn_info.setText('IR')
                btn_info.clicked.connect(self.posicion_boton)
                hbox1.addWidget(btn_info)
                vbox.addWidget(frame_info)
                lbl_img.setPixmap(QPixmap(myresult[index][7]))
                lbl_info.setText(myresult[index][2])
                self.ui.grid_agregar_recur.addWidget(frame_pri,self.fila_recur,self.colum_recur)
                self.colum_recur += 1
            elif self.colum_recur == 2:
                self.colum_recur = 0
                self.fila_recur += 1
        self.actualizar_grid()
        self.ui.cbox_recurso.addItem(str(myresult[index][2]))
        
    def agregar_receta(self,i):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recetas")
        myresult = cursor.fetchall()
        for index in range(len(myresult)):
            if index == i:
                btn_ir_receta = QPushButton(self.ui.scrollAreaWidgetContents_3)
                btn_ir_receta.setObjectName(f'btn_ir_receta_{index}')
                btn_ir_receta.setText(str(myresult[index][0]))
                btn_ir_receta.clicked.connect(self.posicion_btn_recet)
                self.ui.verticalLayout_23.addWidget(btn_ir_receta)
                self.ui.grid_recetas.addWidget(btn_ir_receta,self.fila_rece,0)
                self.fila_rece += 1
        self.actualizar_grid_rece()
        self.ui.cbox_agr_rece.addItem(myresult[index][0])
    
    def actualizar_grid_rece(self):
        fil = 0
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recetas")
        myresult = cursor.fetchall()
        self.limpiar_grid_rece()
        for index in range(len(myresult)):
            btn_ir_receta = QPushButton(self.ui.scrollAreaWidgetContents_3)
            btn_ir_receta.setObjectName(f'btn_ir_receta_{index}')
            btn_ir_receta.clicked.connect(self.posicion_btn_recet)
            btn_ir_receta.setText(str(myresult[index][0]))
            self.ui.verticalLayout_23.addWidget(btn_ir_receta)
            self.ui.grid_recetas.addWidget(btn_ir_receta,fil,0)
            fil += 1

    def filtrar_rece(self):
            fil = 0   
            if self.ui.cbox_filtro_receta.currentText() == '':
                self.actualizar_grid_rece()
            else:
                var = self.ui.cbox_filtro_receta.currentText()
                self.afecc = var
                bd = Conexion()
                cursor = bd.conexion.cursor()
                sql = '''SELECT * FROM Table_Recetas WHERE Afecciones =?'''
                cursor.execute(sql,(var,))
                myresult = cursor.fetchall()
                self.limpiar_grid_rece()
                for index in range(len(myresult)):
                    btn_ir_receta = QPushButton(self.ui.scrollAreaWidgetContents_3)
                    btn_ir_receta.setObjectName(f'btn_ir_receta_{index}')
                    btn_ir_receta.clicked.connect(self.filtro_btn_recet)
                    btn_ir_receta.setText(str(myresult[index][0]))
                    self.ui.verticalLayout_23.addWidget(btn_ir_receta)
                    self.ui.grid_recetas.addWidget(btn_ir_receta,fil,0)
                    fil += 1
    

    def actualizar_grid(self):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recursos")
        myresult = cursor.fetchall()
        fil = 0
        col = 0
        self.limpiar_grid()
        for index in range(len(myresult)):
                frame_pri = QFrame(self.ui.scrollAreaWidgetContents_2)
                frame_pri.setMinimumSize(QSize(350, 220))
                frame_pri.setMaximumSize(QSize(350, 220))
                frame_pri.setFrameShape(QFrame.StyledPanel)
                frame_pri.setFrameShadow(QFrame.Raised)
                vbox = QVBoxLayout(frame_pri)
                vbox.setSpacing(0)
                vbox.setContentsMargins(0, 0, 0, 0)
                frame_img = QFrame(frame_pri)
                frame_img.setFrameShape(QFrame.StyledPanel)
                frame_img.setFrameShadow(QFrame.Raised)
                hbox = QHBoxLayout(frame_img)
                space1 = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                hbox.addItem(space1)
                lbl_img = QLabel(frame_img)
                lbl_img.setScaledContents(True)
                lbl_img.clear()
                lbl_img.setMinimumSize(QSize(120, 120))
                lbl_img.setMaximumSize(QSize(120, 120))
                hbox.addWidget(lbl_img)
                space2 = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                hbox.addItem(space2)
                vbox.addWidget(frame_img)
                frame_info = QFrame(frame_pri)
                frame_info.setFrameShape(QFrame.StyledPanel)
                frame_info.setFrameShadow(QFrame.Raised)
                hbox1 = QHBoxLayout(frame_info)
                lbl_info = QLabel(frame_info)
                lbl_info.clear()
                lbl_info.setMinimumSize(QSize(120, 58))
                lbl_info.setMaximumSize(QSize(120, 58))
                hbox1.addWidget(lbl_info)
                btn_info = QPushButton(frame_info)
                btn_info.setMinimumSize(QSize(100, 42))
                btn_info.setMaximumSize(QSize(100, 42))
                btn_info.setText('IR')
                btn_info.clicked.connect(self.posicion_boton)
                hbox1.addWidget(btn_info)
                vbox.addWidget(frame_info)
                btn_info.setObjectName(f'btn_info_{self.fila_recur}_{self.colum_recur}_{index}')
                lbl_img.setPixmap(QPixmap(myresult[index][7]))
                lbl_info.setText(myresult[index][2])
                self.ui.grid_agregar_recur.addWidget(frame_pri,fil,col)
                col += 1
                if col == 2:
                    col = 0
                    fil += 1
                               
    def limpiar_grid(self):
        fil = self.ui.grid_agregar_recur.rowCount()
        col = self.ui.grid_agregar_recur.columnCount()
        for fila in range(fil):
            for columna in range(col):
                item = self.ui.grid_agregar_recur.itemAtPosition(fila,columna)
                if item is not None:
                    widget = item.widget()
                    if widget is not None:
                        self.ui.grid_agregar_recur.removeWidget(widget)
                        widget.deleteLater()
        self.ui.grid_agregar_recur.update()
                                  
    def esta_ocupado(self,fila,columna):
        item = self.ui.grid_agregar_recur.itemAtPosition(self.fila_recur, self.colum_recur)
        if item is not None:
            return True
        else:
            return False
        
    def posicion_boton(self):
        boton_presionado = self.sender()
        object_name = boton_presionado.objectName()
        fila, columna, indice = object_name.split('_')[2:]
        indice = int(indice)
        self.mostrar_info_recurso(indice)
        
    def posicion_btn_recet(self):
        boton_presionado = self.sender()
        object_name = boton_presionado.objectName()
        indice = object_name.split('_')[-1]
        indice = int(indice)
        self.mostrar_info_receta(indice)

        
    def mostrar_info_recurso(self,i):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recursos")
        myresult = cursor.fetchall()
        self.page_info_recursos()
        self.ui.lbl_recurso.setText(myresult[i][0])
        self.ui.lbl_id_recurso.setText(myresult[i][1])
        self.ui.lbl_nombre_recur.setText(myresult[i][2])
        self.ui.lbl_cienti_recur.setText(myresult[i][3])
        self.ui.lbl_img_recurso.setPixmap(QPixmap(myresult[i][7]))
        self.ui.lbl_info_produc.setText(myresult[i][4])
        self.ui.lbl_usos_produc.setText(myresult[i][5])
        self.ui.lbl_contra_produc.setText(myresult[i][6])
        
    def mostrar_info_receta(self, i):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recetas")
        myresult = cursor.fetchall()
        self.page_info_recetas()
        self.ui.lbl_receta.setText(myresult[i][0])
        self.ui.lbl_img_receta.setPixmap(QPixmap(myresult[i][7]))
        self.ui.lbl_afecci_recetas.setText(myresult[i][2])
        self.ui.lbl_ingredientes_rece.setText(myresult[i][3])
        self.ui.lbl_prepara_rece.setText(myresult[i][4])
        self.ui.lbl_contra_rece.setText(myresult[i][5])
        self.id_rece = myresult[i][1]
        self.rece = myresult[i][0]
        if self.verificar_calificacion_rece(self.id_usu,self.id_rece) == True :
            self.generar_promedio_calificaciones(self.id_rece)
        else:
            self.generar_promedio_calificaciones(self.id_rece)
    
    def mostrar_info_rece_bus(self,i):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        consulta = "SELECT * FROM Table_Recetas WHERE LOWER(Nombre) LIKE ? or LOWER(Afecciones) LIKE ? or LOWER(Ingredientes) LIKE ? or LOWER(Preparacion) LIKE ? or LOWER(Contradicciones) LIKE ?"
        cursor.execute(consulta, ('%' + self.contenido + '%','%' + self.contenido + '%','%' + self.contenido + '%','%' + self.contenido + '%','%' + self.contenido + '%'))
        myresult = cursor.fetchall()
        self.page_info_recetas()
        self.ui.lbl_receta.setText(myresult[i][0])
        self.ui.lbl_img_receta.setPixmap(QPixmap(myresult[i][7]))
        self.ui.lbl_afecci_recetas.setText(myresult[i][2])
        self.ui.lbl_ingredientes_rece.setText(myresult[i][3])
        self.ui.lbl_prepara_rece.setText(myresult[i][4])
        self.ui.lbl_contra_rece.setText(myresult[i][5])
        self.id_rece = myresult[i][1]
        self.rece = myresult[i][0]
        if self.verificar_calificacion_rece(self.id_usu,self.id_rece) == True :
            self.generar_promedio_calificaciones(self.id_rece)
        else:
            self.generar_promedio_calificaciones(self.id_rece)

    def mostrar_info_recur_bus(self,i):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        consulta = "SELECT * FROM Table_Recursos WHERE LOWER(Nombre_Comun) LIKE ? or LOWER(Nombre_Cientifico) LIKE ? or LOWER(Descripcion) LIKE ? or LOWER(Usos) LIKE ? or LOWER(Contradicciones) LIKE ?"
        cursor.execute(consulta, ('%' + self.contenido + '%','%' + self.contenido + '%','%' + self.contenido + '%','%' + self.contenido + '%','%' + self.contenido + '%'))
        myresult = cursor.fetchall()
        self.page_info_recursos()
        self.ui.lbl_recurso.setText(myresult[i][0])
        self.ui.lbl_id_recurso.setText(myresult[i][1])
        self.ui.lbl_nombre_recur.setText(myresult[i][2])
        self.ui.lbl_cienti_recur.setText(myresult[i][3])
        self.ui.lbl_img_recurso.setPixmap(QPixmap(myresult[i][7]))
        self.ui.lbl_info_produc.setText(myresult[i][4])
        self.ui.lbl_usos_produc.setText(myresult[i][5])
        self.ui.lbl_contra_produc.setText(myresult[i][6])

    def mostrar_filtro_rece(self,i):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        sql = '''SELECT * FROM Table_Recetas WHERE Afecciones = ?'''
        cursor.execute(sql, (self.afecc,))
        myresult = cursor.fetchall()
        self.page_info_recetas()
        self.ui.lbl_receta.setText(myresult[i][0])
        self.ui.lbl_img_receta.setPixmap(QPixmap(myresult[i][7]))
        self.ui.lbl_afecci_recetas.setText(myresult[i][2])
        self.ui.lbl_ingredientes_rece.setText(myresult[i][3])
        self.ui.lbl_prepara_rece.setText(myresult[i][4])
        self.ui.lbl_contra_rece.setText(myresult[i][5])
        self.id_rece = myresult[i][1]
        self.rece = myresult[i][0]
        if self.verificar_calificacion_rece(self.id_usu,self.id_rece) == True :
            self.generar_promedio_calificaciones(self.id_rece)
        else:
            self.ui.lbl_prom_rec.setText(f'Sin calificar')


    def filtro_btn_recet(self):
        boton_presionado = self.sender()
        object_name = boton_presionado.objectName()
        indice = object_name.split('_')[-1]
        indice = int(indice)
        self.mostrar_filtro_rece(indice)

    def calificar_rece(self):
        ola = self.sender().objectName()
        usu = self.usu
        id_usu = self.id_usu
        rece = self.rece
        id_rece = self.id_rece
        if ola == 'pushButton_19':
            cal = 1
            if self.verificar_calificacion_rece(id_usu,id_rece) == False:
                self.base_datos.generar_calificacion_receta(id_usu,usu,id_rece,rece,cal)
                choice = self.MensajeBox('Éxito','Se ha calificado con 1 estrella')
                self.generar_promedio_calificaciones(id_rece)
            else:
                choice = self.MensajeBox('Aviso', "¿El usuario ya calificó está receta, desea actualizar?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    self.actualizar_calificacion_rece(id_usu,id_rece,cal)
        elif ola == 'pushButton_20':
            cal = 2
            if self.verificar_calificacion_rece(id_usu,id_rece) == False:
                self.base_datos.generar_calificacion_receta(id_usu,usu,id_rece,rece,cal)
                choice = self.MensajeBox('Éxito','Se ha calificado con 2 estrellas')
                self.generar_promedio_calificaciones(id_rece)
            else:
                choice = self.MensajeBox('Aviso', "¿El usuario ya calificó está receta, desea actualizar?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    self.actualizar_calificacion_rece(id_usu,id_rece,cal)
        elif ola == 'pushButton_21':
            cal = 3
            if self.verificar_calificacion_rece(id_usu,id_rece) == False:
                self.base_datos.generar_calificacion_receta(id_usu,usu,id_rece,rece,cal)
                choice = self.MensajeBox('Éxito','Se ha calificado con 3 estrellas')
                self.generar_promedio_calificaciones(id_rece)
            else:
                choice = self.MensajeBox('Aviso', "¿El usuario ya calificó está receta, desea actualizar?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    self.actualizar_calificacion_rece(id_usu,id_rece,cal)
        elif ola == 'pushButton_22':
            cal = 4
            if self.verificar_calificacion_rece(id_usu,id_rece) == False:
                self.base_datos.generar_calificacion_receta(id_usu,usu,id_rece,rece,cal)
                choice = self.MensajeBox('Éxito','Se ha calificado con 4 estrellas')
                self.generar_promedio_calificaciones(id_rece)
            else:
                choice = self.MensajeBox('Aviso', "¿El usuario ya calificó está receta, desea actualizar?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    self.actualizar_calificacion_rece(id_usu,id_rece,cal)
        elif ola == 'pushButton_23':
            cal = 5
            if self.verificar_calificacion_rece(id_usu,id_rece) == False:
                self.base_datos.generar_calificacion_receta(id_usu,usu,id_rece,rece,cal)
                choice = self.MensajeBox('Éxito','Se ha calificado con 5 estrellas')
                self.generar_promedio_calificaciones(id_rece)
            else:
                choice = self.MensajeBox('Aviso', "¿El usuario ya calificó está receta, desea actualizar?", QMessageBox.Information, QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    self.actualizar_calificacion_rece(id_usu,id_rece,cal)
        else:
            print('la cagamos')
    
    def verificar_calificacion_rece(self, id_usu, id_rece):
        cursor = self.base_datos.conexion.cursor()
        sql = '''SELECT * FROM Calificacion_Rece WHERE Id_Receta = ? AND Cod_Usuario = ?'''
        cursor.execute(sql,(id_rece,id_usu,))
        resultado = cursor.fetchone()
        if resultado is not None:
            if resultado[2] == id_rece:
                return True
            else:
                return False
        else:

            return False
    
    def actualizar_calificacion_rece(self, id_usu, id_rece,cal):
        cursor = self.base_datos.conexion.cursor()
        sql = '''SELECT * FROM Calificacion_Rece WHERE Id_Receta = ? AND Cod_Usuario = ?'''
        cursor.execute(sql, (id_rece,id_usu,))
        myresult = cursor.fetchone()
        resultado = list(myresult)
        if resultado[4] == cal:
            choice = self.MensajeBox('Aviso','El usuario ya ha dado esta calificación')
        else:
            sql = '''UPDATE Calificacion_Rece SET Calificacion =? WHERE Id_Receta = ? AND Cod_Usuario = ?'''
            cursor.execute(sql,(cal,id_rece,id_usu,))
            self.base_datos.conexion.commit()
            choice = self.MensajeBox('Éxito','Se ha actualizado la calificación')
            self.generar_promedio_calificaciones(id_rece)
    
    def generar_promedio_calificaciones(self, id_rece):
        cursor = self.base_datos.conexion.cursor()
        sql = '''SELECT * FROM Calificacion_Rece WHERE Id_Receta = ? '''
        cursor.execute(sql, (id_rece,))
        myresult = cursor.fetchall()
        prom = 0
        if myresult != []:
            list(myresult)
            i = 0
            j = 0

            for x in range (len(myresult)):
                i = i + myresult[x][4]
                j = j + 1
            if j > 0:
                prom = i/j
                self.ui.lbl_prom_rec.setText(f'Promedio: {prom}')
        else:
            self.ui.lbl_prom_rec.setText(f'Promedio: {prom}')
    
    def llenar_combo(self):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recursos")
        myresult = cursor.fetchall()
        self.ui.cbox_recurso.addItem(str(''))
        self.actualizar_grid()
        for index in range(len(myresult)):
            self.ui.cbox_recurso.addItem(str(myresult[index][2]))
    
    def llenar_combo_rec(self):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Recetas")
        myresult = cursor.fetchall()
        self.ui.cbox_mod_rec.addItem(str(''))
        for index in range(len(myresult)):
            self.ui.cbox_mod_rec.addItem(str(myresult[index][0]))

    def llenar_combo_prov(self):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Proovedores")
        myresult = cursor.fetchall()
        self.ui.comboBox.addItem(str(''))
        self.actualizar_grid()
        for index in range(len(myresult)):
            self.ui.comboBox.addItem(str(myresult[index][0]))

    def limpiar_grid_rece(self):
        fil = self.ui.grid_recetas.rowCount()
        for fila in range(fil):
            item = self.ui.grid_recetas.itemAtPosition(fila,0)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    self.ui.grid_recetas.removeWidget(widget)
                    widget.deleteLater()
        self.ui.grid_recetas.update()
    
    def agregar_prove(self,i):
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Proovedores")
        myresult = cursor.fetchall()
        for index in range(len(myresult)):
            if self.esta_ocupado3() == False and index == i:
                frame_pri = QFrame(self.ui.scrollAreaWidgetContents_4)
                frame_pri.setMinimumSize(QSize(450, 195))
                frame_pri.setMaximumSize(QSize(450, 195))
                frame_pri.setStyleSheet(u"QFrame {\n"
"    border: 2px solid #000000; /* Establece el borde de 2 p\u00edxeles de ancho y color negro. Puedes ajustar el grosor y el color seg\u00fan tus preferencias. */\n"
"}")
                frame_pri.setFrameShape(QFrame.StyledPanel)
                frame_pri.setFrameShadow(QFrame.Raised)
                vbox = QVBoxLayout(frame_pri)
                lbl_prove = QLabel(frame_pri)
                lbl_prove.setMinimumSize(QSize(0, 20))
                lbl_prove.setMaximumSize(QSize(16777215, 20))
                lbl_prove.setText(myresult[i][0])
                vbox.addWidget(lbl_prove)
                lbl_info_pro = QLabel(frame_pri)
                lbl_info_pro.setWordWrap(True)
                lbl_info_pro.setText(myresult[i][1])
                vbox.addWidget(lbl_info_pro)
                frm_prove = QFormLayout()
                lbl_dir = QLabel(frame_pri)
                lbl_dir.setText('Dirección') 
                frm_prove.setWidget(0, QFormLayout.LabelRole, lbl_dir)
                lbl_info_dir = QLabel(frame_pri)
                lbl_info_dir.setText(myresult[i][2]) 
                frm_prove.setWidget(0, QFormLayout.FieldRole, lbl_info_dir)
                lbl_tel = QLabel(frame_pri)
                lbl_tel.setText('Teléfono')
                frm_prove.setWidget(1, QFormLayout.LabelRole, lbl_tel)
                lbl_info_tel = QLabel(frame_pri)
                lbl_info_tel.setText(str(myresult[i][3]))
                frm_prove.setWidget(1, QFormLayout.FieldRole, lbl_info_tel)
                lbl_correo = QLabel(frame_pri)
                lbl_correo.setText('Correo')
                frm_prove.setWidget(2, QFormLayout.LabelRole, lbl_correo)
                lbl_info_corr = QLabel(frame_pri)
                lbl_info_corr.setText(str(myresult[i][4]))
                frm_prove.setWidget(2, QFormLayout.FieldRole, lbl_info_corr)
                vbox.addLayout(frm_prove)
                self.ui.grid_prove.addWidget(frame_pri, self.fila_prove, self.colum_prove)
                self.colum_prove += 1
            elif self.colum_prove == 2:
                self.fila_prove += 1
                self.colum_prove = 0
       
    def esta_ocupado3(self):
        item = self.ui.grid_prove.itemAtPosition(self.fila_prove,self.colum_prove)
        if item is not None:
            return True
        else:
            return False
        
    def limpiar_grid_prove(self):
        fil = self.ui.grid_prove.rowCount()
        col = self.ui.grid_prove.columnCount()
        for fila in range(fil):
            for columna in range(col):
                item = self.ui.grid_prove.itemAtPosition(fila,columna)
                if item is not None:
                    widget = item.widget()
                    if widget is not None:
                        self.ui.grid_prove.removeWidget(widget)
                        widget.deleteLater()
        self.ui.grid_prove.update()

    def filtrar_prove(self):
        self.nom_ciu = self.ui.cbox_filtro_prove.currentText()
        bd = Conexion()
        cursor = bd.conexion.cursor()
        consulta = "SELECT * FROM Table_Proovedores WHERE LOWER(Direccion) LIKE ?"
        cursor.execute(consulta, ('%' + self.nom_ciu.lower() + '%',))
        myresult = cursor.fetchall()
        fil = 0
        col = 0
        self.limpiar_grid_prove()
        for index in range(len(myresult)):
            
            frame_pri = QFrame(self.ui.scrollAreaWidgetContents_4)
            frame_pri.setMinimumSize(QSize(450, 195))
            frame_pri.setMaximumSize(QSize(450, 195))
            frame_pri.setStyleSheet(u"QFrame {\n"
"    border: 2px solid #000000; /* Establece el borde de 2 p\u00edxeles de ancho y color negro. Puedes ajustar el grosor y el color seg\u00fan tus preferencias. */\n"
"}")
            frame_pri.setFrameShape(QFrame.StyledPanel)
            frame_pri.setFrameShadow(QFrame.Raised)
            vbox = QVBoxLayout(frame_pri)
            lbl_prove = QLabel(frame_pri)
            lbl_prove.setMinimumSize(QSize(0, 20))
            lbl_prove.setMaximumSize(QSize(16777215, 20))
            lbl_prove.setText(myresult[index][0])
            vbox.addWidget(lbl_prove)
            lbl_info_pro = QLabel(frame_pri)
            lbl_info_pro.setWordWrap(True)
            lbl_info_pro.setText(myresult[index][1])
            vbox.addWidget(lbl_info_pro)
            frm_prove = QFormLayout()
            lbl_dir = QLabel(frame_pri)
            lbl_dir.setText('Dirección') 
            frm_prove.setWidget(0, QFormLayout.LabelRole, lbl_dir)
            lbl_info_dir = QLabel(frame_pri)
            lbl_info_dir.setText(myresult[index][2]) 
            frm_prove.setWidget(0, QFormLayout.FieldRole, lbl_info_dir)
            lbl_tel = QLabel(frame_pri)
            lbl_tel.setText('Teléfono')
            frm_prove.setWidget(1, QFormLayout.LabelRole, lbl_tel)
            lbl_info_tel = QLabel(frame_pri)
            lbl_info_tel.setText(str(myresult[index][3]))
            frm_prove.setWidget(1, QFormLayout.FieldRole, lbl_info_tel)
            lbl_correo = QLabel(frame_pri)
            lbl_correo.setText('Correo')
            frm_prove.setWidget(2, QFormLayout.LabelRole, lbl_correo)
            lbl_info_corr = QLabel(frame_pri)
            lbl_info_corr.setText(str(myresult[index][4]))
            frm_prove.setWidget(2, QFormLayout.FieldRole, lbl_info_corr)
            vbox.addLayout(frm_prove)
            self.ui.grid_prove.addWidget(frame_pri, fil, col)
            col += 1
            if col == 2:
                fil += 1
                col = 0


    def actualizar_grid_prove(self):
        
        bd = Conexion()
        cursor = bd.conexion.cursor()
        cursor.execute("SELECT * FROM Table_Proovedores")
        myresult = cursor.fetchall()
        fil = 0
        col = 0
        self.limpiar_grid_prove()
        for index in range(len(myresult)):
            
            frame_pri = QFrame(self.ui.scrollAreaWidgetContents_4)
            frame_pri.setMinimumSize(QSize(450, 195))
            frame_pri.setMaximumSize(QSize(450, 195))
            frame_pri.setStyleSheet(u"QFrame {\n"
"    border: 2px solid #000000; /* Establece el borde de 2 p\u00edxeles de ancho y color negro. Puedes ajustar el grosor y el color seg\u00fan tus preferencias. */\n"
"}")
            frame_pri.setFrameShape(QFrame.StyledPanel)
            frame_pri.setFrameShadow(QFrame.Raised)
            vbox = QVBoxLayout(frame_pri)
            lbl_prove = QLabel(frame_pri)
            lbl_prove.setMinimumSize(QSize(0, 20))
            lbl_prove.setMaximumSize(QSize(16777215, 20))
            lbl_prove.setText(myresult[index][0])
            vbox.addWidget(lbl_prove)
            lbl_info_pro = QLabel(frame_pri)
            lbl_info_pro.setWordWrap(True)
            lbl_info_pro.setText(myresult[index][1])
            vbox.addWidget(lbl_info_pro)
            frm_prove = QFormLayout()
            lbl_dir = QLabel(frame_pri)
            lbl_dir.setText('Dirección') 
            frm_prove.setWidget(0, QFormLayout.LabelRole, lbl_dir)
            lbl_info_dir = QLabel(frame_pri)
            lbl_info_dir.setText(myresult[index][2]) 
            frm_prove.setWidget(0, QFormLayout.FieldRole, lbl_info_dir)
            lbl_tel = QLabel(frame_pri)
            lbl_tel.setText('Teléfono')
            frm_prove.setWidget(1, QFormLayout.LabelRole, lbl_tel)
            lbl_info_tel = QLabel(frame_pri)
            lbl_info_tel.setText(str(myresult[index][3]))
            frm_prove.setWidget(1, QFormLayout.FieldRole, lbl_info_tel)
            lbl_correo = QLabel(frame_pri)
            lbl_correo.setText('Correo')
            frm_prove.setWidget(2, QFormLayout.LabelRole, lbl_correo)
            lbl_info_corr = QLabel(frame_pri)
            lbl_info_corr.setText(str(myresult[index][4]))
            frm_prove.setWidget(2, QFormLayout.FieldRole, lbl_info_corr)
            vbox.addLayout(frm_prove)
            self.ui.grid_prove.addWidget(frame_pri, fil, col)
            col += 1
            if col == 2:
                fil += 1
                col = 0

    def recuperar_contra(self):
        self.ui.btn_confirmar_pass.setEnabled(False)
        self.ui.btn_veri_cod.setEnabled(False)
        self.ui.ln_pass_new.setEnabled(False)
        self.ui.ln_pass_confirm.setEnabled(False)
        self.ui.line_veri_cod.setEnabled(False)
        correo_recuperar = self.ui.ln_correo_recu.text()
        usuario_recuperar = self.ui.ln_user_recu.text()
        bd = Conexion()
        cursor = bd.conexion.cursor()

        if bd.busca_usuario(usuario_recuperar) is not None and bd.busca_correo(correo_recuperar) is not None:
            veri = self.enviar_correo(correo_recuperar)
            choice = self.MensajeBox('Éxito','El correo ha sido enviado')
            self.ui.line_veri_cod.setEnabled(True)
            self.ui.btn_veri_cod.setEnabled(True)
            if self.ui.btn_veri_cod.clicked.connect(lambda:self.verificar_codigo(veri)):

                self.ui.ln_pass_new.setEnabled(True)
                self.ui.ln_pass_confirm.setEnabled(True)
                self.ui.btn_confirmar_pass.setEnabled(True)
                self.ui.btn_confirmar_pass.clicked.connect(lambda:self.actualizar_contra(usuario_recuperar))
            else:
                choice = self.MensajeBox('Exito','El codigo no coincide')
        else:
            choice = self.MensajeBox('Alerta','El usuario o el correo no coincide')

    def verificar_codigo(self,cod):
        veri = self.ui.line_veri_cod.text()
        if veri == cod:
            choice = self.MensajeBox('Exito','El codigo coincide')
            return True
        else:
            return False
        
    def actualizar_contra(self,id):
        if self.ui.ln_pass_new.text() != '' and self.ui.ln_pass_confirm.text() != '':
            new = self.ui.ln_pass_new.text()
            new2 = self.ui.ln_pass_confirm.text()
            if new == new2:
                bd = Conexion()
                cursor = bd.conexion.cursor()
                bd.actualizar_contraseña(new,id)
                choice = self.MensajeBox('Éxito','La contraseña se ha actualizado')
                self.ui.ln_pass_new.setEnabled(False)
                self.ui.ln_pass_confirm.setEnabled(False)
                self.ui.btn_confirmar_pass.setEnabled(False)
                self.ui.ln_correo_recu.clear()
                self.ui.ln_user_recu.clear()
                self.ui.line_veri_cod.clear()
                self.ui.ln_pass_new.clear()
                self.ui.ln_pass_confirm.clear()
            else:
                choice = self.MensajeBox('Érror','Error, Las contraseñas no coinciden',QMessageBox.Warning)
        else: 
            choice = self.MensajeBox('Érror','Error, hace falta un campo',QMessageBox.Warning)

    def enviar_correo(self,destinatario):
        codigo = "".join([str(random.randint(0, 9)) for _ in range(5)])
        load_dotenv()  # Cargamos las variables de entorno
        remitente = 'hedmedcol@gmail.com'  # Guardamos el contenido de la variable user
        asunto = 'Recuperar contraseña HedMedCol'
        msg = MIMEMultipart()
        msg['Subject'] = asunto
        msg['From'] = remitente
        msg['To'] = destinatario
        # Cuerpo del mensaje
        cuerpo_mensaje = f"El código de recuperación de contraseña es el siguiente: {codigo}"
        msg.attach(MIMEText(cuerpo_mensaje, 'plain'))
        # Nos conectamos con gmail para enviar el mensaje
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, "bldq lmty rbbe hnxg")
        # Enviamos el correo
        server.sendmail(remitente, destinatario, msg.as_string())
        # Cerramos la conexión
        server.quit()
        return codigo

    def envia_wssp(self):
        nombre = self.usu
        mensaje = f'Hola, ¿cómo estás {nombre}? Envía el mensaje si quieres comunicarte con un asesor de HelMerCol.'
        pywhatkit.sendwhatmsg_instantly('+57'+self.num_usu,mensaje)
        choice = self.MensajeBox('Exito','El mensaje ha sido enviado')
    

    def enviar_correo(self):
        destinatario = self.correo_usu
        remitente = 'hedmedcol@gmail.com'  # Guardamos el contenido de la variable user
        asunto = 'Bienvenido a HedMedCol'
        msg = MIMEMultipart()
        msg['Subject'] = asunto
        msg['From'] = remitente
        msg['To'] = destinatario
        # Cuerpo del mensaje
        cuerpo_mensaje = f"Usted se ha comunicado con HenMedCol, conteste el correo con su inquietud."
        msg.attach(MIMEText(cuerpo_mensaje, 'plain'))
        # Nos conectamos con gmail para enviar el mensaje
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, "bldq lmty rbbe hnxg")
        # Enviamos el correo
        server.sendmail(remitente, destinatario, msg.as_string())
        # Cerramos la conexión
        server.quit()
        choice = self.MensajeBox('Exito','El correo ha sido enviado')

    

    def guardar_historial(self):
        if self.ui.ln_buscar.text() != '':
            fecha_y_hora_actual = datetime.datetime.now()
            fecha_actual = fecha_y_hora_actual.strftime("%Y-%m-%d")  # Formato: Año-Mes-Día
            hora_actual = fecha_y_hora_actual.strftime("%H:%M:%S")
            self.base_datos.ingresarHistorial(self.id_usu,self.ui.ln_buscar.text(),fecha_actual,hora_actual)
            choice = self.MensajeBox('Éxito','La busqueda ha sido realizada')
            self.agregar_info_buscar()
        else:
            choice = self.MensajeBox('Érror','Error, hace falta un campo',QMessageBox.Warning)
    
    def mostrar_historial(self):
        self.page_historial()
        bd = Conexion()
        cursor = bd.conexion.cursor()
        sql = '''Select * FROM Historial_Usu WHERE Cod_Usu = ?'''
        cursor.execute(sql,(self.id_usu,))
        myresult = cursor.fetchall()
        i = len(myresult)
        self.ui.tabl_historial.setRowCount(i)
        tablerow = 0
        for x in range (len(myresult)):
            
            self.ui.tabl_historial.setItem(tablerow,0,QTableWidgetItem(str(myresult[x][1])))
            self.ui.tabl_historial.setItem(tablerow,1,QTableWidgetItem(str(myresult[x][2])))
            self.ui.tabl_historial.setItem(tablerow,2,QTableWidgetItem(str(myresult[x][3])))

            tablerow +=1

    def agregar_info_buscar(self):
        self.page_buscar()
        fila = 0
        self.limpiar_grid_buscar()
        contenido = self.ui.ln_buscar.text()
        self.contenido = self.ui.ln_buscar.text()
        self.ui.ln_buscar.clear()

        bd = Conexion()
        cursor = bd.conexion.cursor()
        consulta = "SELECT * FROM Table_Recursos WHERE LOWER(Nombre_Comun) LIKE ? or LOWER(Nombre_Cientifico) LIKE ? or LOWER(Descripcion) LIKE ? or LOWER(Usos) LIKE ? or LOWER(Contradicciones) LIKE ?"
        cursor.execute(consulta, ('%' + contenido + '%','%' + contenido + '%','%' + contenido + '%','%' + contenido + '%','%' + contenido + '%'))
        table_recu = cursor.fetchall()
        consulta = "SELECT * FROM Table_Recetas WHERE LOWER(Nombre) LIKE ? or LOWER(Afecciones) LIKE ? or LOWER(Ingredientes) LIKE ? or LOWER(Preparacion) LIKE ? or LOWER(Contradicciones) LIKE ?"
        cursor.execute(consulta, ('%' + contenido + '%','%' + contenido + '%','%' + contenido + '%','%' + contenido + '%','%' + contenido + '%'))
        table_rece = cursor.fetchall()

        if table_rece != [] and table_recu != []:
            for i in range(len(table_rece)):
                btn_buscar = QPushButton(self.ui.scrollAreaWidgetContents)
                btn_buscar.setObjectName(f'btn_ir_receta_{i}')
                btn_buscar.setText(table_rece[i][0])
                btn_buscar.clicked.connect(self.posicion_btn_general_rece)
                self.ui.grid_buscar.addWidget(btn_buscar,fila,0)
                fila += 1

            for j in range(len(table_recu)):
                btn_buscar = QPushButton(self.ui.scrollAreaWidgetContents)
                btn_buscar.setObjectName(f'btn_ir_recurs_{j}')
                btn_buscar.setText(table_recu[j][2])
                btn_buscar.clicked.connect(self.posicion_btn_general_recu)
                self.ui.grid_buscar.addWidget(btn_buscar,fila,0)
                fila += 1

        elif table_rece != []:
            for i in range(len(table_rece)):
                btn_buscar = QPushButton(self.ui.scrollAreaWidgetContents)
                btn_buscar.setObjectName(f'btn_ir_receta_{i}')
                btn_buscar.setText(table_rece[i][0])
                btn_buscar.clicked.connect(self.posicion_btn_general_rece)
                self.ui.grid_buscar.addWidget(btn_buscar,fila,0)
                fila += 1

        elif table_recu != []:
            for j in range(len(table_recu)):
                btn_buscar = QPushButton(self.ui.scrollAreaWidgetContents)
                btn_buscar.setObjectName(f'btn_ir_recurs_{j}')
                btn_buscar.setText(table_recu[j][2])
                btn_buscar.clicked.connect(self.posicion_btn_general_recu)
                self.ui.grid_buscar.addWidget(btn_buscar,fila,0)
                fila += 1
        else:
            choice = self.MensajeBox('Érror','Error, no hay resultados con la busqueda',QMessageBox.Warning)
    
    def posicion_btn_general_rece(self):
        
        boton_presionado = self.sender()
        object_name = boton_presionado.objectName()
        indice = object_name.split('_')[-1]
        indice = int(indice)
        print(indice)
        self.mostrar_info_rece_bus(indice)
        
    def posicion_btn_general_recu(self):
            
        boton_presionado = self.sender()
        object_name = boton_presionado.objectName()
        indice = object_name.split('_')[-1]
        indice = int(indice)
        self.mostrar_info_recur_bus(indice)
    
    def limpiar_grid_buscar(self):
        fil = self.ui.grid_buscar.rowCount()
        for fila in range(fil):
            item = self.ui.grid_buscar.itemAtPosition(fila,0)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    self.ui.grid_buscar.removeWidget(widget)
                    widget.deleteLater()
        self.ui.grid_buscar.update()
        
    def mostrar_info_home(self):
        numero = random.randint(1,2)
        bd = Conexion()
        cursor = bd.conexion.cursor()
        consulta = "SELECT * FROM Table_Recursos "
        cursor.execute(consulta)
        table_recu = cursor.fetchall()
        consulta = "SELECT * FROM Table_Recetas " 
        cursor.execute(consulta)
        table_rece = cursor.fetchall()
        magnitud = 1
        if numero == 1:
            tamaño = len(table_rece)
            if tamaño > 6 or tamaño >= 6:
                while magnitud <= 6:
                    indice_random = random.randint(0,tamaño-1)
                    if magnitud == 1:
                        self.ui.lbl_img1.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img1.setScaledContents(True)
                        self.ui.lbl_info1.setText(table_rece[indice_random][0])
                        magnitud += 1
                    elif magnitud == 2:
                        self.ui.lbl_img2.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img2.setScaledContents(True)
                        self.ui.lbl_info2.setText(table_rece[indice_random][0])
                        magnitud += 1
                    elif magnitud == 3:
                        self.ui.lbl_img3.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img3.setScaledContents(True)
                        self.ui.lbl_info3.setText(table_rece[indice_random][0])
                        magnitud += 1
                    elif magnitud == 4:
                        self.ui.lbl_img4.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img4.setScaledContents(True)
                        self.ui.lbl_info4.setText(table_rece[indice_random][0])
                        magnitud += 1
                    elif magnitud == 5:
                        self.ui.lbl_img5.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img5.setScaledContents(True)
                        self.ui.lbl_info5.setText(table_rece[indice_random][0])
                        magnitud += 1
                    elif magnitud == 6:
                        self.ui.lbl_img6.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img6.setScaledContents(True)
                        self.ui.lbl_info6.setText(table_rece[indice_random][0])
                        magnitud += 1
            elif tamaño < 6 :
                while magnitud <= tamaño:
                    indice_random = random.randint(0,tamaño-1)
                    if magnitud == 1 and magnitud <= tamaño:
                        self.ui.lbl_img1.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img1.setScaledContents(True)
                        self.ui.lbl_info1.setText(table_rece[indice_random][0])
                        magnitud += 1
                    elif magnitud == 2 and magnitud <= tamaño:
                        self.ui.lbl_img2.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img2.setScaledContents(True)
                        self.ui.lbl_info2.setText(table_rece[indice_random][0])
                        magnitud += 1
                    elif magnitud == 3 and magnitud <= tamaño:
                        self.ui.lbl_img3.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img3.setScaledContents(True)
                        self.ui.lbl_info3.setText(table_rece[indice_random][0])
                        magnitud += 1
                    elif magnitud == 4 and magnitud <= tamaño:
                        self.ui.lbl_img4.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img4.setScaledContents(True)
                        self.ui.lbl_info4.setText(table_rece[indice_random][0])
                        magnitud += 1
                    elif magnitud == 5 and magnitud <= tamaño:
                        self.ui.lbl_img5.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img5.setScaledContents(True)
                        self.ui.lbl_info5.setText(table_rece[indice_random][0])
                        magnitud += 1
                    elif magnitud == 6 and magnitud <= tamaño:
                        self.ui.lbl_img6.setPixmap(QPixmap(table_rece[indice_random][7]))
                        self.ui.lbl_img6.setScaledContents(True)
                        self.ui.lbl_info6.setText(table_rece[indice_random][0])
                        magnitud += 1
        elif numero == 2:
            tamaño = len(table_recu)
            if tamaño > 6 or tamaño >= 6:
                while magnitud <= 6:
                    indice_random = random.randint(0,tamaño-1)
                    if magnitud == 1:
                        self.ui.lbl_img1.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img1.setScaledContents(True)
                        self.ui.lbl_info1.setText(table_recu[indice_random][2])
                        magnitud += 1
                    elif magnitud == 2:
                        self.ui.lbl_img2.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img2.setScaledContents(True)
                        self.ui.lbl_info2.setText(table_recu[indice_random][2])
                        magnitud += 1
                    elif magnitud == 3:
                        self.ui.lbl_img3.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img3.setScaledContents(True)
                        self.ui.lbl_info3.setText(table_recu[indice_random][2])
                        magnitud += 1
                    elif magnitud == 4:
                        self.ui.lbl_img4.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img4.setScaledContents(True)
                        self.ui.lbl_info4.setText(table_recu[indice_random][2])
                        magnitud += 1
                    elif magnitud == 5:
                        self.ui.lbl_img5.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img5.setScaledContents(True)
                        self.ui.lbl_info5.setText(table_recu[indice_random][2])
                        magnitud += 1
                    elif magnitud == 6:
                        self.ui.lbl_img6.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img6.setScaledContents(True)
                        self.ui.lbl_img6.setScaledContents(True)
                        self.ui.lbl_info6.setText(table_recu[indice_random][2])
                        magnitud += 1
            elif tamaño < 6 :
                while magnitud <= tamaño:
                    indice_random = random.randint(0,tamaño-1)
                    if magnitud == 1 and magnitud <= tamaño:
                        self.ui.lbl_img1.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img1.setScaledContents(True)
                        self.ui.lbl_info1.setText(table_recu[indice_random][2])
                        magnitud += 1
                    elif magnitud == 2 and magnitud <= tamaño:
                        self.ui.lbl_img2.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img2.setScaledContents(True)
                        self.ui.lbl_info2.setText(table_recu[indice_random][2])
                        magnitud += 1
                    elif magnitud == 3 and magnitud <= tamaño:
                        self.ui.lbl_img3.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img3.setScaledContents(True)
                        self.ui.lbl_info3.setText(table_recu[indice_random][2])
                        magnitud += 1
                    elif magnitud == 4 and magnitud <= tamaño:
                        self.ui.lbl_img4.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img4.setScaledContents(True)
                        self.ui.lbl_info4.setText(table_recu[indice_random][2])
                        magnitud += 1
                    elif magnitud == 5 and magnitud <= tamaño:
                        self.ui.lbl_img5.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img5.setScaledContents(True)
                        self.ui.lbl_info5.setText(table_recu[indice_random][2])
                        magnitud += 1
                    elif magnitud == 6 and magnitud <= tamaño:
                        self.ui.lbl_img6.setPixmap(QPixmap(table_recu[indice_random][7]))
                        self.ui.lbl_img6.setScaledContents(True)
                        self.ui.lbl_info6.setText(table_recu[indice_random][2])
                        magnitud += 1
        
        
        
        self.ui.lbl_img5.setScaledContents(True)
        self.ui.lbl_img4.setScaledContents(True)
        self.ui.lbl_img3.setScaledContents(True)
        self.ui.lbl_img2.setScaledContents(True)
        self.ui.lbl_img1.setScaledContents(True)




    #------------------------------------------------------------------------------------------------------------
         

        

        
#---------------------------------------------------------------------------------------------------------------- 

if __name__ == "__main__":
   app = QApplication(sys.argv)
   window = main()
   window.show()
   app.exec() 