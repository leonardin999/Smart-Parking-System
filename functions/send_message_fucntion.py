from modules import *
import pymysql
from Dialog import CustomDbConnectionDialog, CustomMessageInformation
from PySide6.QtCore import Qt
import time
import smtplib


class MessageFunctions(MessageWindow):

    def initial_connection(self):
        try:
            self.db = pymysql.connect(host="localhost",
                                      user="root",
                                      database="parking",
                                      passwd="")
            if self.db is not None:
                self.db_connection = True
        except:
            dialog = CustomDbConnectionDialog()
            if dialog.exec_():
                self.db_connection = False
            else:
                self.db_connection = False

    def reset_tools(self):
        self.founded = False
        self.license_search.clear()
        self.license_search.setPlaceholderText('insert license number...')
        self.license_search.setFocusPolicy(Qt.StrongFocus)
        self.name_edit.clear()
        self.number_edit.clear()
        self.slot_edit.clear()

    def search_information(self):
        if self.license_search.text() is not None and self.db_connection:
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            query = f"SELECT db.username,db.phone,db.license_number,s.slot_name " \
                    "FROM software_db as db " \
                    "LEFT JOIN slots as s " \
                    "ON db.slot = s.id " \
                    "WHERE db.license_number = '%s'" % self.license_search.text()
            self.cursor.execute(query)
            data = self.cursor.fetchone()
            if data is not None:
                self.founded = True
                self.name_edit.setText(data['username'])
                self.number_edit.setText(data['phone'])
                self.slot_edit.setText(data['slot_name'])
            else:
                error_message = f'Cannot find the Information of result {self.license_search.text()}.\n' \
                                f'Please Try Again!'
                dialog = CustomMessageInformation(error_message)
                if dialog.exec_():
                    MessageFunctions.reset_tools(self)
                else:
                    self.founded = False
                    pass
        else:
            error_message = f'Information cannot be empty.\n' \
                            f'Please Try Again!'
            dialog = CustomMessageInformation(error_message)
            if dialog.exec_():
                MessageFunctions.reset_tools(self)
            else:
                pass

    def check_field_empty(self):
        if (self.name_edit.text() is None or
                self.number_edit.text() is None):
            error_message = f'input field cannot be empty.\n' \
                            f'Please Try Again!'
            dialog = CustomMessageInformation(error_message)
            if dialog.exec_():
                return False
            else:
                return False
        return True

    def check_valid_number(self):
        if len(self.number_edit.text()) == 10 \
                and all([x.isdigit() for x in self.number_edit.text().split()]):
            return True
        else:
            error_message = f'Invalid Phone number.\n' \
                            f'Please Try Again!'
            dialog = CustomMessageInformation(error_message)
            if dialog.exec_():
                return False
            else:
                return False

    def update_table(self):

        if self.db_connection:
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            sql_update = f"UPDATE software_db SET username=%s, phone=%s WHERE license_number= %s"
            data = (self.name_edit.text(),
                    self.number_edit.text(),
                    self.license_search.text())
            self.cursor.execute(sql_update, data)
            self.db.commit()
            self.cursor.close()
            confirm_message = 'information saved.'
            dialog = CustomMessageInformation(confirm_message)
            if dialog.exec_():
                pass

    def update_vehicle_detail(self):

        if self.db_connection:
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            sql_update = f"UPDATE vehicle_detail SET type=%s WHERE license_number= %s"
            data = (self.name_edit_2.text(),
                    self.license_search.text())
            self.cursor.execute(sql_update, data)
            self.db.commit()
            self.cursor.close()

    def save_information(self):
        if (MessageFunctions.check_field_empty(self) and
                MessageFunctions.check_valid_number(self)):
            MessageFunctions.update_table(self)
            MessageFunctions.update_vehicle_detail(self)
        return

    def check_valid_mail(self):
        import re
        regex = r'(\W|^)[\w.+\-]*@gmail\.com(\W|$)'
        email = self.email_edit.text().strip()
        if email:
            if re.fullmatch(regex, email):
                return True
            return False
        return False

    def send_SMS(self):
        error_message = f'This Module will be updated soon.'
        dialog = CustomMessageInformation(error_message)
        if dialog.exec_():
            return

    def send_Email(self):
        # Creating SMTP Client Session
        if MessageFunctions.check_valid_mail(self):
            smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpobj.starttls()
            sender_email_id = "freemailvt1999@gmail.com"
            sender_email_id_password = "12345678Aa#"
            receiver_email_id = self.email_edit.text()
            smtpobj.login(sender_email_id, sender_email_id_password)
            message = f"""
            From: From Mr.President, <{sender_email_id}>
            To: To {self.name_edit.text()} <{self.email_edit.text()}>
            Subject: Notification from Smart Parking System
            
            Hello {self.name_edit.text()},\n
            Welcome to The Smart Parking System Company.\n
            Your Parking slot number is {self.slot_edit.text()}.
            Enjoy your services Here. Have a nice day!
    
            """
            smtpobj.sendmail(sender_email_id, receiver_email_id, message)
            smtpobj.quit()
            confirm_message = f'Information has been sent to email: \n' \
                              f'{receiver_email_id}!'
            dialog = CustomMessageInformation(confirm_message)
            if dialog.exec_():
                return
        else:
            error_message = f'Invalid Email format.\n' \
                            f'Please try again.'
            dialog = CustomMessageInformation(error_message)
            if dialog.exec_():
                return

