from app import create_app, db
#from app.models import User, Pitch, Comment

app = create_app()

@app.shell_context_processor
def make_shell_context():
    #return {'db': db, 'User': User, 'Blog': Blog, 'Comment': Comment}
    pass

