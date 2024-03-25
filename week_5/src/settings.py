from pathlib import Path
import pyodbc
import sqlite3
from loguru import logger

class Settings():
    basedir = Path.cwd()
    rawdir = Path("raw_data")
    processeddir = Path("processed_data")
    logdir = basedir / "log"

    # Connectie maken met de SSMS database
    DB = {'servername': 'MSI\SQLEXPRESS',
        'database': 'johari'}

settings = Settings()
logger.add("../logfile.log")