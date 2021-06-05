var option = document.getElementsByClassName("option")
var coption = document.getElementsByClassName("coption")
var label = document.getElementsByClassName("label")
var cname = document.getElementsByClassName("cname")
var country = document.getElementById("country")
var continent = document.getElementById("continent")

for (let i = 0; i < label.length; i++) {
    option[i].addEventListener('click', function () {
        c = label[i].innerHTML.toString()
        country.value = c
    })
}

function executeGraph() {
    eel.locaExist(country.value.trim().replace(/\s+/g, " "))
    eel.expose(checkInput)
    // eel.expose(checkEmpty)

    // function checkEmpty(empty_flag) {
    //     console.log(empty_flag)
    // }

    

    function checkInput(code) {

        if (code == 1) {
            Swal.fire({
                icon: 'success',
                title: 'Successfully',
                text: 'Plot successfully',
                showConfirmButton: false,
                timer: 1000
            })
            setTimeout(eel.plotGraph(country.value.trim().replace(/\s+/g, " "), code), 1000)
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Failed',
                text: 'Something went wrong!'
            })
        }
    }
}



for (let i = 0; i < cname.length; i++) {
    coption[i].addEventListener('click', function () {
        let cstring = cname[i].innerHTML.toString()
        continent.value = cstring
    })
}

function continentGroup() {
    if (continent.value) {
        Swal.fire({
            icon: 'success',
            title: 'Successfully',
            text: 'Plot successfully',
            showConfirmButton: false,
            timer: 1000
        })
        eel.contGroup(continent.value)
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Failed',
            text: 'Something went wrong!'
        })
    }

}




// if (empty_flag == 1)
//     setTimeout(eel.plotGraph(country.value.trim().replace(/\s+/g, " "), code), 1000)
// else
//     Swal.fire({
//         icon: 'error',
//         title: 'Failed',
//         text: 'The data of this country is empty!'
//     })