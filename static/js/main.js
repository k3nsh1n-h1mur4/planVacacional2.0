/*const form1 = document.querySelector('#form');

form1.addEventListener('submit', async e => {
    e.preventDefault()

    const matricula =  form['matricula'].value
    const name = form['name'].value
    const adscription = form['adscription'].value
    const category = form['category'].value
    const nafil = form['nafil'].value
    const cellnumber = form['cellnumber'].value
    const address = form['address'].value

    const response = await fetch('http://localhost:5000/registro', {
        method: 'POST',
        mode: 'no-cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            matricula,
            name,
            adscription,
            category,
            nafil,
            cellnumber,
            address
        })
    })
    console.log(matricula, name, adscription)
    const data = await response.json()
    console.log(data)
}) 
*/




/*const form = document.querySelector('#form')
form.onSubmit = async e => {
    e.preventDefault()
    let response = await fetch('/registro', {
        method: 'POST',
        body: new FormData(form)
    });

    let result = await response.json()
    alert(result.message)
};
*/


/*const form = document.querySelector('#formH')
form.addEventListener('onsubmit', e => {
    e.preventDefault()
    const bdate = form['bdate'].value
    if (bdate < '2008-07-25' && bdate > '2016-07-25'){
	console.log("fecha fuera de rango")
    }
    console.log(bdate)
}) */



/*const listado_url = {{ url_for('listado')|tojson }}
fetch(listado_url)
    .then(response => response.json())
    .then(data => {
	console.log(data)
    })*/
