# -*- coding:gb2312 -*-
import xlrd

def GetUser():
    bk = xlrd.open_workbook("excel�ļ�����") # ��excel�ļ�
    sh = bk.sheet_by_name("excel����")# ��excel��
    nrows = sh.nrows # ��ȡ������
    for i in range(1,nrows):  
        TestCase = sh.cell_value(i,0)
        uname = sh.cell_value(i,1)
        method = sh.cell_value(i,2)
        EX_Result=sh.cell_value(i,3)
        WriterLog('Testcase Name:'+TestCase+'TestData: uname = '+uname+' ,method = '+method+' ,EX_Result = ' + EX_Result) # д������־
        AC_result = httpgetGetUserInfo(uname,method) # ����API�ӿ�
        WriterLog('AC_result = ' + AC_result) # д������־
        if EX_Result == AC_result: #ʵ�ʽ����Ԥ�ڽ���Ա�
            WriterLog(...) #д������־
            WriterReport(...)#д���Ա���
        else
            WriterLog(...)#д������־
            WriterReport(...)#д���Ա���
