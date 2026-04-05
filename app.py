from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html dir="rtl">
<head>
    <title>نظام توقع النجاح في الدراسة 🤖</title>
    <meta charset="utf-8">
    <style>
        body { font-family: "Arial", sans-serif; text-align: center; margin-top: 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; min-height: 100vh; }
        .container { max-width: 500px; margin: 0 auto; padding: 20px; }
        input { padding: 20px; font-size: 24px; border: none; border-radius: 15px; width: 250px; text-align: center; margin-bottom: 20px; }
        button { padding: 20px 50px; font-size: 20px; background: #f39c12; color: white; border: none; border-radius: 15px; cursor: pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
        button:hover { background: #e67e22; }
        #result { font-size: 32px; margin-top: 30px; font-weight: bold; padding: 20px; border-radius: 15px; background: rgba(255,255,255,0.2); }
        .success { background: #27ae60 !important; }
        .fail { background: #e74c3c !important; }
        h1 { font-size: 36px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 نظام الذكاء الاصطناعي لتوقع النجاح</h1>
        <p>ادخل عدد ساعات الدراسة اليومية:</p>
        <input type="number" id="hours" placeholder="مثال: 6" min="0" step="0.1">
        <br>
        <button onclick="predict()">توقع النتيجة</button>
        <div id="result"></div>
    </div>

    <script>
        function predict() {
            const hours = parseFloat(document.getElementById('hours').value) || 0;
            fetch(`/predict?hours=${hours}`)
                .then(res => res.json())
                .then(data => {
                    const resultDiv = document.getElementById('result');
                    const pred = data.prediction;
                    const prob = (data.probability * 100).toFixed(1);
                    if (pred === 1) {
                        resultDiv.innerHTML = `✅ ناجح! احتمال النجاح: ${prob}%`;
                        resultDiv.className = 'success';
                    } else {
                        resultDiv.innerHTML = `❌ راسب! احتمال النجاح: ${prob}%`;
                        resultDiv.className = 'fail';
                    }
                })
                .catch(err => {
                    document.getElementById('result').innerHTML = 'خطأ في الاتصال!';
                });
        }
    </script>
</body>
</html>
    '''

@app.route('/predict')
def predict():
    try:
        hours_str = request.args.get('hours', '')
        hours = 0.0
        if hours_str:
            hours = float(hours_str)
    except ValueError:
        hours = 0.0
    pred = 1 if hours > 4 else 0
    prob = min(1.0, hours / 10.0)
    return jsonify({'prediction': pred, 'probability': prob})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
