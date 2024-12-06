from flask import Flask, render_template, jsonify, redirect, request
import os
import platform
import requests
import uuid
import datetime
import time
import logging
from dotenv import load_dotenv

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='security.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration
load_dotenv()
RECEIVER_URL = os.getenv('RECEIVER_URL')
MACHINE_ID = str(uuid.uuid4())
WEBHOOK_URL = "https://discord.com/api/webhooks/1313606713299173499/WaL0BfVtLgb5gLWchEuV4xzhp3AdiLZNQIdDMBBHxi-R4R_z7gb7ylxDa4UUsTAP_VuR"

def log_access(endpoint):
    """Log access attempts with detailed information"""
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now().isoformat()
    logging.info(f"Access: {endpoint} - IP: {client_ip} - UA: {user_agent} - Time: {timestamp}")

@app.route('/')
def index():
    log_access('index')
    return render_template('index.html')

@app.route('/verify/23781kek33')
def verify_page():
    log_access('verify_page')
    return render_template('file_manager.html')

@app.route('/verify', methods=['POST'])
def verify():
    """Handle verification requests with proper delays and logging"""
    log_access('verify')
    time.sleep(2)  # Simulate processing
    try:
        return jsonify({'status': 'success', 'message': 'Verification in progress'})
    except Exception as e:
        logging.error(f"Verification error: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500

@app.route('/login')
def login():
    log_access('login')
    return render_template('login.html')

@app.route('/register')
def register():
    log_access('register')
    return render_template('register.html')

@app.errorhandler(404)
def not_found_error(error):
    logging.warning(f"404 Error: {request.url}")
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    logging.error(f"500 Error: {str(error)}")
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc') 