document.getElementById('loginForm').addEventListener('submit',async function(event) {
    event.preventDefault(); // Verhindert das Neuladen der Seite

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const data = {
        login_name: username,
        password: password
    };
    
    try {
        const response = await fetch("http://127.0.0.1:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });
        if (response.ok) {
            const result = await response.json();
            localStorage.setItem("token", result.token);
        } else {
            alert("Login fehlgeschlagen. Bitte überprüfe deine Eingaben.");
        }
    } catch (error) {
        console.error("Fehler beim Login:", error);
        console.log(result);
        alert("Es gab ein Problem mit der Anfrage.");
    }
});