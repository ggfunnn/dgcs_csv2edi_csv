# Main file
from dgcs_csv2edi_csv import read
from dgcs_csv2edi_csv import write
from dgcs_csv2edi_csv import send
import configparser
import os


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'dgcs_csv2edi_csv', 'config.ini'))

Buyer_iln = config['WRITE']['Buyer_iln']
Seller_iln = config['WRITE']['Seller_iln']
Deliverypoint_iln = config['WRITE']['Deliverypoint_iln']

Server_address = config['SEND']['Server_address']
Login = config['SEND']['Login']
Password = config['SEND']['Password']
Ftp_port = int(config['SEND']['Ftp_port'])

reader = read.Read()
writer = write.Write()
sender = send.Send()

order_date = reader.get_order_date()
order_number = reader.get_order_number()
order_function = reader.get_order_function()
order_currency = reader.get_order_currency()
order_lines = reader.get_order_lines()
total_lines = reader.get_total_lines()
total_ordered_amount = reader.get_total_ordered_amount()

writer.add_order_number(order_number)
writer.add_order_date(order_date)
writer.add_order_function(order_function)
writer.add_order_currnecy(order_currency)
writer.add_buyer_iln(Buyer_iln)
writer.add_seller_iln(Seller_iln)
writer.add_deliverypoint_iln(Deliverypoint_iln)
writer.add_order_lines(order_lines)
writer.add_total_lines(total_lines)
writer.add_total_ordered_amount(total_ordered_amount)
writer.close_file()

sender.send(Server_address, Login, Password, Ftp_port)