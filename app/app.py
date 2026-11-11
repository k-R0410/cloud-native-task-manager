from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory task storage
tasks = []
next_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to DevOps Task Manager!",
        "status": "running",
        "version": "v2",
        "deployment": "Kubernetes Rolling Update"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


@app.route("/api/tasks", methods=["POST"])
def create_task():
    global next_id

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON object required"}), 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Valid task title required"}), 400

    task = {
        "id": next_id,
        "title": title.strip(),
        "completed": False
    }

    tasks.append(task)
    next_id += 1

    return jsonify(task), 201


@app.route("/api/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON object required"}), 400

    for task in tasks:
        if task["id"] == task_id:
            if "completed" in data:
                if not isinstance(data["completed"], bool):
                    return jsonify({
                        "error": "completed must be true or false"
                    }), 400

                task["completed"] = data["completed"]

            return jsonify(task), 200

    return jsonify({"error": "Task not found"}), 404


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"}), 200

    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
