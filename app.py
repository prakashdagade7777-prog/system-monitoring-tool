from flask import Flask, render_template
import psutil

app = Flask(__name__)

LOG_FILE = "logs.txt"

def log_data(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def get_data():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    status = f"CPU:{cpu}% Memory:{memory}% Disk:{disk}%"
    log_data(status)

    return {
        "cpu": cpu,
        "memory": memory,
        "disk": disk
    }

@app.route("/")
def home():
    data = get_data()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
