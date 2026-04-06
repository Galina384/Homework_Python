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


def test_update_student(conn):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (%s, %s, %s, %s)
    """, (777666, 'Elementary', 'group', 888))

    print("📝 Создан студент с user_id=777666, форма 'group'")

    cursor.execute("""
        UPDATE student
        SET education_form = %s
        WHERE user_id = %s
    """, ('personal', 777666))

    cursor.execute("""
        SELECT education_form FROM student WHERE user_id = %s
    """, (777666,))

    new_form = cursor.fetchone()[0]

    assert new_form == 'personal'
    print(f"Форма изменена: group -> {new_form}")
