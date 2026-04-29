let role = localStorage.getItem("role");

if(role !== "admin"){
    addBtn.style.display = "none";
    editBtn.style.display = "none";
}

async function loadPeople(){

    const res = await fetch('/people');
    const data = await res.json();

    tableBody.innerHTML = "";

    data.forEach(p=>{

        tableBody.innerHTML += `
        <tr>
            <td>${p.id}</td>
            <td>${p.fullname}</td>
            <td>${p.position}</td>
            <td>${p.ministry}</td>
        </tr>
        `;
    });
}

loadPeople();