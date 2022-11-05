from app import db

class data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)                                                #id is an int datatype and a primary-key
    title = db.Column(db.String(500), index=True, unique=True)                                  #title is string datatype has a upper-limit of 500 and it does not share this key value with other tuples 
    module_code = db.Column(db.String(), index = True, unique = True)                           #module code is also mean't to be unique like title
    deadline = db.Column(db.Date())                                                             #deadline is a Date field
    description = db.Column(db.String)                                                          #description is the String field
    status = db.Column(db.String)                                                               #status is also the String field

    def __init__(self, title, module_code, deadline, description, status):                      #Constructor to the database model
        self.title = title                                                                      #title = title
        self.module_code = module_code                                                          #module_code = module_code
        self.deadline = deadline                                                                #deadline = deadline
        self.description = description                                                          #description = description
        self.status = status                                                                    #status = status
