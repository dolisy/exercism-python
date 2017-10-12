import collections


class School(object):
  def __init__(self, name):
    self.name = name
    self.students = {}

  def add(self, student, grade):
    # super(School, self).__setattr__(student, grade)
    self.students[student] = grade

  def grade(self, grade):
    grade_students = []

    for student in self.students.keys():
      if self.students[student] == grade:
        grade_students.append(student)

    return grade_students

  def sort(self):
    result = {}

    for i in range(0, 10):
      result[i] = self.grade(i)

    return result



# import operator

# class School(object):
#     def __init__(self, name):
#         self.name = name
#         self.__students = {}

#     def add(self, name, grade):
#         self.__students[name] = grade

#     def grade(self, grade):
#         return [key for key, value in self.__students.iteritems() if value == grade]

#     def sort(self):
#         result = {}
#         for key, value in self.__students.iteritems():
#             if value in result:
#                 result[value] = tuple(sorted(result[value] + (key,)))
#             else:
#                 result[value] = (key,)
#         return sorted(result.items(), key=operator.itemgetter(0))





