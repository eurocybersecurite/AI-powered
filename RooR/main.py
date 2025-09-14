# main.py
# This file is now only used to run the Flask app
import os
from RooR import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5577))
    app.run(debug=True, host='0.0.0.0', port=port)
