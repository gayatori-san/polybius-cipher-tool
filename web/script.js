// Polybius square — 5x5 grid with I/J combined
var SQUARE = [
  ['A', 'B', 'C', 'D', 'E'],
  ['F', 'G', 'H', 'I', 'K'],
  ['L', 'M', 'N', 'O', 'P'],
  ['Q', 'R', 'S', 'T', 'U'],
  ['V', 'W', 'X', 'Y', 'Z']
];

// Build letter-to-coordinate lookup
var LETTER_TO_COORD = {};
for (var r = 0; r < 5; r++) {
  for (var c = 0; c < 5; c++) {
    LETTER_TO_COORD[SQUARE[r][c]] = String(r + 1) + String(c + 1);
  }
}

// Render the Polybius square
function renderSquare() {
  var el = document.getElementById('square-output');
  var html = '<div class="cell header"></div>';
  for (var i = 1; i <= 5; i++) {
    html += '<div class="cell header">' + i + '</div>';
  }
  for (var r = 0; r < 5; r++) {
    html += '<div class="cell row-label">' + (r + 1) + '</div>';
    for (var c = 0; c < 5; c++) {
      var letter = SQUARE[r][c];
      var display = (letter === 'I') ? 'I/J' : letter;
      html += '<div class="cell letter">' + display + '</div>';
    }
  }
  el.innerHTML = html;
}

// Render the mappings
function renderMappings() {
  var el = document.getElementById('mappings-output');
  var html = '';
  var keys = Object.keys(LETTER_TO_COORD).sort();
  for (var i = 0; i < keys.length; i++) {
    var letter = keys[i];
    html += '<div class="map-item">' + letter + ' &rarr; ' + LETTER_TO_COORD[letter] + '</div>';
  }
  el.innerHTML = html;
}

// Encrypt plaintext into Polybius coordinates
function encrypt(text) {
  var result = [];
  var upper = text.toUpperCase();
  for (var i = 0; i < upper.length; i++) {
    var ch = upper[i];
    if (LETTER_TO_COORD[ch]) {
      result.push(LETTER_TO_COORD[ch]);
    } else {
      result.push(ch);
    }
  }
  return result.join(' ');
}

// Build step-by-step encryption
function encryptWithSteps(text) {
  var lines = [];
  var upper = text.toUpperCase();
  for (var i = 0; i < upper.length; i++) {
    var ch = upper[i];
    if (LETTER_TO_COORD[ch]) {
      lines.push(ch + ' &rarr; ' + LETTER_TO_COORD[ch]);
    } else {
      lines.push(ch + ' &rarr; ' + ch + ' (unchanged)');
    }
  }
  return lines;
}

// Decrypt Polybius coordinates back into text
function decrypt(text) {
  var result = [];
  var digits = '';
  for (var i = 0; i < text.length; i++) {
    var ch = text[i];
    if (ch >= '0' && ch <= '9') {
      digits += ch;
    } else {
      if (digits.length >= 2) {
        result.push(decryptDigits(digits));
        // Keep leftover digit if odd count
        digits = digits.length % 2 === 1 ? digits[digits.length - 1] : '';
      } else {
        digits = '';
      }
      // Spaces between digit pairs are just separators — skip them
      if (ch !== ' ' && ch !== '\t') {
        result.push(ch);
      }
    }
  }
  if (digits.length >= 2) {
    result.push(decryptDigits(digits));
  } else if (digits.length === 1) {
    result.push(digits);
  }
  return result.join('');
}

// Decrypt a string of digit pairs
function decryptDigits(digits) {
  var result = [];
  for (var i = 0; i < digits.length - 1; i += 2) {
    var row = parseInt(digits[i]) - 1;
    var col = parseInt(digits[i + 1]) - 1;
    if (row >= 0 && row < 5 && col >= 0 && col < 5) {
      result.push(SQUARE[row][col]);
    } else {
      result.push('?');
    }
  }
  return result.join('');
}

// Check if input looks like coordinates (mostly digits and spaces)
function isCoordinates(text) {
  var stripped = text.replace(/[\s,]/g, '');
  if (stripped.length === 0) return false;
  var digitCount = 0;
  for (var i = 0; i < stripped.length; i++) {
    if (stripped[i] >= '0' && stripped[i] <= '9') digitCount++;
  }
  return digitCount / stripped.length > 0.6;
}

// Show error message
function showError(msg) {
  var el = document.getElementById('error-msg');
  el.textContent = msg;
  el.classList.remove('hidden');
}

// Clear error message
function clearError() {
  var el = document.getElementById('error-msg');
  el.textContent = '';
  el.classList.add('hidden');
}

// Handle encrypt button
function handleEncrypt() {
  clearError();
  var input = document.getElementById('input-text').value;
  if (!input.trim()) {
    showError('Please enter some text to encrypt.');
    return;
  }
  var result = encrypt(input);
  document.getElementById('output-text').textContent = result;

  // Show steps
  var steps = encryptWithSteps(input);
  var stepsEl = document.getElementById('steps-output');
  var html = '';
  for (var i = 0; i < steps.length; i++) {
    html += '<div class="step-line">' + steps[i] + '</div>';
  }
  html += '<div class="step-result">Result: ' + result + '</div>';
  stepsEl.innerHTML = html;
  document.getElementById('steps-section').classList.remove('hidden');
}

// Handle decrypt button
function handleDecrypt() {
  clearError();
  var input = document.getElementById('input-text').value;
  if (!input.trim()) {
    showError('Please enter coordinates to decrypt.');
    return;
  }
  if (!isCoordinates(input)) {
    showError('Input does not look like Polybius coordinates. Enter digit pairs like "23 15 31 31 34".');
    return;
  }
  var result = decrypt(input);
  document.getElementById('output-text').textContent = result;
  document.getElementById('steps-section').classList.add('hidden');
}

// Wire up buttons
document.getElementById('btn-encrypt').addEventListener('click', handleEncrypt);
document.getElementById('btn-decrypt').addEventListener('click', handleDecrypt);

// Allow Ctrl+Enter to encrypt
document.getElementById('input-text').addEventListener('keydown', function(e) {
  if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
    e.preventDefault();
    handleEncrypt();
  }
});

// Initialize
renderSquare();
renderMappings();
