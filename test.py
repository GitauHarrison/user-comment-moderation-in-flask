from app import app, db
from app.models import UserComment, Admin


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, UserComment=UserComment, Admin=Admin)
