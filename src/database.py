import sqlite3


# ---------------------------------------------------
# CREATE DATABASE CONNECTION
# ---------------------------------------------------

conn = sqlite3.connect(
    "resume_matcher.db",
    check_same_thread=False
)

cursor = conn.cursor()


# ---------------------------------------------------
# CREATE TABLE
# ---------------------------------------------------

cursor.execute("""

CREATE TABLE IF NOT EXISTS resumes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    candidate_name TEXT,

    predicted_profile TEXT,

    resume_strength INTEGER,

    final_score REAL

)

""")

conn.commit()


# ---------------------------------------------------
# INSERT RESUME DATA
# ---------------------------------------------------

def save_resume_data(

    candidate_name,
    predicted_profile,
    resume_strength,
    final_score
):

    cursor.execute("""

    INSERT INTO resumes (

        candidate_name,
        predicted_profile,
        resume_strength,
        final_score

    )

    VALUES (?, ?, ?, ?)

    """, (

        candidate_name,
        predicted_profile,
        resume_strength,
        final_score

    ))

    conn.commit()


# ---------------------------------------------------
# FETCH ALL RESUMES
# ---------------------------------------------------

def fetch_all_resumes():

    cursor.execute("""

    SELECT * FROM resumes

    """)

    return cursor.fetchall()