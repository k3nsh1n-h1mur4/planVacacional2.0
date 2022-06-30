/*const form1 = document.querySelector('#formMain');

form1.addEventListener('submit', async e => {
    e.preventDefault()

    const matricula =  formMain['matricula'].value
    const name = formMain['name'].value
    const adscription = formMain['adscription'].value
    const category = formMain['category'].value
    const nafil = formMain['nafil'].value
    const cellnumber = formMain['cellnumber'].value
    const address = formMain['address'].value
   
    let data = {
        matricula: matricula,
        name: name,
        adscription: adscription,
        nafil: nafil,
        cellnumber: cellnumber,
        address: address
    }

    const response = await fetch('/registro', {
        method: 'POST',
        //mode: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        mode: 'cors',
        body: JSON.stringify(
            data
        ),
    })
    console.log(matricula, name, adscription)
    const data1 = await response.json()
    console.log(data)
}) */



/*const form1 = document.querySelector('#form')
form1.addEventListener('submit', e => {
    e.preventDefault()
    window.addEventListener('DOMContentLoaded', () => {

    })
})*/








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
form.addEventListener('submit', e => {
    e.preventDefault()
    const bdate = form['bdate'].value
    console.log(bdate)
    const date1 = new Date(bdate)
    const date2 = new Date('2008-07-25')
    const date3 = new Date('2016-07-25')
    console.log(date1)
    if (date1 < date2 || date1 > date3){
        alert("Fecha no Válida o Fuera de Rango")
    }
    else{
        pass
    }
}) 
*/


/*const listado_url = {{ url_for('listado')|tojson }}
fetch(listado_url)
    .then(response => response.json())
    .then(data => {
	console.log(data)
    })*/
