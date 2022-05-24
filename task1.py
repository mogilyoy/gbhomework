# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

import time

class TrafficLight:
    __color = 'red'
    def running(self):
        TrafficLight.__color = 'red'
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = 'yellow'
        print(TrafficLight.__color)
        time.sleep(2)
        TrafficLight.__color = 'green'
        print(TrafficLight.__color)
        time.sleep(10)

a = TrafficLight()
for i in range(1, 4):
    a.running()



