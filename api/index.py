# api/index.py

import os
import sys

# Ensure the root directory is in sys.path so we can import 'backend'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.main import app

# This exposes 'app' for Vercel serverless ASGI runtime
