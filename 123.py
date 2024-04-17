
class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    credit_hour = models.IntegerField()
    pre_req = models.CharField(max_length=255, blank=True, null=True)
    course_type = models.CharField(max_length=255)
    credits = models.IntegerField()

class Instructor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    instructor_pay = models.DecimalField(max_digits=10, decimal_places=2)

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    service_date = models.DateField()

class Campus(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

class Chatbot(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    query = models.TextField()
    response = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

# Additional models for relationships
class StudentEnrolledInCourse(models.Model):
    grade = models.CharField(max_length=2)
    marks = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class CoursesOfferedByStudent(models.Model):
    credit_hour = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)

class CoursesTaughtByInstructor(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class ServicesUsedByStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    complain = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)

class StudentInSemester(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)

class Semester(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    student = models.ManyToManyField(Student, through=StudentInSemester)
    course = models.ManyToManyField(Course, through=CoursesOfferedByStudent)
