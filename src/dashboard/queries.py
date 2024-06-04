from django.db import connection
from collections import namedtuple

def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def dictfetchone(cursor):
    """
    Return one row from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, cursor.fetchone()))]

def namedtuplefetchall(cursor):
    """
    Return all rows from a cursor as a namedtuple.
    Assume the column names are unique.
    """
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def namedtuplefetchone(cursor):
    """
    Return one row from a cursor as a namedtuple.
    Assume the column names are unique.
    """
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return nt_result(*cursor.fetchone())

# Create
def book_create(title: str, author: str) ->str:
    with connection.cursor as cursor:
        cursor.execute("""INSERT INTO book 
                       (title, author) 
                       VALUES (%s, %s) 
                       RETURNING *;
                       """, [title, author])
        
    return "success"

# Read
def book_read_all():
    with connection.cursor() as cursor:
        cursor.execute("""
                       SELECT id, title, author 
                       FROM book;
                       """,[])
        
        return namedtuplefetchall(cursor)

def book_read_one_id(id: str):
    with connection.cursor() as cursor:
        cursor.execute("""
                       SELECT id, title, author 
                       FROM book 
                       WHERE 
                       id = %s;
                       """, [id])
        
        return namedtuplefetchone(cursor)

# Update
def book_update(title: str, author: str, id: str) ->str:
    with connection.cursor as cursor:
        cursor.execute("""UPDATE book 
                       SET 
                       title = %s, 
                       author = %s
                       WHERE id = %s
                       RETURNING *;
                       """, [title, author, id])
        
    return "success"
    
# Delete
def book_delete(id: str) -> str:
    with connection.cursor as cursor:
        cursor.execute("""DELETE FROM book 
                       WHERE id = %s
                       ;
                       """, [id])
        
    return f"Data with id {id} succesfully deleted"