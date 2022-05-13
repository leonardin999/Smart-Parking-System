import time

from modules import *
import pymysql
from Dialog import CustomDbConnectionDialog
from PySide6.QtWidgets import QTableWidgetItem
from Dialog import CustomUpdateToolsDialog, \
    CustomEntryNotify, \
    CustomExitNotify, \
    CustomAcceptedInformation
import webbrowser
from functions import SystemFunctions


class DatabaseFunctions(MainWindow):

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

    def show_table_data(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.clear()
            self.tableWidget.removeRow(0)

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(("License Number", "Username", "Phone", "Slot", "Check-in"))
        col = 0
        row = 0
        if self.db_connection:
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            query = "SELECT db.license_number,db.username" \
                    ",db.phone,s.slot_name,db.in_time " \
                    "FROM software_db as db " \
                    "LEFT JOIN slots as s " \
                    "ON db.slot = s.id"

            self.cursor.execute(query)
            all_data = self.cursor.fetchall()
            self.db.commit()
            self.cursor.close()
            for data in all_data:
                self.tableWidget.insertRow(row)
                for key, item in data.items():
                    if key == 'in_time':
                        format_item = item.split('T')
                        new = ' '.join(format_item)
                        self.tableWidget.setItem(row, col, QTableWidgetItem(new.strip()))
                        col += 1
                        continue
                    self.tableWidget.setItem(row, col, QTableWidgetItem(item))
                    col += 1
                row += 1
                col = 0
            # closing the cursor

    def counted_function(self):
        reserved_slot = 0
        available_slot = 0
        total_car = 0
        if self.db_connection:
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            slot_count_query = f"SELECT * FROM slots"
            self.cursor.execute(slot_count_query)
            all_data = self.cursor.fetchall()
            for data in all_data:
                if data['active'] == 1 and data['availability_status'] == 1:
                    available_slot += 1
                if data['active'] == 2:
                    reserved_slot += 1

            car_count_query = "SELECT * FROM `vehicle_details`"
            self.cursor.execute(car_count_query)
            total_car = len(self.cursor.fetchall())
            self.cursor.close()
        self.slot_display.setText(str(reserved_slot))
        self.available_slot_display.setText(str(available_slot))
        self.car_display.setText(str(total_car))

    @staticmethod
    def unfinished_function(self):
        dialog = CustomUpdateToolsDialog()
        if dialog.exec_():
            pass
        else:
            pass

    def check_reserved(self, plate=None):
        reserved_list = []
        if self.db_connection:
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            query = "SELECT license_number, entry_status, deleted " \
                    "FROM vehicle_details"

            self.cursor.execute(query)
            all_data = self.cursor.fetchall()
            for data in all_data:
                if data['deleted'] == 0 and data['entry_status'] is None:
                    reserved_list.append(data['license_number'].strip())
            self.cursor.close()
            if plate.trip() in reserved_list:
                return True
            return False
        return False


    def change_entry_status(self, plate=None):
        entry_status = False
        if self.db_connection:
            if plate:
                self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
                selected_query = f"SELECT * FROM vehicle_details WHERE license_number='{plate}'"
                # data = ("0","72A-9999")
                self.cursor.execute(selected_query)
                all_data = self.cursor.fetchall()
                for data in all_data:
                    if data['entry_status'] is None and data['deleted'] == 0:
                        update_query = f"UPDATE vehicle_details SET entry_status= %s where license_number= %s"
                        data = ("0", plate)
                        self.cursor.execute(update_query, data)
                self.db.commit()
                self.cursor.close()
                entry_status = True

        if entry_status:
            CustomEntryNotify()

    def change_exit_status(self, plate=None):
        exit_status = False
        if self.db_connection:
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            if plate:
                selected_query = f"SELECT * FROM vehicle_details WHERE license_number='{plate}'"
                # data = ("0","72A-9999")
                self.cursor.execute(selected_query)
                all_data = self.cursor.fetchall()
                for data in all_data:
                    if data['entry_status'] == 0:
                        update_query = f"UPDATE vehicle_details SET entry_status= %s where license_number= %s"
                        data = ("1", plate)
                        self.cursor.execute(update_query, data)
                    else:
                        self.cursor.close()
                        exit_status = False
                        return None
                self.db.commit()
                self.cursor.close()
                exit_status = True

        if exit_status:
            CustomExitNotify()

    def update_table(self, plate=None, slot_id=None):
        if self.db_connection:
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M")
            if plate is not None and slot_id is not None:
                self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
                insert_query = f"INSERT INTO software_db(username,phone,license_number,type, slot, in_time) " \
                               f"VALUES ('unknown','+00-00-000-0000',{plate}','unknown',{slot_id},{current_time});"
                self.cursor.execute(insert_query)
                self.db.commit()
                self.cursor.close()
                DatabaseFunctions.refresh_page(self)

    @staticmethod
    def update_parking_page(self):
        url = "http://localhost/parking/parking/create"
        webbrowser.open_new_tab(url)

    @staticmethod
    def get_payment_update(self, plate):

        url = f"http://localhost/parking/parking"
        webbrowser.open_new_tab(url)

    def get_slot_name(self, slot_id):
        slot_name = ''
        if self.db_connection:
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            selected_query = f"SELECT slot_name FROM slots WHERE id='{slot_id}'"
            self.cursor.execute(selected_query)
            data = self.cursor.fetchone()
            slot_name = data['slot_name']
            self.cursor.close()
        return slot_name

    def get_slot_name_reserved(self, plate):
        slot_name = ''
        if self.db_connection:
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            query = f"SELECT slot FROM software_db WHERE license_number ='{plate}'"
            self.cursor.execute(query)
            data = self.cursor.fetchone()
            self.cursor.close()
            slot_id = data['slot']
            slot_name = DatabaseFunctions.get_slot_name(slot_id)
        return slot_name

    def update_entry_information(self, plate=None):
        available_slot = []
        if self.db_connection:
            if DatabaseFunctions.check_reserved(self, plate):
                DatabaseFunctions.change_entry_status(self, plate)
                name = DatabaseFunctions.get_slot_name_reserved(self, plate)
                if name:
                    SystemFunctions.send_information(self, name)
                DatabaseFunctions.update_parking_page(self)
            else:
                self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
                selected_query = f"SELECT * FROM slots"
                # data = ("0","72A-9999")
                self.cursor.execute(selected_query)
                all_data = self.cursor.fetchall()
                for data in all_data:
                    if data['active'] == 1 and data['availability_status'] == 1:
                        available_slot.append(data['id'])

                if available_slot:
                    import random
                    slot_id = random.choice(available_slot)
                    insert_query = f"INSERT INTO Vehicle_Details(license_number,deleted) " \
                                   f"VALUES ('{plate}',0);"
                    self.cursor.execute(insert_query)
                    update_query = f"UPDATE slots SET active= %s where id= %s"
                    data = ("2", str(slot_id))
                    self.cursor.execute(update_query, data)
                    self.db.commit()
                    self.cursor.close()
                    time.sleep(0.5)
                    DatabaseFunctions.change_entry_status(self, plate)
                    DatabaseFunctions.update_parking_page(self)
                    # for only unreserved clients
                    DatabaseFunctions.update_table(self, plate, slot_id)
                    name = DatabaseFunctions.get_slot_name(self, slot_id)
                    if name:
                        SystemFunctions.send_information(self, name)

            DatabaseFunctions.show_table_data(self)
            DatabaseFunctions.counted_function(self)

    def update_exit_information(self, plate=None):
        if self.db_connection:
            if plate:
                DatabaseFunctions.change_exit_status(self, plate)
                DatabaseFunctions.get_payment_update(self)

    def Ask_for_permission_get_in(self, plate):
        if self.accept_entrance.isChecked():
            dialog = CustomAcceptedInformation(plate)
            if dialog.exec_():
                DatabaseFunctions.update_entry_information(self)
            else:
                pass

    def Ask_for_permission_get_out(self, plate):
        if self.accept_exit.isChecked():
            dialog = CustomAcceptedInformation(plate)
            if dialog.exec_():
                DatabaseFunctions.update_exit_information(self)
            else:
                pass
