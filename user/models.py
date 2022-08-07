from flask import Flask, jsonify , request
from passlib.hash import pbkdf2_sha256
import uuid
from app import db

class User:
    def signup(self):
        user = {
            "_id" : uuid.uuid4().hex,
            "name":request.form.get('name'),
            "email" :request.form.get('email'),
            "password":request.form.get('password')
        }

        # Encrypt password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        if db.users.find_one({"email":user['email']}):
            print("error===========")
            return jsonify({"error": "Email address already exist"}),400
        
        if db.users.insert_one(user):
            jsonify(user),200
        
        return jsonify({"error": "Signup Failed"}),400 