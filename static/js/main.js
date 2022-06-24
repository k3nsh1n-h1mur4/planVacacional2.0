const form1 = document.querySelector('#formMain');

form1.addEventListener('submit', async e => {
    e.preventDefault()

    const matricula =  formMain['matricula'].value
    console.log(matricula)
    const name = formMain['name'].value
    const adscription = formMain['adscription'].value
    const category = formMain['category'].value
    const nafil = formMain['nafil'].value
    const cellnumber = formMain['cellnumber'].value
    const address = formMain['address'].value


    let data = {
        matricula: matricula,
        name: name,
        adscription:adscription,
        category: category,
        nafil: nafil,
        cellnumber: cellnumber,
        address: address
    }

    const response = await fetch('http://127.0.0.1:5000/registro', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(
            data
            /*matricula: matricula,
            name: name,
            adscription: adscription,
            category: category,
            nafil: nafil,
            cellnumber: cellnumber,
            address: address*/
        ),
    })
    console.log(matricula, name, adscription)
    const data = await response.json()
    console.log(data)
}) 





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


const form = document.querySelector('#formH')
form.addEventListener('submit', e => {
    e.preventDefault()
    
    const name = form['name'].value
    const bdate = form['bdate'].value
    const tblood = form['tblood'].value
    const allergies = form['allergies'].value


    let data1 = {
        name: name,
        bdate: bdate,
    }
    
    
    console.log(bdate)
    const date1 = new Date(bdate)
    const date2 = new Date('2008-07-25')
    const date3 = new Date('2016-07-25')
    console.log(date1)
    if (date1 < date2 || date1 > date3){
        alert("Fecha no Válida o Fuera de Rango")
    }
    
}) 



/*const listado_url = {{ url_for('listado')|tojson }}
fetch(listado_url)
    .then(response => response.json())
    .then(data => {
	console.log(data)
    })*/
