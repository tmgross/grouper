const form = document.getElementById('usernameForm');
const usernameList = document.getElementById('usernameList');
const displayAllButton = document.getElementById('displayAllButton');

form.addEventListener('submit', function(event) {
  event.preventDefault();
  const usernameInput = document.getElementById('usernameInput');
  const username = usernameInput.value;

  fetch('/usernames', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username })
  })
  .then(response => response.json())
  .then(data => {
    if (data.message) {
      const usernameElement = document.createElement('li');
      usernameElement.textContent = username;
      usernameList.appendChild(usernameElement);
      usernameInput.value = '';
    } else if (data.error) {
      console.log(data.error);
    }
  })
  .catch(error => {
    console.log('Error:', error);
  });
});

function loadUsernames() {
  fetch('/usernames')
    .then(response => response.json())
    .then(data => {
      data.forEach(username => {
        const usernameElement = document.createElement('li');
        usernameElement.textContent = username;
        usernameList.appendChild(usernameElement);
      });
    })
    .catch(error => {
      console.log('Error:', error);
    });
}

loadUsernames();

displayAllButton.addEventListener('click', function() {
  usernameList.innerHTML = ''; // Clear the existing usernames

  fetch('/usernames')
    .then(response => response.json())
    .then(data => {
      data.forEach(username => {
        const usernameElement = document.createElement('li');
        usernameElement.textContent = username;
        usernameList.appendChild(usernameElement);
      });
    })
    .catch(error => {
      console.log('Error:', error);
    });
});