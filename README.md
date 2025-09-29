
# 🎓 College Admission Chatbot

A simple and interactive web-based chatbot built with Flask to assist prospective students with college admission queries. The chatbot provides instant responses to common questions about admission processes, fees, hostel facilities, scholarships, and placements.

## ✨ Features

- **Interactive Chat Interface**: Clean and modern UI with a conversational chatbot
- **Quick Options Sidebar**: Pre-defined buttons for common queries
- **Real-time Responses**: Instant answers to admission-related questions
- **Responsive Design**: Works seamlessly across different screen sizes
- **Easy to Deploy**: Single-file Flask application with inline HTML/CSS

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask library

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd college-admission-chatbot
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python chatbot.py
   ```

4. **Open your browser**
   Navigate to `http://127.0.0.1:5000/`

## 📋 Usage

### Asking Questions

You can interact with the chatbot in two ways:

1. **Type your question** in the input box at the bottom
2. **Click quick options** in the sidebar for instant queries

### Supported Topics

The chatbot can answer questions about:

- **Admission Process**: Timeline and requirements
- **Course Fees**: Fee structure for different programs
- **Hostel Facilities**: Accommodation options and costs
- **Scholarships**: Available financial aid programs
- **Placement Cell**: Career opportunities and company partnerships

## 🛠️ Customization

### Adding More Responses

Edit the `bot_response()` function in `chatbot.py`:

```python
def bot_response(user_input):
    user_input = user_input.lower()
    if "your_keyword" in user_input:
        return "Your custom response here"
    # Add more conditions as needed
```

### Modifying Quick Options

Update the sidebar section in the HTML template:

```html
<li onclick="sendPredefined('Your Topic')">Your Topic</li>
```

### Styling Changes

Modify the `<style>` section in the template to customize colors, fonts, and layout.

## 📁 Project Structure

```
college-admission-chatbot/
│
├── chatbot.py          # Main Flask application
└── README.md           # Project documentation
```

## 🔧 Technical Details

- **Framework**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Template Engine**: Jinja2 (Flask's default)
- **Architecture**: Single-page application with server-side rendering

## 🎯 Future Enhancements

- [ ] Add database integration for persistent chat history
- [ ] Implement natural language processing (NLP) for better understanding
- [ ] Add user authentication system
- [ ] Create admin panel for updating responses
- [ ] Add file upload functionality for documents
- [ ] Integrate with college database for real-time information
- [ ] Add multilingual support

## ⚠️ Limitations

- Responses are keyword-based and may not understand complex queries
- Chat history is stored in memory and resets on server restart
- No user session management (all users share the same chat)

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
## 👥 Authors

- **Trupti Savale** - Project Developer

## 🏢 Supported By

**NEWGEN TECH** - Technology Partner and Support
  For questions or support, please contact:
- Developer: Trupti Savale
- Project Link: [https://github.com/truptisavale/college-admission-chatbot](https://github.com/truptisavale/college-admission-chatbot)

## 🙏 Acknowledgments

- NEWGEN TECH for their continuous support and guidance
- Flask documentation and community
- Inspiration from modern chatbot interfaces
- All contributors and testers

---

**Note**: This is a basic implementation intended for educational purposes. For production use, consider implementing proper security measures, database integration, and advanced NLP capabilities.
