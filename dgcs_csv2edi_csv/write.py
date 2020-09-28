# Write module
import os

class Write(object):
    '''Class that saves data to zam_export file.'''
    def __init__(self):

        if os.path.exists('./zam_export.csv'):
            os.remove('./zam_export.csv')
            self.zam_export = open('./zam_export.csv', 'w+')
        else:
            self.zam_export = open('./zam_export.csv', 'w+')
        self.zam_export.write('HEADER;')


    def add_order_number(self, order_number):
        self.zam_export.write('ORDERNUMBER;')
        self.zam_export.write(order_number + ';')

    def add_order_date(self, order_date):
        self.zam_export.write('ORDERDATE;')
        self.zam_export.write(order_date + ';;;;;')

    def add_order_function(self, order_function):
        self.zam_export.write('DOCUMENTFUNCTIONCODE;')
        self.zam_export.write(order_function + ';')

    def add_order_currnecy(self, order_currency):
        self.zam_export.write('ORDERCURRENCY;')
        self.zam_export.write(order_currency)

    def add_buyer_iln(self, buyer_iln):
        self.zam_export.write('\n')
        self.zam_export.write('BUYER;')
        self.zam_export.write('ILN;')
        self.zam_export.write(buyer_iln)

    def add_seller_iln(self, seller_iln):
        self.zam_export.write('\n')
        self.zam_export.write('SELLER;')
        self.zam_export.write('ILN;')
        self.zam_export.write(seller_iln + ';;')

    def add_deliverypoint_iln(self, deliverypoint_iln):
        self.zam_export.write('\n')
        self.zam_export.write('DELIVERYPOINT;')
        self.zam_export.write('ILN;')
        self.zam_export.write(deliverypoint_iln)

    def add_order_lines(self, order_lines):
        self.zam_export.write('\n')
        for line in order_lines:
            self.zam_export.write('LINE;')
            self.zam_export.write('LINENUMBER;')
            self.zam_export.write(line[0] + ';')

            self.zam_export.write('EAN;')
            self.zam_export.write(line[1] + ';;;;;')

            self.zam_export.write('ITEMDESCRIPTION;')
            self.zam_export.write(line[2] + ';')

            self.zam_export.write('ORDEREDQUANTITY;')
            self.zam_export.write(line[3] + ';;;;')

            self.zam_export.write('\n')

    def add_total_lines(self, total_lines):
        self.zam_export.write('ORDERSUMMARY;')
        self.zam_export.write('TOTALLINES;')
        self.zam_export.write(total_lines + ';')

    def add_total_ordered_amount(self, total_ordered_amount):
        self.zam_export.write('TOTALORDEREDAMOUNT;')
        self.zam_export.write(total_ordered_amount)

    def close_file(self):
        self.zam_export.close()












