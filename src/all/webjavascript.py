#coding=utf-8
from selenium import webdriver 
import time,os
    
driver = webdriver.Firefox()
#file_path =  'file:///' + os.path.abspath('js.html')
file_path='C:\edaixi_testdata\js.html'
print "file_path ",file_path
driver.get(file_path)
    
#######通过JS 隐藏选中的元素#########
#第一种方法：
driver.execute_script('$("#tooltip").fadeOut();')
time.sleep(5)
    
#第二种方法：
button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut()',button)
time.sleep(5)
    
driver.quit()