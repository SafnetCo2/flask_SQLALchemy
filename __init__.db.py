from datetime import date
from app import db, Employee

db.drop_all()
db.create_all()

el=Employee(firstname='Jose',
            lastname='Doe',
            email='jd@example.com',
            age=32,
            hire_date=date(2012,3,3),
            active=True
            
            )
el1=Employee(firstname='ose',
            lastname='Toe',
            email='gd@example.com',
            age=45,
            hire_date=date(2012,3,3),
            active=True
            
            )
el2=Employee(firstname='Jose',
            lastname='yoe',
            email='hd@example.com',
            age=32,
            hire_date=date(2012,3,3),
            active=True
            
            )
el3=Employee(firstname='Jos',
            lastname='ooe',
            email='yd@example.com',
            age=32,
            hire_date=date(2012,3,3),
            active=True
            
            )
db.session.add_all([el1,el2,el3])
db.session.commit()