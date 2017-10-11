class Garden(object):
    def __init__(self, diagram, students="Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()):
      self.diagram = diagram.split()
      self.students = sorted(students)

    def plants(self, student):
      plants = {
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets'
      }
      student_index = self.students.index(student)
      student_plants = ''
      for row in self.diagram:
        student_plants += row[student_index*2:student_index*2+2]
      return [plants[letter] for letter in list(student_plants)]
