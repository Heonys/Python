from openpyxl import Workbook

wb = Workbook() ## 워크북 생성 >> 하나의 엑셀파일 
ws = wb.active # 현재 활성화된 워크시트  
ws.title = 'HeonSheet' #이름 변경
wb.save('sample.xlsx')
wb.close()

