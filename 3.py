class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"User: {self.name}, Email: {self.email}")

class Instructor(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def upload_content(self):
        print(f"Uploading content for subject: {self.subject}")

    def display_info(self):
        print(f"Instructor: {self.name}, Email: {self.email}, Subject: {self.subject}")

class CourseCreator(Instructor):
    def __init__(self, name, email, subject):
        super().__init__(name, email, subject)
        self.courses = []

    def create_course(self, course_name, modules):
        self.courses.append({'name': course_name, 'modules': modules})
        print(f"Course '{course_name}' created with {len(modules)} modules.")

    def display_info(self):
        super().display_info()
        print(f"Courses created: {[course['name'] for course in self.courses]}")

if __name__ == "__main__":
    creator = CourseCreator("Dr. John", "john@example.com", "Data Science")
    creator.upload_content()
    creator.create_course("Machine Learning", ["Intro", "Supervised", "Unsupervised"])
    creator.display_info()
