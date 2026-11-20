\# Least Privilege Demonstration



A simple Lab Equipment Management System that demonstrates role-based access control.



\## Roles



\- Viewer: Can view equipment records.

\- Admin: Can view and add equipment records.



\## Demo accounts



\- Viewer: `viewer` / `view123`

\- Admin: `admin` / `admin123`



\## Run the project



1\. Activate the virtual environment:

&#x20;  ` .venv\\Scripts\\activate `

2\. Install Flask:

&#x20;  `py -m pip install flask`

3\. Start the app:

&#x20;  `py app.py`

4\. Open http://127.0.0.1:5000 in a browser.



\## Permission test



A viewer's direct request to add equipment is rejected by the server with HTTP 403 Forbidden.

