var option = document.getElementsByClassName("option")
var label = document.getElementsByClassName("label")
var country = document.getElementById("country")

for (let i = 0; i < label.length; i++) {
    option[i].addEventListener('click', function () {
        c = label[i].innerHTML.toString()
        country.value = c
    })
}





function executeGraph() {
    eel.locaExist(country.value.trim().replace(/\s+/g, " "))
    eel.expose(checkInput)

    function checkInput(a) {
        if (a == 1)
            Swal.fire({
                icon: 'success',
                title: 'Successfully',
                text: 'Plot successfully'
            })
        else {
            Swal.fire({
                icon: 'error',
                title: 'Failed',
                text: 'Something went wrong!'
            })
        }
    }
    setTimeout(eel.plotGraph(country.value.trim().replace(/\s+/g, " ")), 1000)
}

// if (country.value) {
//     eel.expose(checkInput)

//     function checkInput(a) {
//         if (a == 1)
//             eel.plotGraph(loca_trim)
//         else
//             console.log("Not exist")
//     }
// } else {
//     console.log('None data')
// }




// fetch("../country.json", {
//     headers: {
//       'Content-Type': 'application/json',
//       'Accept': 'application/json'
//     }
//   })
//   .then(response => response.json())
//   .then(data => {
//     console.log(data)
//   })