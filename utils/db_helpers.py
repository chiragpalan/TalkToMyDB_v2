import sqlite3
import pandas as pd
from utils.groq_helpers import nl_to_sql

DB_PATH = "data/sakila.db"

def get_connection():
    """Establish a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)

def run_sql(sql: str) -> pd.DataFrame:
    """Execute a SQL query and return the results as a DataFrame."""
    with get_connection() as conn:
        return pd.read_sql_query(sql, conn)

def ask_question(question: str):
    """Convert a natural language question to SQL, execute it, and return results."""
    sql = nl_to_sql(question)
    df = run_sql(sql)
    return {"sql": sql, "df": df}
