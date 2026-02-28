# 🚀 Secure Dockerized Moodle-to-MCP Bridge

A high-performance, local-first **Model Context Protocol (MCP)** server that provides AI-ready access to Moodle LMS data while maintaining strict enterprise security standards.

## 🛡️ "High-Ticket" Security Features
Unlike basic AI integrations, this bridge is built for sensitive educational environments:
- **Least Privilege Access:** Uses a dedicated Read-Only SQL user to prevent any accidental data modification.
- **PII Redaction:** Integrated regex filters automatically scrub student email addresses and sensitive identifiers before they reach the LLM.
- **Containerized Isolation:** Runs within a Docker environment, shielding your primary Moodle infrastructure from the AI runtime.
- **Local-First Architecture:** Processes data within your own VMWare/On-premise infrastructure, ensuring data sovereignty.

## 🏗️ Architecture
The bridge acts as a secure "Private Tunnel" between your LMS and AI agents:
`Moodle DB (MySQL/MariaDB) <-> Read-Only Bridge (Python/FastMCP) <-> Docker Container <-> MCP Client (Claude/Cursor)`

## 🚀 Getting Started

### 1. Database Setup
Create a restricted user in your Moodle database:
```sql
CREATE USER 'moodle_ai_reader'@'localhost' IDENTIFIED BY 'YourSecurePassword';
GRANT SELECT ON moodle.* TO 'moodle_ai_reader'@'localhost';
FLUSH PRIVILEGES;
