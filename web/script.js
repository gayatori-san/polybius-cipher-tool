// Polybius Cipher Tool - workshop version
// Exact 5x5 Polybius square from the workshop image.
// Rows and columns are numbered 1-5.
var SQUARE = [
  ['A', 'B', 'C', 'D', 'E'],
  ['F', 'G', 'H', 'I', 'J'],
  ['K', 'L', 'M', 'N', 'O'],
  ['P', 'Q', 'R', 'S', 'T'],
  ['U', 'V', 'W', 'X', 'Y']
];

var LETTER_TO_COORD = {};
var COORD_TO_LETTER = {};

for (var r = 0; r < 5; r++) {
  for (var c = 0; c < 5; c++) {
    var coord = String(r + 1) + String(c + 1);
    LETTER_TO_COORD[SQUARE[r][c]] = coord;
    COORD_TO_LETTER[coord] = SQUARE[r][c];
  }
}

function renderSquare() {
  var el = document.getElementById('square-output');
  var html = '<div class="cell header"></div>';
  for (var i = 1; i <= 5; i++) html += '<div class="cell header">' + i + '</div>';
  for (var row = 0; row < 5; row++) {
    html += '<div class="cell row-label">' + (row + 1) + '</div>';
    for (var col = 0; col < 5; col++) html += '<div class="cell letter">' + SQUARE[row][col] + '</div>';
  }
  el.innerHTML = html;
}

function renderMappings() {
  var el = document.getElementById('mappings-output');
  var html = '';
  var letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  for (var i = 0; i < letters.length; i++) {
    var letter = letters[i];
    html += '<div class="map-item">' + letter + ' &rarr; ' + (LETTER_TO_COORD[letter] || 'no coordinate') + '</div>';
  }
  el.innerHTML = html;
}

function encrypt(text) {
  var result = [];
  var upper = text.toUpperCase();
  for (var i = 0; i < upper.length; i++) {
    var ch = upper[i];
    if (ch === 'Z') throw new Error('Z is not present in the 5x5 grid shown in the workshop.');
    result.push(LETTER_TO_COORD[ch] || ch);
  }
  return result.join(' ');
}

function encryptWithSteps(text) {
  var lines = [];
  var upper = text.toUpperCase();
  for (var i = 0; i < upper.length; i++) {
    var ch = upper[i];
    if (ch === 'Z') lines.push('Z &rarr; no coordinate');
    else if (LETTER_TO_COORD[ch]) lines.push(ch + ' &rarr; ' + LETTER_TO_COORD[ch]);
    else lines.push(ch + ' &rarr; ' + ch + ' (unchanged)');
  }
  return lines;
}

function decrypt(text) {
  if (!text.trim()) return '';
  var tokens = text.trim().split(/\s+/);
  var result = [];
  for (var i = 0; i < tokens.length; i++) {
    var token = tokens[i];
    if (!/^\d{2}$/.test(token) || !COORD_TO_LETTER[token]) {
      throw new Error('Invalid coordinate: ' + token + '. Use values from 11 to 55.');
    }
    result.push(COORD_TO_LETTER[token]);
  }
  return result.join('');
}

function showError(message) {
  var el = document.getElementById('error-msg');
  el.textContent = message;
  el.classList.remove('hidden');
}

function clearError() {
  var el = document.getElementById('error-msg');
  el.textContent = '';
  el.classList.add('hidden');
}

function handleEncrypt() {
  clearError();
  var input = document.getElementById('input-text').value;
  if (!input.trim()) return showError('Please enter some text to encrypt.');
  try {
    var result = encrypt(input);
    document.getElementById('output-text').textContent = result;
    var steps = encryptWithSteps(input);
    var html = '';
    for (var i = 0; i < steps.length; i++) html += '<div class="step-line">' + steps[i] + '</div>';
    html += '<div class="step-result">Result: ' + result + '</div>';
    document.getElementById('steps-output').innerHTML = html;
    document.getElementById('steps-section').classList.remove('hidden');
  } catch (error) { showError(error.message); }
}

function handleDecrypt() {
  clearError();
  var input = document.getElementById('input-text').value;
  if (!input.trim()) return showError('Please enter coordinates to decrypt.');
  try {
    document.getElementById('output-text').textContent = decrypt(input);
    document.getElementById('steps-section').classList.add('hidden');
  } catch (error) { showError(error.message); }
}

document.getElementById('btn-encrypt').addEventListener('click', handleEncrypt);
document.getElementById('btn-decrypt').addEventListener('click', handleDecrypt);
document.getElementById('input-text').addEventListener('keydown', function(e) {
  if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); handleEncrypt(); }
});

renderSquare();
renderMappings();
