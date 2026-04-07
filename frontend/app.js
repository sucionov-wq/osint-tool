const API = "http://localhost:8000";

async function checkUsername() {
    const username = document.getElementById("username").value;
    const res = await fetch(`${API}/username/${username}`);
    show(await res.json());
}

async function checkEmail() {
    const email = document.getElementById("email").value;
    const res = await fetch(`${API}/email/${email}`);
    show(await res.json());
}

async function checkDomain() {
    const domain = document.getElementById("domain").value;
    const res = await fetch(`${API}/domain/${domain}`);
    show(await res.json());
}

async function uploadImage() {
    const fileInput = document.getElementById("file");
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch(`${API}/geoint`, {
        method: "POST",
        body: formData
    });

    show(await res.json());
}

function show(data) {
    document.getElementById("result").innerText =
        JSON.stringify(data, null, 2);
}
