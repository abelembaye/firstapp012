from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Azure App Service!"

if __name__ == '__main__':
    app.run()



#This file uses the virt env at
# conda deactivate
# ../venv4pdfgen/Scripts/activate.ps1
# streamlit run ./main.py
