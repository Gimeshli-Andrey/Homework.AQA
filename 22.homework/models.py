import os
from sqlalchemy import Column, Integer, String, Table, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase
from sqlalchemy.orm import declarative_base
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

Base = declarative_base()

student_course_association = Table(
    'student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    email = Column(String(100), unique=True)

    courses = relationship(
        "Course",
        secondary=student_course_association,
        back_populates="students"
    )

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"


class Course(Base):
    """Модель курсу"""
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))

    students = relationship(
        "Student",
        secondary=student_course_association,
        back_populates="courses"
    )

    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}')>"


def get_db_connection(db_url):
    try:
        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)
        return Session(), engine
    except Exception as e:
        logger.error(f"Помилка підключення до бази даних: {e}")
        raise