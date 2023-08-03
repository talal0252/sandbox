const pythonCode = 
`import random

a = random.randint(1, 10)
b = random.randint(2, 5)

def get_question_data(a, b):
    correct_answer = (a + b) * 2 ** 3
    question_data = {
        "question": f"What is value of ({a} + {b} * 2 ^ 3)",
        "correct_answer": correct_answer
        }
    question_data["incorrect_answers"] = [correct_answer + 1, correct_answer - 1, correct_answer + 2]
    return question_data

__sandbox_result__ = get_question_data(a, b)
`;

fetch('http://127.0.0.1:5000/execute_python', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ python_code: pythonCode })
})
.then(response => response.json())
.then(data => {
    if ('error' in data) {
        console.log('Error: ' + data.error);
    } else {
        console.log('Result: ' + JSON.stringify(data.result));
    }
})
.catch(error => {
    console.log('Error: ' + error.message);
});
