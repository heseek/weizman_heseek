import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

font_list = fm.findSystemFonts()
path = font_list[font_list.index('C:\Windows\Fonts\malgun.ttf')]
font_name = fm.FontProperties(fname=path, size=18).get_name()
plt.rc('font', family=font_name)

pets = ['개', '뱀', '괴물', '물고기', '햄스터', '고양이', '도마뱀', '와! 샌즈', '마크 드래곤`s', ]
students = [56, 23, 1, 19, 25, 52, 31, 100, 55, ]
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'orange', 'black', 'gold', 'green', ]

plt.bar(pets, students, color=colors)

plt.xlabel('애완동물')
plt.ylabel('숫자')
plt.title('사람들이 키우는 애완동물 수')
plt.show()

countries = ['USA', 'GBR', 'China', 'Russia', 'Germany']
gold = [34, 53, 24, 54, 24]
colors = ['red', 'green', 'blue', 'yellow', 'cyan']
