from flask import Flask, request, redirect, session, url_for, render_template_string

app = Flask(__name__)
app.secret_key = "change-this-demo-key"

users = {
    "viewer": {"password": "view123", "role": "viewer"},
    "admin": {"password": "admin123", "role": "admin"},
}

equipment = [
    {"id": 1, "name": "Microscope", "location": "Lab 1"},
    {"id": 2, "name": "Projector", "location": "Room 2"},
]

PAGE = """
<h1>Lab Equipment System</h1>
{% if user %}
  <p>Logged in as <b>{{ user }}</b> ({{ role }})</p>
  <a href="/logout">Logout</a>
  <h2>Equipment</h2>
  <ul>
  {% for item in equipment %}
    <li>{{ item.name }} — {{ item.location }}</li>
  {% endfor %}
  </ul>
  {% if role == "admin" %}
    <h2>Add equipment</h2>
    <form method="post" action="/add">
      <input name="name" placeholder="Equipment name" required>
      <input name="location" placeholder="Location" required>
      <button type="submit">Add</button>
    </form>
  {% endif %}
{% else %}
  <p>Demo accounts: viewer / view123 and admin / admin123</p>
  <form method="post">
    <input name="username" placeholder="Username" required>
    <input name="password" type="password" placeholder="Password" required>
    <button type="submit">Login</button>
  </form>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        account = users.get(username)
        if account and account["password"] == password:
            session["username"] = username
            return redirect(url_for("home"))
        return "Login failed. Go back and try again.", 401

    username = session.get("username")
    role = users.get(username, {}).get("role")
    return render_template_string(
        PAGE, user=username, role=role, equipment=equipment
    )

@app.route("/add", methods=["POST"])
def add_equipment():
    username = session.get("username")
    role = users.get(username, {}).get("role")

    # Server-side authorization check: only admins can add equipment.
    if role != "admin":
        return "Access denied: admin permission required.", 403

    name = request.form.get("name", "").strip()
    location = request.form.get("location", "").strip()
    if name and location:
        new_id = max(item["id"] for item in equipment) + 1
        equipment.append({"id": new_id, "name": name, "location": location})
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)