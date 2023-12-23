from main import app, db
app.app_context().push()
db.create_all()

try:
    a = 0
    b = 2
    print(b/a)
except ex:
    print('что-то пошло не так', ex)