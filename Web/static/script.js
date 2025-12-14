
const tools = ['encoding', 'encryption', 'hashing'];
const toolButtons = {
    encoding: document.getElementById('encoding_button'),
    encryption: document.getElementById('encryption_button'),
    hashing: document.getElementById('hashing_button')
};
const optionSections = {
    encoding: document.getElementById('encoding_options'),
    encryption: document.getElementById('encryption_options'),
    hashing: document.getElementById('hashing_options')
};
const encodeBtn = document.getElementById('encode_btn');
const decodeBtn = document.getElementById('decode_btn');
const inputText = document.getElementById('input_text');
const outputText = document.getElementById('output_text');
const outputArea = document.getElementById('output_area');
const submitBtn = document.getElementById('submit_btn');
const resultDescription = document.getElementById('result_description');

// Initialize
let activeTool = 'encoding';
let activeMode = 'encode';

function switchTool(tool) {
    activeTool = tool;
    tools.forEach(t => {
        toolButtons[t].classList.toggle('active', t === tool);
        optionSections[t].style.display = t === tool ? 'block' : 'none';
    });
    resultDescription.textContent = `You are using ${tool.charAt(0).toUpperCase() + tool.slice(1)} tool.`;
    outputArea.style.display = 'none';
}

function switchMode(mode) {
    activeMode = mode;
    encodeBtn.classList.toggle('active', mode === 'encode');
    decodeBtn.classList.toggle('active', mode === 'decode');
    outputArea.style.display = 'none';
}

// Event listeners for tools
toolButtons.encoding.addEventListener('click', () => switchTool('encoding'));
toolButtons.encryption.addEventListener('click', () => switchTool('encryption'));
toolButtons.hashing.addEventListener('click', () => switchTool('hashing'));

// Event listeners for encode/decode
encodeBtn.addEventListener('click', () => switchMode('encode'));
decodeBtn.addEventListener('click', () => switchMode('decode'));

// Event listener for submit button
submitBtn.addEventListener('click', async () => {
    const payload = {
        tool: activeTool,
        mode: activeMode,
        input: inputText.value,
        option: document.querySelector(`#${activeTool}_options input[type='radio']:checked`)?.value || ''
    };

    const response = await fetch('/process', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
    });

    const data = await response.json();
    outputText.value = data.result;
    outputArea.style.display = 'block';
});