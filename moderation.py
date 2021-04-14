from app import app
from app.models import Admin, Comment


@app.shell_context_processor
def make_shell_context():
    return {'Admin': Admin, 'Comment': Comment}
