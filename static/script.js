// Base URL for API calls
const API_BASE = window.location.origin;

// Helper function to show results
function showResult(elementId, data) {
    const resultDiv = document.getElementById(elementId);
    resultDiv.innerHTML = `
        <div class="formula">Formula: ${data.formula}</div>
        <strong>Result: ${data.result} ${data.unit}</strong><br>
        <small>Shape: ${data.shape} | Calculation: ${data.calculation}</small>
    `;
    resultDiv.style.display = 'block';
    // Hide error if showing result
    document.getElementById(elementId.replace('result', 'error')).style.display = 'none';
}

// Helper function to show errors
function showError(elementId, message) {
    const errorDiv = document.getElementById(elementId);
    errorDiv.innerHTML = `<strong>Error:</strong> ${message}`;
    errorDiv.style.display = 'block';
    // Hide result if showing error
    document.getElementById(elementId.replace('error', 'result')).style.display = 'none';
}

// Helper function to make API calls
async function makeAPICall(url, resultElementId, errorElementId) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        
        if (response.ok) {
            showResult(resultElementId, data);
        } else {
            showError(errorElementId, data.error || 'Unknown error occurred');
        }
    } catch (error) {
        showError(errorElementId, 'Failed to connect to API');
    }
}

// Circle calculations
function calculateCirclePerimeter() {
    const radius = document.getElementById('circle-radius').value;
    if (!radius || radius <= 0) {
        showError('circle-error', 'Please enter a valid positive radius');
        return;
    }
    makeAPICall(`${API_BASE}/circle/perimeter/${radius}`, 'circle-result', 'circle-error');
}

function calculateCircleArea() {
    const radius = document.getElementById('circle-radius').value;
    if (!radius || radius <= 0) {
        showError('circle-error', 'Please enter a valid positive radius');
        return;
    }
    makeAPICall(`${API_BASE}/circle/area/${radius}`, 'circle-result', 'circle-error');
}

// Rectangle calculations
function calculateRectanglePerimeter() {
    const width = document.getElementById('rect-width').value;
    const height = document.getElementById('rect-height').value;
    if (!width || !height || width <= 0 || height <= 0) {
        showError('rectangle-error', 'Please enter valid positive width and height');
        return;
    }
    makeAPICall(`${API_BASE}/rectangle/perimeter/${width}/${height}`, 'rectangle-result', 'rectangle-error');
}

function calculateRectangleArea() {
    const width = document.getElementById('rect-width').value;
    const height = document.getElementById('rect-height').value;
    if (!width || !height || width <= 0 || height <= 0) {
        showError('rectangle-error', 'Please enter valid positive width and height');
        return;
    }
    makeAPICall(`${API_BASE}/rectangle/area/${width}/${height}`, 'rectangle-result', 'rectangle-error');
}

// Triangle calculation
function calculateTriangleArea() {
    const base = document.getElementById('triangle-base').value;
    const height = document.getElementById('triangle-height').value;
    if (!base || !height || base <= 0 || height <= 0) {
        showError('triangle-error', 'Please enter valid positive base and height');
        return;
    }
    makeAPICall(`${API_BASE}/triangle/area/${base}/${height}`, 'triangle-result', 'triangle-error');
}

// Health check
async function checkHealth() {
    try {
        const response = await fetch(`${API_BASE}/health`);
        const data = await response.json();
        document.getElementById('server-status').innerHTML = `✅ ${data.message}`;
        document.getElementById('server-status').style.color = 'green';
    } catch (error) {
        document.getElementById('server-status').innerHTML = '❌ Server not responding';
        document.getElementById('server-status').style.color = 'red';
    }
}

// Check health on page load
window.onload = function() {
    checkHealth();
};

// Add Enter key support for inputs
document.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        const activeElement = document.activeElement;
        if (activeElement.id === 'circle-radius') {
            calculateCirclePerimeter();
        } else if (activeElement.id === 'rect-width' || activeElement.id === 'rect-height') {
            calculateRectangleArea();
        } else if (activeElement.id === 'triangle-base' || activeElement.id === 'triangle-height') {
            calculateTriangleArea();
        }
    }
});