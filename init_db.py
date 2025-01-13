from ext import app, db
from models import Product, User


with app.app_context():

    db.drop_all()
    db.create_all()

    admin_user = User(
       username="admin",
       password="adminpass",
       email="lelele_lelele@gmail.com",
       role="Admin",
       name="admin",
       number="123",
       img="https://i.seadn.io/gae/jCQAQBNKmnS_AZ_2jTqBgBLIVYaRFxLX6COWo-HCHrYJ1cg04oBgDfHvOmpqsWbmUaSfBDHIdrwKtGnte3Ph_VwQPJYJ6VFtAf5B?auto=format&dpr=1&w=1000"
    )

    admin_user.create()


