# Vercel serverless function entry point
import sys
import os
from pathlib import Path

# Ensure project root is in Python path so 'app' package is importable.
# In Vercel's serverless environment, the project root is the function's
# parent directory (one level up from api/).
_project_root = str(Path(__file__).resolve().parent.parent)
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

# Also add to PYTHONPATH for any subprocess calls
os.environ.setdefault("PYTHONPATH", _project_root)

from app.main import app  # noqa: E402

# Vercel's @vercel/python runtime detects and uses the 'app' ASGI variable.
# The variable named 'app' is exported from the import above.
