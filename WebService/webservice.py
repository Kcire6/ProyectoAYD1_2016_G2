__author__ = "G2"
__date__ = "$Ago 9, 2016 11:41:07 PM$"

from flask import Flask, session, request, render_template, jsonify, Response

app = Flask("AYD_PROYECTO")
    
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')