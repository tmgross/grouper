// Get the form and username list elements
const form = document.getElementById('usernameForm');
const usernameList = document.getElementById('usernameList');

// Add an event listener to the form submission
form.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form submission

  // Get the username input value
  const usernameInput = document.getElementById('usernameInput');
  const username = usernameInput.value;

  // Create a new username element
  const usernameElement = document.createElement('div');
  usernameElement.className = 'username';
  usernameElement.textContent = username;

  // Append the username element to the username list
  usernameList.appendChild(usernameElement);

  // Clear the input field
  usernameInput.value = '';
});