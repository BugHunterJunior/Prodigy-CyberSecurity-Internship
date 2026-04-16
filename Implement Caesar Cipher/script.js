async function processText() {
    const input = document.getElementById('inputText').value;
    const shift = document.getElementById('keyInput').value;
    const output = document.getElementById('outputText');

    if (!input) {
        alert("Please enter text!");
        return;
    }

    if (!shift) {
        alert("Enter key!");
        return;
    }

    try {
        let result;

        if (currentMode === 'encrypt') {
            result = await window.pywebview.api.encrypt(input, shift);
        } else {
            result = await window.pywebview.api.decrypt(input, shift);
        }

        output.value = result;
        document.getElementById('copyBtn').style.display = 'block';

    } catch (err) {
        console.error(err);
        alert("Error processing text");
    }
}