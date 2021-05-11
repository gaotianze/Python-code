import xlrd
import json
from train_graph.MainGraphWindow import MainGraphWindow
from PyQt5.QtWidgets import QApplication
import sys

'''文件位置，自行修改'''
address='C:\\Users\\Administrator\\Desktop\\train_graph-3.3.2-R50_魔改版\\train_graph-3.3.2-R50\\'
file_name='demo.json'
excel_name='数据表.xlsx'

excel = xlrd.open_workbook(excel_name)
sheet0=excel.sheet_by_index(0)
sheet1=excel.sheet_by_index(1)
rows_0 = sheet0.nrows
cols_0= sheet0.ncols
nrows = sheet1.nrows
ncols = sheet1.ncols
find=[]
for i in range(ncols):
    if i%2!=0 and i!=ncols-1:
        find.append(i)
find_reverse=find[::-1]

'''头部站名、里程信息为预设'''
data={
  "line": {"name": "", "rulers": [],
          "stations": [],
          "forbid": {"different": True, "nodes": [], "upShow": False, "downShow": False}},
  "trains": [],

  "circuits": [],
  "config": {"seconds_per_pix": 20.0, "seconds_per_pix_y": 8.0, "pixes_per_km": 4.0, "grid_color": "#10F010",
            "text_color": "#0000FF", "default_keche_width": 1.5, "default_huoche_width": 0.75, "start_hour": 20,
            "end_hour": 1, "ordinate": 'null', "minutes_per_vertical_line": 10.0, "bold_line_level": 2,
            "show_line_in_station": True, "not_show_types": [],
            "default_colors": {"快速": "#FF0000", "特快": "#0000FF", "直达特快": "#FF00FF", "动车组": "#804000", "动车": "#804000",
                               "高速": "#FF00BE", "城际": "#FF33CC", "default": "#008000"},
            "showFullCheci": True}, "markdown": ""}

for i in range(1,rows_0):
    stations_add = {"zhanming": "Null", "licheng": 0, "dengji": 4, "show": True, "direction": 3, "y_value": 0}
    stations_add['zhanming']=sheet0.row_values(i)[0]
    stations_add['licheng']=int(sheet0.row_values(i)[1])
    data['line']['stations'].append(stations_add)

for i in range(1,nrows):

    if sheet1.row_values(i)[-1]==0:
        train = {"checi": [], "UI": {}, "type": "",
                 "timetable": [],
                 "sfz": "", "zdz": "", "shown": True}

        train['checi'].append(sheet1.row_values(i)[0])
        train['checi'].append(sheet1.row_values(i)[0])
        train['checi'].append('')
        train['type']='快速'

        '''find定位奇数列'''
        for j in find:
            item = {"zhanming": "", "ddsj": "", "cfsj": "", "note": ""}
            if sheet1.row_values(i)[j]!="":
                item['zhanming']=sheet1.row_values(0)[j]
                item['ddsj'] = sheet1.row_values(i)[j]
                item['cfsj'] = sheet1.row_values(i)[j+1]
                train['timetable'].append(item)

    elif sheet1.row_values(i)[-1]==1:
        train = {"checi": [], "UI": {}, "type": "",
                 "timetable": [],
                 "sfz": "", "zdz": "", "shown": True}

        train['checi'].append(sheet1.row_values(i)[0])
        train['checi'].append(sheet1.row_values(i)[0])
        train['checi'].append('')
        train['type'] = '快速'

        '''find定位奇数列'''
        for j in find_reverse:
            item = {"zhanming": "", "ddsj": "", "cfsj": "", "note": ""}
            if sheet1.row_values(i)[j] != "":
                item['zhanming'] = sheet1.row_values(0)[j]
                item['ddsj'] = sheet1.row_values(i)[j+1]
                item['cfsj'] = sheet1.row_values(i)[j]
                train['timetable'].append(item)

    data["trains"].append(train)
print("--------Data--------")
print(data)
print("---------End--------")

with open(address+file_name, 'w') as file:
    json.dump(data,file)
    print("Converted!")

print("Launching pyETRC...")
print("-------PyETRC-------")

app = QApplication(sys.argv)
try:
    f = sys.argv[1]
except IndexError:
    f = None
mainWindow = MainGraphWindow(f)
mainWindow.showMaximized()
app.exec_()

