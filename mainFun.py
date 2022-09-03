import json

pravelniyOtvet = [2,2,3,0,3,2,2,2,2,3,3,2,2,2,2,3,0,3,3,0,3,2,3,2,2]
nazadOtvet =     [0,0,0,1,2,1,0,0,0,0,1,1,0,0,0,0,1,2,1,1,2,1,0,1,0]
count = 1
save = {"xod": count}


def vopros():
    otvet = int(input(f"Ход- {count}>>Куда пойдем ??? 0-это влево, 1-это вверх, 2-это вправо, 3-это вниз. Ваш выбор = "))
    return otvet


def proverkaOtveta():
    global count
    for i in range((count-1),len(pravelniyOtvet)):
        returnOtvet = vopros()
        if returnOtvet == pravelniyOtvet[i]:
            print("Шарик нашел правильный путь")
            count += 1
        elif returnOtvet == nazadOtvet[i]:
            print("Шарик струсил и убежал, игра закончена.")
            xod = {"xod": count}
            save.update(xod)
            break
        else:
            print("Щарик заблудился, игра закончена")
            xod = {"xod": count}
            save.update(xod)
            break
    if count > len(pravelniyOtvet):
        print("Поздравляем с победой")
with open('save.json') as p:
    save = json.load(p)

if save["xod"] == 1:
    proverkaOtveta()
else:
    startWithSave = int(input("Начнем оттуда где закончили? 0-это да. 1-это нет"))
    if startWithSave == 1:
        proverkaOtveta()
        save["xod"] = 1

    elif startWithSave == 0:
        count = save["xod"]
        proverkaOtveta()

with open('save.json', 'w', encoding='utf-8') as json_file:
    json.dump(save, json_file, indent=4, ensure_ascii=False)



