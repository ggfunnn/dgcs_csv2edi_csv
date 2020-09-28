# Read module
import csv
import sys
import os

class Read(object):
    '''Class that reads data from DGCS' CSV file.'''
    def __init__(self):
        self.f = open(sys.argv[1], 'r')
        self.f.readline()
        self.reader = csv.reader(self.f)

    def get_order_date(self):
        order_date_dgcs = self.f.readline()
        order_date_dgcs = order_date_dgcs.replace('Data wprowadzenia', '')
        order_date_dgcs = order_date_dgcs.replace(',', '')
        order_date_dgcs = order_date_dgcs.replace('-', '')

        quantity = 0
        day = ''
        month = ''
        year = ''
        for char in order_date_dgcs:
            quantity += 1
            if quantity < 3:
                day += char

            elif quantity < 5 >= 3:
                month += char

            else:
                year += char

        year = year.rstrip('\n')

        order_date = year + '-' + month + '-' + day
        print(order_date)
        return order_date

    def get_order_number(self):
        order_number = self.f.readline()
        order_number = order_number.replace('Zamówienie nr ', '')
        order_number = order_number.replace(',', '')
        order_number = order_number.rstrip('\n')
        print(order_number)
        return order_number

    def get_order_function(self):
        order_function = 'O'
        print(order_function)
        return order_function

    def get_order_currency(self):
        order_currency = 'PLN'
        print(order_currency)
        return order_currency

    def get_order_lines(self):
        l = self.f.readline()

        while 'L.p' not in l:
            l = self.f.readline()

        order_lines = []
        self.total_lines = 0
        self.total_ordered_amount = 0
        for row in self.reader:
            if 'szt.' in row:
                self.total_lines += 1

                while ("" in row):
                    row.remove('')

                order_line = []
                line_number = row[0]
                line_name = row[1]
                line_ean = row[3]

                line_quantity = row[4]
                line_quantity = line_quantity.replace(' ', '')
                line_quantity = line_quantity.replace(',', '.')
                line_quantity += '0'

                self.total_ordered_amount += float(line_quantity)

                order_line.append(line_number)
                order_line.append(line_ean)
                order_line.append(line_name)
                order_line.append(line_quantity)

                order_lines.append(order_line)
        print(order_lines)
        return(order_lines)

    def get_total_lines(self):
        print(self.total_lines)
        self.total_lines = str(self.total_lines)
        return self.total_lines # from get_order_lines

    def get_total_ordered_amount(self):
        self.total_ordered_amount = str(self.total_ordered_amount)
        self.total_ordered_amount += '00'
        print(self.total_ordered_amount)
        return self.total_ordered_amount # from get_order_lines

    def delete(self):
        os.remove(sys.argv[1])




