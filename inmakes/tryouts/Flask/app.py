from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (you can replace this with a database)
tasks = {
    1: {'title': 'Task 1', 'description': 'Do something'},
    2: {'title': 'Task 2', 'description': 'Read a book'},
}


# Get all tasks
@app.route('/api/tasks/', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


# Create a new task
@app.route('/api/tasks/', methods=['POST'])
def create_task():
    data = request.get_json()
    task_id = max(tasks.keys()) + 1
    tasks[task_id] = {'title': data['title'], 'description': data['description']}
    return jsonify({'message': 'Task created successfully', 'task_id': task_id})


# Get details of a specific task
@app.route('/api/tasks/<int:task_id>/', methods=['GET'])
def get_task(task_id):
    if task_id in tasks:
        return jsonify(tasks[task_id])
    else:
        return jsonify({'error': 'Task not found'}), 404


# Update a specific task
@app.route('/api/tasks/<int:task_id>/', methods=['PUT'])
def update_task(task_id):
    if task_id in tasks:
        data = request.get_json()
        tasks[task_id]['title'] = data['title']
        tasks[task_id]['description'] = data['description']
        return jsonify({'message': 'Task updated successfully'})
    else:
        return jsonify({'error': 'Task not found'}), 404


# Delete a specific task
@app.route('/api/tasks/<int:task_id>/', methods=['DELETE'])
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'error': 'Task not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
