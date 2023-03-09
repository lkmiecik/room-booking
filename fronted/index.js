let navButtons = document.getElementsByTagName('ul')[1].getElementsByTagName('li')

for(let i=0; i<navButtons.length - 1; i++) {
    navButtons[i].addEventListener('mouseover', () => {
        navButtons[i].getElementsByTagName('span')[0].style.padding = '0 10px'
        navButtons[i].getElementsByTagName('span')[0].style.width = '100%'
    })

    navButtons[i].addEventListener('mouseout', () => {
        navButtons[i].getElementsByTagName('span')[0].style.padding = ''
        navButtons[i].getElementsByTagName('span')[0].style.width = ''
    })
}

document.getElementById('send').addEventListener('click', () => {
    filter()
})

function filter() {
    const filters = {
        wynajem_od: document.getElementById('wynajemod').value,
        wynajem_do: document.getElementById('wynajemdo').value,
        rzutnik: document.getElementById('projector').checked,
        audio: document.getElementById('audio').checked,
        tablica: document.getElementById('tablica').checked,
        wifi: document.getElementById('wifi').checked,
        klimatyzacja: document.getElementById('ac').checked,
        catering: document.getElementById('catering').checked,
        czy_dostepna_dla_osob_z_niepelnosprawnoscia: true,
        ilosc_osob: parseInt(document.getElementById('personNum').value)
    }

    console.log(JSON.stringify(filters))

    fetch('http://192.168.1.188:8000/api/szukaj/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(filters)
    }).then(res => res.json())
    .then(res => {
        document.getElementById('out').innerHTML = `<article><div></div></article>`
        
        console.log(res)
        if(res.available.length < 1) {
            console.error('Wystąpił problem')
            return
        } 

        for(let x=0; x<res.available.length; x++) {
            let written = false, index, index2, temp

            temp = ''

            if(res.available[x].rzutnik) {
                temp += 'Projektor, '
            }

            if(res.available[x].tablica) {
                temp += 'Tablica, '
            }

            if(res.available[x].audio) {
                temp += 'Audio, '
            }

            if(res.available[x].catering) {
                temp += 'Katering, '
            }

            if(res.available[x].wifi) {
                temp += 'WiFi, '
            }
            
            if(res.available[x].klimatyzacja) {
                temp += 'Klimatyzacja, '
            }

            temp = temp.substring(0, temp.length - 2)
            
            for(let i=0; i<document.getElementsByTagName('article').length; i++) {
                for(let j=0; j<2; j++) {
                    if(document.getElementsByTagName('article')[i].getElementsByTagName('div').length > 0) {
                        if(document.getElementsByTagName('article')[i].getElementsByTagName('div')[j].innerHTML.length < 10) {
                            let emptyDiv = document.getElementsByTagName('article')[i].getElementsByTagName('div')[j]
        
                            written = true
                            emptyDiv.setAttribute('onclick', 'send(this)')
                            emptyDiv.setAttribute('sala', res.available[x].id)
                            emptyDiv.innerHTML = `
                                <h1>${res.available[x].nazwa_sali}</h1><h3>Budynek: ${res.available[x].building.number}, Piętro: ${res.available[x].pietro}</h3><br>
                                <h2>Max osób: ${res.available[x].max_ilosc_osob}<br>Wyposażenie: ${temp}<br>Dostępna dla niepełnosprawnych: ${res.available[x].czy_dostepna_dla_osob_z_niepelnosprawnoscia ? 'TAK' : 'NIE'}</h2>
                            `
                        }
                    }
    
                    if(!written) {
                        index = i
                        index2 = j
                        break
                    }
                }
            }
    
            if(!written) {
                if(document.getElementById('out').getElementsByTagName('article').length == 0) {
                    index = -1
                }
                
                if(index2 < 1) {
                    document.getElementById('out').getElementsByTagName('article')[index].innerHTML += '<div></div>'
                    index2 = 1
                } else {
                    document.getElementById('out').innerHTML += '<article></article>'
                    document.getElementById('out').getElementsByTagName('article')[index+1].innerHTML += '<div></div>'
                    index2 = 0
                }
    
                document.getElementById('out').getElementsByTagName('article')[index].getElementsByTagName('div')[index2].setAttribute('onclick', 'send(this)')
                document.getElementById('out').getElementsByTagName('article')[index].getElementsByTagName('div')[index2].setAttribute('sala', res.available[x].id)
                document.getElementById('out').getElementsByTagName('article')[index].getElementsByTagName('div')[index2].innerHTML = `
                    <h1>${res.available[x].nazwa_sali}</h1><h3>Budynek: ${res.available[x].building.number}, Piętro: ${res.available[x].pietro}</h3><br>
                    <h2>Max osób: ${res.available[x].max_ilosc_osob}<br>Wyposażenie: ${temp}<br>Dostępna dla niepełnosprawnych: ${res.available[x].czy_dostepna_dla_osob_z_niepelnosprawnoscia ? 'TAK' : 'NIE'}</h2>
                `
            }
        }

    })
    .catch(err => {
        console.error(err)
    })
}

function send(element) {
    const filters = {
        wynajem_od: document.getElementById('wynajemod').value,
        wynajem_do: document.getElementById('wynajemdo').value,
        sala: parseInt(element.getAttribute('sala'))
    }

    console.log(JSON.stringify(filters))

    fetch('http://192.168.1.188:8000/api/wynajmij/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4MzcxNjg5LCJpYXQiOjE2NzgzNjk4ODksImp0aSI6IjI4NDM4ODZlOTBlMzQ4NWJiZjQ0ZDY2OGNmMmIxMjgxIiwidXNlcl9pZCI6MX0.j_y807NsMx7vXGiFtbmlCXHyrTYtxWJjKjgt1pfMqa'
        },
        body: JSON.stringify(filters)
    }).then(res => res.json())
    .then(res => {
        window.open(res.checkout_url)
        window.location.href = 'end.html'
    })
    .catch(err => {
        console.error(err)
    })
}