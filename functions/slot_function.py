from modules import *
import pymysql
import time


class SlotFunctions(MainWindow):

    def initial_slot(self):
        SlotFunctions.display_information(self, '', '', '')
        self.all_opt.setChecked(True)
        self.slot_map = [self.slot_0, self.slot_1, self.slot_2,
                         self.slot_3, self.slot_4, self.slot_5,
                         self.slot_6, self.slot_7, self.slot_8,
                         self.slot_9, self.slot_10, self.slot_11]
        self.slots_name = []
        self.avalable_list = []
        self.reserved_list = []
        self.unavailable_list = []

        self.color = {'green': '#00aa00',
                      'yellow': '#d4d400',
                      'red': '#c30000'}
        style_str = "QPushButton {background-color: %s; color: #000000;}" \
                    "QPushButton:hover {" \
                    "background-color: rgb(240, 240, 240);" \
                    "color:#000000;}" \
                    "QPushButton:pressed {" \
                    "background-color: rgb(65, 64, 66);" \
                    "color: rgb(240, 235, 225);}"
        if self.db_connection:
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            slot_query = f"SELECT * FROM slots"
            self.cursor.execute(slot_query)
            all_data = self.cursor.fetchall()
            for data in all_data:
                self.slots_name.append(data['slot_name'])
                if data['active'] == 1 and data['availability_status'] == 1:
                    self.slot_map[int(data['id'])].setStyleSheet(style_str % self.color['green'])
                    self.avalable_list.append(self.slot_map[int(data['id'])])
                elif data['active'] == 2 and data['availability_status'] == 1:
                    self.slot_map[int(data['id'])].setStyleSheet(style_str % self.color['yellow'])
                    self.reserved_list.append(self.slot_map[int(data['id'])])
                elif data['active'] == 2 and data['availability_status'] == 2:
                    self.slot_map[int(data['id'])].setStyleSheet(style_str % self.color['red'])
                    self.unavailable_list.append(self.slot_map[int(data['id'])])
                self.cursor.close()
        SlotFunctions.show_all_slot(self)
        SlotFunctions.set_button_function(self)
        return None

    def show_all_slot(self):
        for item in self.slot_map:
            item.setVisible(True)
            item.clicked.connect(lambda: SlotFunctions.display_information(self, '', '', ''))

    def show_reserved_list(self):
        for item in self.slot_map:
            item.setVisible(False)

        for item in self.reserved_list:
            item.setVisible(True)

    def show_available_list(self):
        for item in self.slot_map:
            item.setVisible(False)

        for item in self.avalable_list:
            item.setVisible(True)

    def show_unavailable_list(self):
        for item in self.slot_map:
            item.setVisible(False)

        for item in self.unavailable_list:
            item.setVisible(True)

    def display_information(self, plate, name, time):
        self.entry_edit.setText(time)
        self.lincense_edit.setText(plate)
        self.type_edit.setText(name)

    def set_button_function(self):
        if self.db_connection:
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
            self.cursor.execute("SELECT p.vechile_id, p.slot_id, p.in_time, "
                                "s.slot_name, v.type, v.license_number "
                                "FROM parking as p "
                                "LEFT JOIN slots as s ON p.slot_id = s.id "
                                "LEFT JOIN vehicle_details as v ON p.vechile_id = v.id "
                                "WHERE p.paid_status IN ('0');")
            all_data = self.cursor.fetchall()
            for data in all_data:
                struct_time = time.localtime(int(data['in_time']))
                format_time = time.strftime('%Y-%m-%d  %H:%M:%S', struct_time)
                self.slot_map[data['slot_id']].clicked.connect(lambda:
                                                               SlotFunctions.display_information(self,
                                                                                                 data['license_number'],
                                                                                                 data['type'],
                                                                                                 format_time))
