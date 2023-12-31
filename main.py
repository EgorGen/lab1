import pandas as pd 
# Загрузка данных из файла Excel
data = pd.read_excel("lab_pi_101.xlsx")

# Кол-во оценок
last_row = data.shape[0]

# Кол-во оценок, которые относятся к группе ПИ101
score = data['Группа'].str.contains('ПИ101').sum()

#Кол-во студентов из группы ПИ101
stud_PI101 = len(data[data['Группа'] == 'ПИ101']['Личный номер студента'].unique())

#Личные номера студентов группы ПИ101
pi101 = data.loc[data['Группа']== 'ПИ101' , 'Личный номер студента'].unique()

#Виды контроля
control = data['Уровень контроля'].unique()

#Все года
years = sorted(data['Год'].unique())

print("В исходном датасете содержалось" , last_row, "оценок, из них ",score, " относятся к группе ПИ101.")
print("В датасете находятся оценки" , stud_PI101, 'студентов со следующими личными номерами:', ', '.join(map(str, pi101)))
print('Используемые формы контроля:', ', '.join(map(str, control)))
print('Данные представлены по следующим учебным годам: ', ', '.join(map(str, years)))