
document.getElementById('upload-button').addEventListener('click', function() {
    const fileInput = document.getElementById('file-input');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/predict', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('result').innerText = 'Prediction: ' + data.prediction;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error: ' + error.message;
    });
});


