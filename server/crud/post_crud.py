from flask import jsonify, redirect
from models import db, Post, User

def error(err_locale, error):
    print("ERROR in", err_locale, ":", error)
    return jsonify(error=f'Server Error in {err_locale}', message=f'Server Error in {err_locale}')


# gets all posts
def get_all_posts():
    try:
        all_posts = Post.query.filter_by(public=True).all()
        results = [post.as_dict() for post in all_posts]
        return jsonify(results=results)
    except Exception as error:
        return error('getting all posts', error)

# gets a user's posts
def get_user_posts(user_id):
    try:
        posts = Post.query.filter_by(user_id=user_id).all()
        if posts: 
            print("GOT USER POSTS ")
            results = [post.as_dict() for post in posts]
            return jsonify(results=results)
        else: 
            return jsonify(error=f"couldn't find posts for user id {id}")
    except Exception as error:
        return error('getting posts for user', error)


def create_post(title, date, user_id):
    try: 
        print("CREATING A POST")
        new_post = Post(title=title, data=date, user_id=user_id)
        print("ADDING A POST")
        db.session.add(new_post)
        print("SENDING DAT POST")
        db.session.commit()
        return jsonify(results=new_post.as_dict())
    except Exception as error:
        return error('creating a post')

def update_post(id, title, date):
    try: 
        post = Post.query.get(id)
        if post:
            post.title = title or post.title
            post.public = public or post.public
            db.session.commit()
            return jsonify(result=post.as_dict())
        else:
            return jsonify("No post found at id", id)
    except Exception as error:
        return error('updating a user', error)

def destroy_post(id):
    try: 
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return jsonify(result="success")
    except Exception as error:
        return error('deleting a user', error)


            