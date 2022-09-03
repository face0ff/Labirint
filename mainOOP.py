import json

class Gamer:
    def __init__(self, name):
        self.name = name
    def correct(self):
        print("%s нашел правильный путь." % (self.name))
    def ran(self):
        print("%s струсил и убежал, игра закончена." % (self.name))
    def dead(self):
        print("%s заблудился, игра закончена." % (self.name))

class Question:
    def choice(self, count):
        try:
            answer = int(input(f"{count} Куда пойдем ??? 0-это влево, 1-это вверх, 2-это вправо, 3-это вниз. Ваш выбор = "))
            if answer in range(0, 4):
                return answer
            else:
                print("Вы не верно ввели данные")
        except ValueError:
            print("Вы не верно ввели данные")

class Maze:
    def __init__(self, forward, back):
        self.forward = forward
        self.back = back

    def check(self, count):
        for i in range((count-1), len(forward)):
            returnChoice = Question.choice(Question, count)
            if returnChoice == forward[i]:
                player.correct()
                count+=1
            elif returnChoice == back[i]:
                xod = {"xod": count}
                save.update(xod)
                player.ran()
                break
            else:
                xod = {"xod": count}
                save.update(xod)
                player.dead()
                break
        if count > len(forward):
            save["xod"] = 1
            print("Поздравляем с победой")

class OpenSave:

    def run(self, count, save):
        with open('save.json') as p:
            save = json.load(p)
        if save["xod"] == 1:
            maze.check(count)
        else:
            try:
                startWithSave = int(input("Начнем оттуда где закончили? 0-это да. 1-это нет "))
                if int(startWithSave) == 1:
                    save["xod"] = 1
                    maze.check(count)
                elif startWithSave == 0:
                    count = save["xod"]
                    maze.check(count)
                else:
                    print("Вы не верно ввели данные, начинаем с начала")
                    save["xod"] = 1
                    maze.check(count)
            except ValueError:
                print("Вы не верно ввели данные, начинаем с начала")
                save["xod"] = 1
                maze.check(count)

    def save(self,save):
        with open('save.json', 'w', encoding='utf-8') as json_file:
            json.dump(save, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":

    forward = [2, 2, 3, 0, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 0, 3, 3, 0, 3, 2, 3, 2, 2]
    back = [0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 2, 1, 1, 2, 1, 0, 1, 0]
    count = 1
    save = {"xod": count}
    maze = Maze(forward, back)
    name = input("Назовите имя ")
    player = Gamer(name)
    openSave = OpenSave()
    openSave.run(count, save)
    openSave.save(save)