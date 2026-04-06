import psycopg2
import pytest


@pytest.fixture
def conn():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="QA",
        user="postgres",
        password="123"
    )
    connection.autocommit = False
    yield connection
    connection.rollback()
    connection.close()


def test_add_student(conn):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (%s, %s, %s, %s)
    """, (999888, 'Beginner', 'group', 777))

    cursor.execute("""
        SELECT * FROM student WHERE user_id = %s
    """, (999888,))

    result = cursor.fetchone()

    assert result is not None
    print("Студент с user_id=999888 добавлен!")
