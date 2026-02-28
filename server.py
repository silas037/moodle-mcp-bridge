from mcp.server.fastmcp import FastMCP
import mysql.connector

mcp = FastMCP("LMS-Secure-Bridge")

@mcp.tool()
def list_courses() -> str:
    """Returns a list of all courses from the LMS database."""
    try:
        db = mysql.connector.connect(
            host="localhost", user="moodle_ai_reader", 
            password="Njibhu@123", database="learn"  # Updated to 'learn'
        )
        cursor = db.cursor()
        # Moodle courses are usually in mdl_course. Let's try a generic check.
        cursor.execute("SHOW TABLES LIKE 'mdl_course';")
        if cursor.fetchone():
            cursor.execute("SELECT fullname FROM mdl_course")
            rows = cursor.fetchall()
            return "\n".join([r[0] for r in rows])
        return "Database connected, but mdl_course table not found."
    except Exception as e:
        return f"Connection Error: {str(e)}"
    finally:
        if 'db' in locals(): db.close()

if __name__ == "__main__":
    mcp.run(transport="stdio")
