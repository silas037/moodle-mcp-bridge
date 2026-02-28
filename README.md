<<<<<<< HEAD
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
=======
# 🎓 Moodle-to-MCP Secure Bridge
**Enterprise-Grade Agentic AI Infrastructure for Education**

This project provides a secure, Dockerized **Model Context Protocol (MCP)** server that bridges Claude AI to a private Moodle LMS database. It enables AI agents to perform administrative tasks and student analytics while maintaining 100% data privacy.

## 🛡️ Key Features
- **Zero-Knowledge Privacy:** Built-in **PII Scrubber** layer that redacts student names/emails locally before data reaches the cloud.
- **Agentic Analytics:** Proactive tools for identifying at-risk students and monitoring platform engagement.
- **Secure Architecture:** Uses **SSH Tunneling** and restricted **Read-Only SQL** permissions to protect the core LMS.
- **Containerized Deployment:** Fully Dockerized for portable, isolated, and conflict-free installation.

## 🛠️ Tech Stack
- **Protocol:** Model Context Protocol (MCP)
- **Language:** Python 3.11 (FastMCP)
- **Containerization:** Docker
- **Database:** MySQL / MariaDB (Moodle Core)
- **Infrastructure:** VMWare & macOS Orchestration

## 🚀 Available Tools
1. `list_courses`: Summarizes all active courses in the database.
2. `list_students_safe`: Fetches student lists with automated identity redaction.
3. `get_recent_active_users`: Tracks platform-wide engagement and recent login activity.

## 📦 Getting Started
### 1. Build the Container
```bash
docker build -t moodle-mcp-bridge .
>>>>>>> b976085 (chore: prepare for sync)
