from datetime import datetime
import sqlite3

#return doublon en, cas de tentative de créer un doublon
#class doublon(Exception):
#    pass

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_post date,
            statut boolean NOT NULL)""")
        try:
            self.cursor.execute("CREATE UNIQUE INDEX idx_posts_id_date ON posts(date_post)")
        except Exception as e:
            print("index OK " + "\nPartie tech : " + f" {e}")

        # Création de la table "images"
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER,
            chemin TEXT(50),
            FOREIGN KEY(post_id) REFERENCES post(id)
              )''')
        # Création de la table "textes"
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS textes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER,
            contenu TEXT(280),
            FOREIGN KEY(post_id) REFERENCES post(id)
               )''')

    # lecture à la date du jour
    def lecture_post(self, datecherche=datetime.now().strftime("%Y-%m-%d")):
        lecture = """
                    SELECT posts.id, posts.statut, images.chemin, textes.contenu 
                    from "images", "posts", "textes"
                    where posts.id = images.post_id
                    and textes.post_id = posts.id
                    and posts.statut = 0
                    and posts.date_post = ?
                """
        postjour = self.cursor.execute(lecture, (datecherche,)).fetchall()
        # return self.cursor.fetchone(), datecherche
        if not postjour:
            idpost = 0
            poststatut = 0
            lienimage = 0
            texteapublier = "pas texte"
        else:
            idpost = postjour[0][0]
            poststatut = postjour[0][1]
            lienimage = postjour[0][2]
            texteapublier = postjour[0][-1]
        return idpost, poststatut, lienimage, texteapublier, datecherche

    # Insertion d'un nouveau post
    def insert_post(self, chemin, texte, dateinsert=datetime.now().strftime("%Y-%m-%d")):
        """Inserts a post with an image and text into the database.
        Args:
            chemin (str): Path to the image file.
            texte (str): Content of the post.
            dateinsert (str, optional): Date of the post. Defaults to current date.
        Returns:
            int: ID of the inserted post or None on error.

        Raises:
            Exception: If an error occurs during database insertion.
        """
        try:
            post_id = self.execute_insert("INSERT INTO posts (date_post, statut) VALUES (?, 0)", (dateinsert,))
            # Insert image and text only if post insertion was successful
            if post_id:
                self.execute_insert("INSERT INTO images (post_id, chemin) VALUES (?, ?)", (post_id, chemin))
                self.execute_insert("INSERT INTO textes (post_id, contenu) VALUES (?, ?)", (post_id, texte))
                self.conn.commit()
            return post_id
        except Exception as e:
            # Handle the error appropriately, log it, rollback the transaction (if applicable)
            print("Il y a déjà un post à cette date : " + dateinsert + "\nPartie tech : " + f" {e}")
        return None

    # necessaire
    def execute_insert(self, query, params):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor.lastrowid

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetchall(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, post_acquite):
        try:
            self.execute_insert("UPDATE posts SET statut = 1 WHERE id = ?", (post_acquite,))
            # Insert image and text only if post insertion was successful
            self.conn.commit()
            print("MAJ OK pour l'id : " + str(post_acquite))
        except Exception as e:
            # Handle the error appropriately, log it, rollback the transaction (if applicable)
            print("MAJ KO"  + "\nPartie tech : " + f" {e}")
        return None

    def close(self):
        self.conn.close()
