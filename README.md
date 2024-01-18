# GraphQL with PostgreSQL Tutorial

## Introduction
This tutorial demonstrates how to integrate GraphQL with a PostgreSQL database using Python. The project involves setting up a database schema with SQLAlchemy, adding and fetching data, and potentially linking this with a GraphQL schema.

## Project Structure
This project consists of three main files:
- `dbsetup.py`: Contains the database schema and the database creation script.
- `addEntries.py`: Used for adding entries to the database and fetching data.
- `gqlSchema.py`: Intended for setting up a GraphQL schema (note: implementation details to be added).

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- PostgreSQL
- SQLAlchemy
- [Any additional dependencies]

## Setup
### Database Configuration
1. Install PostgreSQL and set up a database named `postgres`.
2. Update the database URI in `dbsetup.py`, `addEntries.py`, and `gqlSchema.py` with your PostgreSQL credentials.