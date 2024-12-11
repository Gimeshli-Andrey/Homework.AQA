import logging
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    courses = relationship('Course', secondary='student_courses', back_populates='students')

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, age={self.age})"

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    students = relationship('Student', secondary='student_courses', back_populates='courses')

    def __repr__(self):
        return f"Course(id={self.id}, name={self.name})"

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)