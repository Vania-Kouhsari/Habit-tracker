// Show the popup when the + button is clicked
document.getElementById('add-habit-btn').addEventListener('click', function() {
    document.getElementById('habit-popup').style.display = 'block';
});

// Close the popup when the close button (x) is clicked
document.getElementById('close-popup').addEventListener('click', function() {
    document.getElementById('habit-popup').style.display = 'none';
});

// Close the popup if clicked outside of the popup content
window.onclick = function(event) {
    if (event.target == document.getElementById('habit-popup')) {
        document.getElementById('habit-popup').style.display = 'none';
    }
};