import pandas as pd 
import openpyxl
import xlsxwriter
'''
การลง library
pip install pandas
pip install xlsxwriter
pip install xlrd
'''
 
# อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
readDataframe = pd.read_excel (r'pandastest.xlsx')
 
# สร้างข้อมูลใหม่เป็นข้อมูลของ orange
newDataframe = pd.DataFrame({'Pvp Daily' : ['120'], 'PVE':  [75]})
 # print (dataframe['Name']) ปริ้น Column
 
# นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
frames = [readDataframe, newDataframe]
result = pd.concat(frames)
 
# สร้าง Writer เหมือนกับตอนเขียนไฟล์
writer = pd.ExcelWriter('Pandastest.xlsx', engine='xlsxwriter')
 
# นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
result.to_excel(writer, index = False)
writer.save()