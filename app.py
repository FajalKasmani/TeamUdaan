from flask import Flask, render_template, request, jsonify
from agents import ComplaintResolverWorkflow
from memory import ComplaintMemory

app = Flask(__name__)

# Initialize Agents
workflow = ComplaintResolverWorkflow()
memory = ComplaintMemory()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    print("🔔 HEY! FRONTEND SE MESSAGE AAYA HAI!")
    data = request.json
    # print("🔔 MESSAGE RECEIVED FROM FRONTEND!")
    complaint_text = data.get('complaint')
    
    if not complaint_text:
        return jsonify({'error': 'No text provided'})

    # Agent Processing
    result = workflow.process_complaint(complaint_text)
    
    # Check Critical/High Logic
    p_level = result['final_priority'].lower()
    is_saved = False
    
    if p_level in ['critical', 'high']:
        memory.add_complaint(
            complaint=complaint_text, 
            category=result['category'], 
            priority=result['final_priority']
        )
        is_saved = True

    # Return JSON to Frontend
    return jsonify({
        'result': result,
        'is_saved': is_saved,
        'memory_count': memory.get_complaint_count()
    })

@app.route('/memory', methods=['GET'])
def get_memory():
    return jsonify(memory.get_all_complaints())

@app.route('/clear_memory', methods=['POST'])
def clear_memory():
    memory.clear_memory()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    # 🛠️ FIX: use_reloader=False lagaya hai taaki Windows error na aaye
    app.run(debug=True, use_reloader=False, port=5000)