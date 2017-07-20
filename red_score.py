# -*- coding: utf-8 -*-
#不及格变红
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]#判断是否为字符串

print toUppers(['Hello', 'world', 101])

print [100 * n1 + 10 * n2 + n3 for n1 in range(1, 10) for n2 in range(10) for n3 in range(10) if n1==n3]

#map函数
def format_name(s):
    return s[0].upper()+s[1:].lower()

print map(format_name, ['adam', 'LISA', 'barT'])

#reduce函数
def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])
#filter函数
import math
def is_sqr(x):
    r = int(math.sqrt(x))
    return r*r==x
print filter(is_sqr, range(1, 101))
#sort函数 排序
def cmp_ignore_case(s1, s2):
    if s1.lower()>s2.lower():
        return 1
    if s1.lower()<s2.lower():
        return -1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

import time

#装饰器
import time, functools
def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial.__name__
#判断类型
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')

print isinstance(t, Person)
print isinstance(t, Student)
print isinstance(t, Teacher)
print isinstance(t, object)

#json.load
import json

class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'

s = Students()

print json.load(s)

#设置对象属性
class Person(object):
    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.iteritems():
            setattr(self, k, v)

p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course

#如果要把一个类的实例变成 str
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)
    __repr__ = __str__

s = Student('Bob', 'male', 88)
print s
#计算
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)
    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)
    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2

#property

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
    @property
    def grade(self):
        if self.score < 60:
            return 'C'
        if self.score < 80:
            return 'B'
        return 'A'
s = Student('Bob', 59)
print s.grade
s.score = 60
print s.grade
s.score = 99
print s.grade



