# -*- coding: utf-8 -*-
__author__ = "eason"
from win32com.client import Dispatch
import os


def excel_decrypt(src_file: str, password: str, del_src: bool = False)->bool:
    """
    Excel解密
    :param src_file:待解密Excel文件路径
    :param password:密码,多个密码用英文逗号隔开
    :param del_src:是否删除原始加密文件
    :return:
    """
    flag = False
    if "," in password:
        passwords = password.split(",")
        for pwd in passwords:
            try:
                xlapp = Dispatch("Excel.Application")
                xlapp.Workbooks.Open(src_file, False, True, None, pwd)
                file_name = src_file.split("\\")[-1]
                file_location = src_file[0:(len(src_file) - len(file_name))]
                wb = xlapp.Workbooks[0]
                wb.Password = ""
                xlapp.ActiveWorkbook.SaveAs(os.path.join(file_location, ("(decrypted)" + file_name)))
                xlapp.Quit()
                flag = True
                print("decrypt success![%s]" % pwd)
                if del_src:
                    try:
                        os.remove(src_file)
                        print("origin file delete success![%s]" % src_file)
                    except Exception as e:
                        print("origin file delete failed![%s]" % src_file)
                break
            except Exception as e:
                print("wrong password![%s]" % pwd)
    else:
        try:
            xlapp = Dispatch("Excel.Application")
            xlapp.Workbooks.Open(src_file, False, True, None, password)
            file_name = src_file.split("\\")[-1]
            file_location = src_file[0:(len(src_file)-len(file_name))]
            wb = xlapp.Workbooks[0]
            wb.Password = ""
            xlapp.ActiveWorkbook.SaveAs(os.path.join(file_location, ("(decrypted)"+file_name)))
            xlapp.Quit()
            flag = True
            print("decrypt success![%s]" % password)
            if del_src:
                try:
                    os.remove(src_file)
                    print("origin file delete success![%s]" % src_file)
                except Exception as e:
                    print("origin file delete failed![%s]" % src_file)
        except Exception as e:
            print("wrong password![%s]" % password)
    return flag


if __name__ == "__main__":
    print(excel_decrypt(r"C:\Users\eason\Desktop\test\decrypt\t1.xls", password="111111,123456,121212", del_src=True))
    print(excel_decrypt(r"C:\Users\eason\Desktop\test\decrypt\t2.xlsx", password="111111,123456,121212", del_src=False))