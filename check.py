# 1) Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.

# У класса должен быть один метод set_deadline, который принимает дату дедлайна (в виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.

# Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, ReadMixin:

# в классе CreateMixin определите метод create, который принимет в себя задачу todo и ключ key по которому нужно добавить задачу в словарь todos, если ключ уже существует верните "Задача под таким ключём уже существует".

# класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key, который передается как аргумент, и возвращает сообщение 'удалили название задачу', где вместо слова название должно быть название задачи.

# класс UpdateMixin должен содержать метод update, который принимает в себя ключ key и новое значение new_value и заменяет задачу под данным ключом на новое значение.

# класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.


class CreateMixin: 
    def create(self, key, todo): 
        if key in self.todos.keys(): 
            return 'Задача под таким ключём уже существует' 
        self.todos[key] = todo 
        return self.todos 
class DeleteMixin: 
    def delete(self, key): 
        delete_ = self.todos.pop(key, 'нет такого ключа') 
        if 'нет такого ключа' == delete_: 
            return delete_ 
        return delete_ 
class UpdateMixin: 
    def update(self, key, new_value): 
        self.todos[key] = new_value 
        return self.todos 
class ReadMixin: 
    def read(self): 
        res = [x for x in self.todos.items()] 
        return sorted(res) 
class ToDo(CreateMixin, 
           DeleteMixin, 
           UpdateMixin, 
           ReadMixin): 
    todos = {} 
    def set_deadline(self, deadline): 
        import datetime 
        time_ = datetime.datetime.now().strftime('%d/%m/%Y') 
        deadline = deadline.split('/')  
        time_ = time_.split('/') 
        deadline = list(map(int, deadline))  
        time_ = list(map(int, time_))  
        time_ = sum((time_[0], time_[1]*30, time_[2]*365)) 
        deadline = datetime.date(deadline[2], deadline[1], deadline[0]) 
        time_ = datetime.date.today() 
        return (deadline - time_).days 
task = ToDo() 
print(task.set_deadline('31/12/2022')) 
print(task.create(1, 'todo')) 
print(task.delete(3)) 
print(task.update(1, 'todo')) 
print(task.read()) 
print(task.create(1, 'Do housework')) 
print(task.create(1, 'Do housework')) 
print(task.create(2, 'Go for a walk')) 
print(task.update(1, 'Do homework')) 
print(task.delete(2)) 
print(task.read()) 
print(task.set_deadline('31/12/2021'))


# 2) Напишите класс Person, который будет хранить информацию о пользователе. У объекта будут следующие защищенные атрибуты экземпляра класса: имя(name), фамилия(last_name), возраст(age), почта (email).
# При инициализации объекта, передавать аргументы классу не нужно, все его атрибуты по умолчанию будут равны None и также все они будут приватными.
# Поэтому реализуйте для каждого атрибута методы доступа get и set с использованием декораторов property и setter. У вас будут такие методы: name (getter, setter), last_name (getter, setter), age (getter, setter) , email (getter, setter)
# Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их как показано ниже и после снова выведите на экран.
# Пример:

# john = Person()
# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# print(john.age) # 30
# print(john.email) # johnsnow@gmail.com

class Person:
    def init(self):
        self._name = None
        self._last_name = None
        self._age = None
        self._email = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

john = Person()

john.name = 'John'
john.last_name = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'

print(john.name)        
print(john.last_name)   
print(john.age)         
print(john.email)

# 3) Создайте классы Dog и Cat с одинаковым методом voice.
# Для собак он должен печатать "Гав", для кошек "Мяу".
# Объявите для каждого из классов по экземпляру, для класса Cat экземпляр в переменной barsik, а для Dog экземпляр rex.
# Затем, вне класса объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice().
# Ввод:
# to_pet(barsik)
# to_pet(rex)
# Вывод:

# Мяу
# Гав 


class Dog:
    def voice(self):
        print("Гав")
class Cat:
    def voice(self):
        print("Мяу")
rex = Dog()
barsik = Cat()
def to_pet(pet):
    pet.voice()
to_pet(barsik)
to_pet(rex)