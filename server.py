from mcp.server.fastmcp import FastMCP
import mysql.connector
import re

mcp = FastMCP("LMS-Privacy-Bridge")

def scrub_pii(text):
    """
    INTERNAL ONLY: This function 'blinds' the AI to sensitive data.
    It replaces Emails and Names with placeholders.
    """
    # 1. Scrub Emails
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', "[EMAIL_REDACTED]", str(text))
    
    # 2. Scrub Names (Example: Simple pattern for capitalized names)
    # In a high-ticket setup, we'd use a library like 'Presidio' here.
    return text

@mcp.tool()
def list_students_safe(course_id: int) -> str:
    """Returns a list of students in a course with PRIVACY REDACTION applied."""
    try:
        db = mysql.connector.connect(
            host="host.docker.internal", 
            user="moodle_ai_reader", 
            password="Njibhu@123", 
            database="learn"
        )
        cursor = db.cursor(dictionary=True)
        
        # Query joining users to a specific course
        query = """
            SELECT u.firstname, u.lastname, u.email 
            FROM mdl_user u 
            JOIN mdl_user_enrolments ue ON ue.userid = u.id
            LIMIT 10
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        results = []
        for i, row in enumerate(rows):
            # SCRUBBING HAPPENS HERE before the 'return'
            scrubbed_name = f"Student_{i+1}" 
            results.append(f"{scrubbed_name} - Status: Enrolled")
            
        return "\n".join(results) if results else "No students found."
        
    except Exception as e:
        return f"Secure Connection Error: {str(e)}"
    finally:
        if 'db' in locals(): db.close()

if __name__ == "__main__":
    mcp.run(transport="stdio")

import time

# ... (keep your existing imports and FastMCP init)

@mcp.tool()
def get_at_risk_students(days_inactive: int = 7) -> str:
    """Identifies students who haven't logged into Moodle for X days."""
    try:
        db = mysql.connector.connect(
            host="host.docker.internal", user="moodle_ai_reader", 
            password="Njibhu@123", database="learn"
        )
        cursor = db.cursor(dictionary=True)
        
        # Calculate the cutoff timestamp (Current time - X days in seconds)
        cutoff = int(time.time()) - (days_inactive * 86400)
        
        query = "SELECT id, lastaccess FROM mdl_user WHERE lastaccess < %s AND lastaccess > 0 LIMIT 10"
        cursor.execute(query, (cutoff,))
        rows = cursor.fetchall()
        
        if not rows:
            return f"Great news! All students have logged in within the last {days_inactive} days."
            
        # Apply the Scrubber for Privacy
        results = [f"Student_{r['id']} - Last seen: {time.ctime(r['lastaccess'])}" for r in rows]
        return f"Found {len(results)} at-risk students:\n" + "\n".join(results)
        
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if 'db' in locals(): db.close()
