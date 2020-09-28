# Send module
from ftplib import FTP
import time


class Send(object):
    '''Class that sends export files to the ftp server.'''
    def send(self, server_address, login, password, ftp_port):
        ftp = FTP()
        ftp.set_debuglevel(2)
        ftp.connect(server_address, ftp_port)
        ftp.login(login, password)
        ftp.cwd('/zamowienia_export')
        ftp.storbinary('STOR ' + './zam_export' + time.strftime("%d%m%Y-%H%M%S") + '.csv', open('./zam_export.csv', 'rb'))
        ftp.close()
