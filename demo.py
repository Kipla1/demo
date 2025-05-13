class Student:
    # class scope
    count = 0   #-->number of students(initially)
    total_grade = 0  #-->sum of grades(initially)
    
    #Constructor --> for initialization of our code
    def __init__(self, name, age, grade):
        self._name = name
        self.age = age
        self.grade = grade
        Student.count += 1
        Student.total_grade += grade
        
    #INSTANCE METHOD
    def student_info(self):     #-->This is an instance method
        return f"Hi my name is {self.name} and I am {self.age} years old and i got {self.grade} "  #--> This is an instance Attribute
    
    # CLASS METHOD
    @classmethod
    def get_count(cls):   #-->classmethods take the class itself(cls) as an argument
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average(cls):
        
        return f"Average grade = {(cls.total_grade / cls.count):.1f}"
        
student_1 = Student("James", 30, 90)  
student_2 = Student("Spongebob", 20, 75)      
student_3 = Student("Patrick", 10, 79)      

print(Student.get_count())    #-->To call a  classmethod, append the classmethod(eg get_count() ) to its class(i.e Student)
print(Student.get_average())