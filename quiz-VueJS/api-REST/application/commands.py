from .app import app, db

#command line interface
@app.cli.command()
def syncdb():
    """create missing tables"""
    db.create_all()
    
