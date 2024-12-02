const togglePassword = document.getElementById('togglePassword');
const passwordInput = document.getElementById('password');

togglePassword.addEventListener('click', () => {
    // Toggle the type attribute to show or hide the password
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);

    // Toggle the icon class
    togglePassword.classList.toggle('bx-hide'); // eye icon (shows password)
    togglePassword.classList.toggle('bx-show'); // crossed eye icon (hides password)
});
