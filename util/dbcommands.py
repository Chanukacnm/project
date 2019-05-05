import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def add_user(username, password_hash):
    doc_ref = db.collection(u'db')

    doc_ref.add({
        u'id': 1,
        u'username': username,
        u'password_hash': password_hash

    })
def add_read(userID,ID):
    doc_ref = db.collection(u'readOrWatched')

    doc_ref.add({
        u'userID':userID,
        u'ID' :ID,
        u'type': "book"
    })

def add_watched(userID,ID):
    doc_ref = db.collection(u'readOrWatched')

    doc_ref.add({
        u'userID':userID,
        u'ID' :ID,
        u'type': "movie"
    })

def add_wishlist_book(userID,ID):
    doc_ref = db.collection(u'wishlist')

    doc_ref.add({
        u'userID': userID,
        u'ID': ID,
        u'type': "book"
    })

def add_wishlist_movie(userID,ID):
    doc_ref = db.collection(u'wishlist')

    doc_ref.add({
        u'userID': userID,
        u'ID': ID,
        u'type': "movie"
    })

def get_books_read(userID):
    cities_ref = db.collection(u'readOrWatched')
    query_ref = cities_ref.where(u'Id', u'==', userID)
    result = query_ref.get()
    books = []
    for a in result:
        books.append(a.to_dict)
    return books
def remove_book_read(userID, ID):
    cities_ref = db.collection(u'readOrWatched')
    query_ref = cities_ref.where(u'userID', u'==', userID).where(u'ID', u'==', ID).where(u'type', u"==", "book")
    result = query_ref.get()
    book=""
    for a in result:
        book=a.to_dict()
    return book

def get_user_id(username):
    cities_ref = db.collection(u'db')
    query_ref = cities_ref.where(u'username', u'==', username)
    result = query_ref.get()
    userID=""
    for a in result:
        userID=a.to_dict["id"]
    return userID

def get_username(id):
    cities_ref = db.collection(u'db')
    query_ref = cities_ref.where(u'id', u'==', id)
    result = query_ref.get()
    username = ""
    for a in result:
        username = a.to_dict["username"]
    return username


def get_all_user_data():
    docs = db.collection(u'db').get()
    usernames = []
    users = []

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
        a = doc.to_dict()
        usernames.append(a["username"])
        users.append(a.to_dict)
    return users


def removeUser(id):
    cities_ref = db.collection(u'db')
    query_ref = cities_ref.where(u'id', u'==', id)

    resut = query_ref.get()
    newid = ""

    for a in resut:
        print(u'{} => {}'.format(a.id, a.to_dict()))
        newid = a.id


    db.collection(u'db').document(newid).delete()





add_watched("1223","12")
#removeUser(1)





