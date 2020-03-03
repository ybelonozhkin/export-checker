import os
import csv
import time

print (" ")
print ("*************")
print ("НАЧАЛО РАБОТЫ")
print ("*************")
print (" ")

timestr = time.strftime("%Y%m%d-%H%M%S")

# List all files in a directory using scandir()
basepath = "c:\Temp"
errorlog = "error" + format(timestr) + ".log"
errorlogfile = basepath + "\\" + errorlog
print (errorlog)

errlog = open(errorlogfile, "a")
errlog.write("Начало проверки" + '\n' + '\n')
filecounter = 0
stringcounter = 0

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file() and entry.name.endswith(".csv"):
            filecounter = filecounter + 1
            full_file_name = basepath + '\\' + entry.name
            print ("Проверяю: " + format(full_file_name))
            filesize = os.path.getsize (full_file_name)
            if filesize == 0:
                print ("Пустой файл")
                errlog.write(full_file_name + '\n')
                errlog.write("Пустой файл" + '\n' + '\n')
            elif filesize > 0:
                with open(full_file_name) as csv_file:
                    reader = csv.reader(csv_file, delimiter = ';')
                    counter = 0
                    print ("Проверяю пополнения")
                    for row in reader:
                        stringcounter = stringcounter + 1
                        if row[7] == "":
                            counter = counter + 1

                    # print ("Пополнений: " + format(counter))
                    if counter == 0:
                        print ("0 пополнений, проверь по отчётам")
                        errlog.write(full_file_name + '\n')
                        errlog.write("Нет пополнений, проверь по отчётам" + '\n')
                with open(full_file_name) as csv_file:                    
                    print ("Проверяю карты: колонка 12, item=10, столбец 25")
                    reader = csv.reader(csv_file, delimiter = ';')
                    troublecounter = 0
                    counter = 0
                    for row in reader:
                        stringcounter = stringcounter + 1
                        # errlog.write(full_file_name + '\n')
                        counter = counter +1
                        if row[11] == "10" and row[24] == "":
                            troublecounter = troublecounter + 1
                            errlog.write(full_file_name + '\n')
                            logentry = format(row)
                            errlog.write("Строка " + format(counter) + ". Нет номера карты в столбце 25"'\n')
                            errlog.write(logentry + '\n' + '\n')
                    # print ("Проверил: " + format(counter) + " строк")
                    if troublecounter > 0:
                        print ("Строк без карт: " + format(troublecounter))

                
                with open(full_file_name) as csv_file:                    
                    print ("Проверяю Золотые карты: колонка 12, item=14, столбец 26")
                    reader = csv.reader(csv_file, delimiter = ';')
                    troublecounter = 0
                    counter = 0
                    for row in reader:
                        stringcounter = stringcounter + 1
                        counter = counter +1
                        if row[11] == "14" and row[25] == "":
                            troublecounter = troublecounter + 1
                            errlog.write(full_file_name + '\n')
                            logentry = format(row)
                            errlog.write("Строка " + format(counter) + ". Нет номера карты в столбце 26"'\n')
                            errlog.write(logentry + '\n' + '\n')
                    # print ("Проверил: " + format(counter) + " строк")
                    if troublecounter > 0:
                        print ("Строк без карт: " + format(troublecounter))
                with open(full_file_name) as csv_file:                    
                    print ("Проверяю замены карт: колонка 12, item=1500000, столбец 25 и 26")
                    reader = csv.reader(csv_file, delimiter = ';')
                    troublecounter = 0
                    counter = 0
                    for row in reader:
                        stringcounter = stringcounter + 1
                        counter = counter +1
                        if row[11] == "1500000":
                            if row[24] == "" or row[25] == "":
                                troublecounter = troublecounter + 1
                                errlog.write(full_file_name + '\n')
                                logentry = format(row)
                                errlog.write("Строка " + format(counter) + ". Нет номера карты в столбце 25 или 26"'\n')
                                errlog.write(logentry + '\n' + '\n')
                    # print ("Проверил: " + format(counter) + " строк")
                    if troublecounter > 0:
                        print ("Строк без карт: " + format(troublecounter))
                with open(full_file_name) as csv_file:                    
                    print ("Проверяю награды: колонка 27 = Награда, столбец 29 и 43")
                    reader = csv.reader(csv_file, delimiter = ';')
                    troublecounter = 0
                    counter = 0
                    for row in reader:
                        stringcounter = stringcounter + 1
                        counter = counter +1
                        if row[26] == "Награда":
                            if row[28] == "" or row[42] == "":
                                troublecounter = troublecounter + 1
                                errlog.write(full_file_name + '\n')
                                logentry = format(row)
                                errlog.write("Строка " + format(counter) + ". Для награды нет номера карты в столбце 29 или 43"'\n')
                                errlog.write(logentry + '\n' + '\n')
                    # print ("Проверил: " + format(counter) + " строк")
                    if troublecounter > 0:
                        print ("Строк без карт: " + format(troublecounter))

                with open(full_file_name) as csv_file:                    
                    print ("Проверяю карты: колонка 20 = 400, столбец 26")
                    reader = csv.reader(csv_file, delimiter = ';')
                    troublecounter = 0
                    counter = 0
                    for row in reader:
                        stringcounter = stringcounter + 1
                        counter = counter +1
                        if row[19] == "400":
                            if row[25] == "":
                                troublecounter = troublecounter + 1
                                errlog.write(full_file_name + '\n')
                                logentry = format(row)
                                errlog.write("Строка " + format(counter) + ". Нет номера карты в столбце 25"'\n')
                                errlog.write(logentry + '\n' + '\n')
                    # print ("Проверил: " + format(counter) + " строк")
                    if troublecounter > 0:
                        print ("Строк без карт: " + format(troublecounter))

                errlog.write('\n')

            print ("Закончил проверку")
            print (" ")

errlog.write("Проверено файлов: " + format(filecounter) + ", строк: " + format(stringcounter))
print (" ")
print ("*************")
print ("КОНЕЦ РАБОТЫ")
print ("*************")
print (" ")