from flask_app.config.mysqlconnection import connectToMySQL

class writing:
    def __init__( self, data ):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.content = data['content']

    @classmethod
    def save( cls, data ):
        query_string = "INSERT INTO writings ( title, description, writing ) \
            VALUES (%(title)s, %(description)s, %(content)s);"
        return connectToMySQL().query_db(query_string, data)