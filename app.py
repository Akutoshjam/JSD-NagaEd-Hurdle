from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

courses = []
course_id_counter = 1

@app.route('/courses', methods=['POST'])
def add_course():
    global course_id_counter
    data = request.json
    new_course = {
        'id': course_id_counter,
        'title': data.get('title', ''),
        'description': data.get('description', ''),
        'duration': data.get('duration', '')
    }
    courses.append(new_course)
    course_id_counter += 1
    return jsonify(new_course), 201

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses), 200

@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.json
    for course in courses:
        if course['id'] == course_id:
            course['title'] = data.get('title', course['title'])
            course['description'] = data.get('description', course['description'])
            course['duration'] = data.get('duration', course['duration'])
            return jsonify(course), 200
    return jsonify({'error': 'Course not found'}), 404

@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    global courses
    courses = [course for course in courses if course['id'] != course_id]
    return jsonify({'message': 'Course deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
