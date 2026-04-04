import pytest
import sqlite3
import os

def test_db_initialization_and_connection(tmp_path, monkeypatch):
    # Use a temporary database for testing to avoid touching production DB
    db_file = tmp_path / "test_fitness.db"
    
    # We must patch the environment before importing if we can, or just patch the variables inside the module
    import database
    monkeypatch.setattr(database, "DB_NAME", str(db_file))
    
    # Test initialization
    database.init_db()
    assert os.path.exists(str(db_file))
    
    # Test connection
    conn = database.get_db_connection()
    assert isinstance(conn, sqlite3.Connection)
    
    # Check if a critical table like 'users' exists
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    assert cur.fetchone() is not None
    
    # Check if default admin user was created
    cur.execute("SELECT username FROM users WHERE username='admin'")
    assert cur.fetchone() is not None
    
    conn.close()
