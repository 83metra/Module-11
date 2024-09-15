import matplotlib.pyplot as plt
import pandas as pn
from PIL import Image, ImageFilter

# Библиотека matplotlib
production= {'1968': 1, '1969':4, '1970':4, '1971':11, '1972':15, '1973':15, '1974': 37, '1975':43, '1976':57,
                '1977': 61, '1978': 66, '1979': 68, '1980': 74, '1981': 57, '1982': 38, '1983': 23, '1984': 11, '1985': 19,
                '1986': 20, '1987': 17, '1988': 32, '1989': 30, '1990': 36, '1991': 36, '1992': 39, '1993': 34, '1994': 10,
                '1995': 8, '1996': 1, '1997': 3, '1998': 6, '1999': 0, '2000':1, '2001': 2, '2002':0, '2003':1, '2004':0,
                '2005': 2, '2006': 0, '2007': 1, '2008': 1, '2009': 0, '2010': 1, '2011': 0, '2012': 2}

modification = ['Ту-154', 'Ту-154А', 'Ту-154Б', 'Ту-154Б-1', 'Ту-154Б-2', 'Ту-154М']
value_of_planes = [49, 63, 105, 68, 382, 320]
planes, years = [], []
all_planes_int, all_planes = 0, []

for key, value in production.items():
    years.append(int(key))
    planes.append(value)
    all_planes_int += value
    all_planes.append(all_planes_int)

x = years
y = planes



plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Выпуск самолётов Ту-154.')
plt.xlabel('Год')
plt.ylabel('Количество выпущенных самолётов.')
#plt.grid(True)
plt.grid(which='major', color='#DDDDDD', linewidth=0.1)
plt.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.1)
plt.minorticks_on()
plt.savefig('Выпуск Ту-154.jpg', dpi=600)
plt.show()


y1 = planes
y2 = all_planes

plt.plot(x, y1, label='Годовой выпуск Ту-154')
plt.plot(x, y2, label='Парк выпущенных самолётов Ту-154')
plt.title('Выпуск самолётов Ту-154 и общий парк Ту-154.')
plt.grid(True)
plt.grid(which='major', color='#DDDDDD', linewidth=0.1)
plt.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.1)
plt.minorticks_on()
plt.legend()
plt.savefig('Парный график.jpg', dpi=600)
plt.show()


labels = modification
values = value_of_planes
colors = ['yellow','green','red','blue', 'purple', 'brown']
plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
plt.axis('equal')
plt.title('Модификации Ту-154')
plt.savefig('Модификации Ту-154.jpg', dpi=600)
plt.show()


# библиотека pillow
image = Image.open('Выпуск Ту-154.jpg')
image = image.resize((800,600))
image.save('Выпуск Ту-154_resize.jpg')

image = Image.open('Парный график.jpg')
image = image.convert('L')
image.save('Парный график_convert.jpg')

image = Image.open('Модификации Ту-154.jpg')
image = image.filter(ImageFilter.FIND_EDGES)
image.save('Модификации Ту-154_filtered.jpg')

# библиотека pandas
filename ='Предсерийные Ту-154.txt'
try:
    with open(filename, 'r', encoding='utf-8') as file:
       line_list = []
       while True:
           line = file.readline()
           if not line:
               break
           line_list.append(line.split())
except FileNotFoundError:
    print(f'"{filename} не найден."')

# библиотека pandas
column = ['Тип', 'Заводской номер', 'Серийный номер', 'Год выпуска', 'Регистрационный номер', 'Код страны']
table = pn.DataFrame(line_list, columns= column)
print(table)

table.to_csv('Предсерийные Ту-154.csv', index= False)
print(table.head(3))
print(table['Серийный номер'])
print(table[['Тип', 'Заводской номер', 'Регистрационный номер']])


new_string = ['Ту-154', '70M009', '0009', '1972', 'UR-85009', 'su']
table.loc[len(table.index)] = new_string
print('Полный список предсерийных Ту-154.\n %s' %(table))
print((table[table['Год выпуска'].isin(['1972'])])[['Год выпуска', 'Тип', 'Заводской номер', 'Регистрационный номер']])
