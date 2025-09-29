from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML Template (inline, single file)
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>College Admission Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #f4f6f9;
        }
        header {
            background: linear-gradient(90deg, #4A90E2, #50E3C2);
            color: white;
            padding: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
        }
        .dashboard {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 20px;
            padding: 20px;
        }
        .sidebar {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        }
        .sidebar h3 {
            margin-bottom: 15px;
        }
        .sidebar ul {
            list-style: none;
            padding: 0;
        }
        .sidebar ul li {
            margin: 10px 0;
            padding: 10px;
            background: #f1f1f1;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
        }
        .sidebar ul li:hover {
            background: #4A90E2;
            color: white;
        }
        .chatbox {
            background: white;
            border-radius: 10px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
            padding: 20px;
            display: flex;
            flex-direction: column;
            height: 70vh;
        }
        .messages {
            flex: 1;
            overflow-y: auto;
            margin-bottom: 20px;
            padding-right: 10px;
        }
        .message {
            margin: 10px 0;
            padding: 10px;
            border-radius: 8px;
            max-width: 70%;
        }
        .user {
            background: #4A90E2;
            color: white;
            align-self: flex-end;
        }
        .bot {
            background: #f1f1f1;
            align-self: flex-start;
        }
        .input-box {
            display: flex;
        }
        .input-box input {
            flex: 1;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        .input-box button {
            padding: 10px 20px;
            border: none;
            background: #4A90E2;
            color: white;
            border-radius: 8px;
            margin-left: 10px;
            cursor: pointer;
        }
        .input-box button:hover {
            background: #357ABD;
        }
    </style>
</head>
<body>
    <header>🎓 College Admission Chatbot Dashboard</header>
    <div class="dashboard">
        <div class="sidebar">
            <h3>Quick Options</h3>
            <ul>
                <li onclick="sendPredefined('Admission Process')">Admission Process</li>
                <li onclick="sendPredefined('Course Fees')">Course Fees</li>
                <li onclick="sendPredefined('Hostel Facilities')">Hostel Facilities</li>
                <li onclick="sendPredefined('Scholarships')">Scholarships</li>
                <li onclick="sendPredefined('Placement Cell')">Placement Cell</li>
            </ul>
        </div>
        <div class="chatbox">
            <div class="messages" id="messages">
                <div class="message bot">👋 Hello! I am your Admission Assistant. How can I help you today?</div>
                {% for chat in chats %}
                    <div class="message user">{{ chat[0] }}</div>
                    <div class="message bot">{{ chat[1] }}</div>
                {% endfor %}
            </div>
            <form method="POST" class="input-box">
                <input type="text" name="query" id="query" placeholder="Type your question..." required>
                <button type="submit">Send</button>
            </form>
        </div>
    </div>
    <script>
        function sendPredefined(text) {
            document.getElementById("query").value = text;
            document.forms[0].submit();
        }
    </script>
</body>
</html>
"""

# Simple Bot Responses
def bot_response(user_input):
    user_input = user_input.lower()
    if "admission" in user_input:
        return "The admission process starts in June. You need to fill out the online form and appear for counseling."
    elif "fees" in user_input:
        return "The course fees vary by program. For B.Tech it's ₹1,20,000 per year, and for MBA it's ₹1,50,000 per year."
    elif "hostel" in user_input:
        return "Yes, we provide hostel facilities with separate hostels for boys and girls. Fees: ₹50,000 per year."
    elif "scholarship" in user_input:
        return "Scholarships are available for meritorious students and those from economically weaker sections."
    elif "placement" in user_input:
        return "Our placement cell has tie-ups with top companies like Infosys, TCS, and Wipro. Placement rate: 90%."
    else:
        return "I am not sure about that. Please contact the admission office for detailed info."

chats = []

@app.route("/", methods=["GET", "POST"])
def home():
    global chats
    if request.method == "POST":
        user_query = request.form["query"]
        reply = bot_response(user_query)
        chats.append((user_query, reply))
    return render_template_string(template, chats=chats)

if __name__ == "__main__":
    app.run(debug=True)
