#############################################################################
#                                 PACKAGES                                  #
#############################################################################


# SQL packages
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Unicode, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Additional packages
import logging

# Project packages
from sqlalchemy.ext.declarative import declarative_base


#############################################################################
#                              FUNCTIONS                                    #
#############################################################################

Base = declarative_base()

class User(Base):

    __tablename__ = 'User'

    ID = Column(Integer, primary_key=True)
    Username = Column("Username", Unicode)
    Name = Column("Name", Unicode)
    Password = Column("Password", Unicode)

    # --------------------------------------------- #

class Question(Base):

    __tablename__ = 'Question'

    ID = Column(Integer, primary_key=True)
    Title = Column("Title", Unicode)
    Question = Column("Question", Unicode)
    Date = Column("Date", Date)
    User_ID = Column("User_ID", Unicode, ForeignKey("User.ID"))

    # --------------------------------------------- #

class Q_A(Base):

    __tablename__ = 'Q_A'

    ID = Column(Integer, primary_key=True)
    Question_ID = Column("Question_ID", Unicode, ForeignKey(Question.ID))
    Answer_ID = Column("Answer_ID", Unicode, ForeignKey("Answer.ID"))

    # --------------------------------------------- #

class Answer(Base):

    __tablename__ = 'Answer'

    ID = Column(Integer, primary_key=True)
    Answer = Column("Answer", Unicode)
    Vote = Column("Vote", Integer)
    Date = Column("Date", Date)
    User_ID = Column("User_ID", Unicode, ForeignKey("User.ID"))

    # --------------------------------------------- #

class User_Obj(object):

    def __init__(self, ID, Username, Name, Password):

        # call the constructor of the super classes
        super().__init__()
        self.ID = ID 
        self.Username = Username
        self.Name = Name
        self.Password = Password

#############################################################################
#                                  MAIN                                     #
#############################################################################

#############################################################################

if __name__ == "__main__":
    sys.exit()
    
    #engine = create_engine("sqlite:///database.db")
    #Base.metadata.create_all(engine)
