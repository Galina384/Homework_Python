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


def test_soft_delete_student(conn):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE student SET deleted_at = NOW() WHERE user_id = 777666"
    )
    cursor.execute("SELECT deleted_at FROM student WHERE user_id = 777666")
    deleted_at = cursor.fetchone()[0]
    assert deleted_at is not None
