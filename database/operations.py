from database.db import get_connection

# save the project

def save_project(
    project_name,
    requirement
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO projects(
            project_name,
            requirement
        )
        VALUES (?,?)
        """,
        (
            project_name,
            requirement
        )
    )

    conn.commit()

    project_id = cursor.lastrowid

    conn.close()

    return project_id

# save document

def save_document(
    project_id,
    document_type,
    content
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO documents(
            project_id,
            document_type,
            content
        )
        VALUES (?,?,?)
        """,
        (
            project_id,
            document_type,
            content
        )
    )

    conn.commit()

    conn.close()

# save review

def save_review(
    project_id,
    review
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reviews(
            project_id,
            review_report
        )
        VALUES (?,?)
        """,
        (
            project_id,
            review
        )
    )

    conn.commit()

    conn.close()



# get projects

def get_projects():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM projects"
    )

    data = cursor.fetchall()

    conn.close()

    return data

# get project details

def get_project_by_id(project_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM projects WHERE id=?",
        (project_id,)
    )

    project = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM documents WHERE project_id=?",
        (project_id,)
    )

    documents = cursor.fetchall()

    cursor.execute(
        "SELECT * FROM reviews WHERE project_id=?",
        (project_id,)
    )

    review = cursor.fetchone()

    conn.close()

    return {
        "project": project,
        "documents": documents,
        "review": review
    }