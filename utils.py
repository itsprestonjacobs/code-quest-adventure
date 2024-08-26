# utils.py

def run_code(code):
    """Executes the provided code and returns the result or error message."""
    local_vars = {}
    try:
        exec(code, globals(), local_vars)
        return "Code executed successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

