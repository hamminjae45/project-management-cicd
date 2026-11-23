from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

projects = [
    {"id": 1, "name": "CI/CD 프로젝트", "description": "자동 배포 시스템 구축", "status": "진행 중"},
    {"id": 2, "name": "웹 서비스 개발", "description": "Flask 웹 서비스 개발", "status": "대기"}
]

@app.route("/")
def index():
    return render_template("index.html", projects=projects)

@app.route("/add", methods=["POST"])
def add_project():
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()

    if name:
        new_id = max([p["id"] for p in projects], default=0) + 1
        projects.append({
            "id": new_id,
            "name": name,
            "description": description,
            "status": "대기"
        })

    return redirect(url_for("index"))

@app.route("/edit/<int:project_id>", methods=["POST"])
def edit_project(project_id):
    for project in projects:
        if project["id"] == project_id:
            project["status"] = request.form.get("status", project["status"])
            break

    return redirect(url_for("index"))

@app.route("/delete/<int:project_id>", methods=["POST"])
def delete_project(project_id):
    projects[:] = [p for p in projects if p["id"] != project_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
