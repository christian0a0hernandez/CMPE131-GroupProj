from website import create_app, db


app = create_app()

@app.before_first_request # fixes SQL error
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True) # updates website as code is changed

