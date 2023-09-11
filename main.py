import pandas as pd 
# Загрузка данных из файла Excel
data = pd.read_excel("lab_pi_101.xlsx")


# Кол-во оценок
last_row = data.shape[0]

# Кол-во оценок, которые относятся к группе ПИ101
score = data['Группа'].str.contains('ПИ101').sum()

#Кол-во студентов 
Number = data['Личный номер студента']
Number1 = []
for i in Number:
    if i not in Number1:
        Number1.append(i)
Number2 = len(Number1)

#Кол-во студентов из группы ПИ101
stud_PI101 = len(data[data['Группа'] == 'ПИ101']['Личный номер студента'].unique())

#Личные номера студентов группы ПИ101
pi101 = data.loc[data['Группа']== 'ПИ101' , 'Личный номер студента'].unique()

#Виды контроля
control = data['Уровень контроля'].unique()

#Все года
years = data['Год'].unique()

print("В исходном датасете содержалось" , last_row, "оценок, из них ",score, " относятся к группе ПИ101. В датасете находятся оценки" , Number2, 'студентов из них:' ,stud_PI101, 'студенты из группы ПИ101' )
print('со следующими личными номерами:', pi101)
print('Используемые формы контроля:', control)
print('Данные представлены по следующим учебным годам:', years )