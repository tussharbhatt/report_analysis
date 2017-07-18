
from openpyxl import load_workbook
import os

'''def get_client_name(sheet):

    stats = {}
    for i in range(2,200000):
        if sheet["T{}".format(str(i))].value in stats:
            stats[(sheet["T{}".format(str(i))].value)] += 1
        else:
            stats[sheet["T{}".format(str(i))].value] = 1
    return stats
'''

filename="BigFile.xlsx"
os.chdir("C:\\Users\\tushar.bhatt\\Desktop")
wb=load_workbook(filename)
print(wb.get_sheet_names())
name=wb.get_sheet_names()
sheet=wb.get_sheet_by_name(name[0])
print(sheet.title)
print(wb.active)


#print(sheet['C'].value)
def get_valid_times(sheet):
    print(os.path.abspath(__file__))
    with open("plain_text.txt", 'w+') as fout:
        for i in range(2, 200):
            temp = sheet["T{}".format(str(i))].value
            # print("c{}".format(str(i)))
            # if temp == sheet["I5"].value:
            # continue
            #print(temp)
            fout.write(str(temp))
    #fout.close()
    return
get_valid_times(sheet)

wb.close()
'''client_names=dict()
client_names=get_client_name(sheet)
print(client_names)
sum=0
for key in client_names.keys():
    sum+=client_names[key]
print(sum)
#print(client_names[0])
'''