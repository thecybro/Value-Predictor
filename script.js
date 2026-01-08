function addRow() {
    const row = document.createElement("tr");
    row.innerHTML = `
        <td><input type="number"></td>
        <td><input type="number"></td>
    `;
    document.getElementById("rows").appendChild(row);
}

document.getElementById("form").addEventListener("submit", e => {
    e.preventDefault();

    const X = [];
    const Y = [];

    document.querySelectorAll("#rows tr").forEach(row => {
        const inputs = row.querySelectorAll("input");
        X.push(Number(inputs[0].value));
        Y.push(Number(inputs[1].value));
    });

    const mode = document.getElementById("mode").value;
    const value = Number(document.getElementById("value").value);

    fetch("/api/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ X, Y, mode, value })
    })
        .then(res => res.json())
        .then(data => {
            document.getElementById("output").innerText = data.result;
        });
});
