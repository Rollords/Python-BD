from flask import Flask, render_template
from conex import conectar_bd
import mysql.connector

app = Flask(__name__)

