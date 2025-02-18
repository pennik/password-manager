
window.addEventListener('load', resizePopup);
  
document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Verhindert das Neuladen der Seite
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    console.log('Benutzername:', username);
    console.log('Passwort:', password);
    
    alert(`Login erfolgreich!\nBenutzername: ${username}`);
});