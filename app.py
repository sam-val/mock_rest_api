from api import app, db
from api.models import Human 

@app.shell_context_processor
def make_sh_context():
    return {'db': db, 'Human': Human}

if __name__ == "__main__":
    app.run(debug=True) 



