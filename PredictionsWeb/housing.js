const predictionURL = "http://127.0.0.1:5000/api/v1.0/prediction";
//function to validate form
function validateForm() {
    // Example starter JavaScript for disabling form submissions if there are invalid fields
    'use strict'
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
    var isValid = true;
    //var button = document.getElementById("#btnPredict");
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('click', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                    isValid = false;
                }

                form.classList.add('was-validated')
            }, false)
        })
    if (isValid) {
        collectData();
    }
}

//function to collect data from form
function collectData() {
    let bedrooms = d3.select("#inputBedrooms").node().value;
    let bathrooms = d3.select("#inputBathrooms").node().value;
    let garages = d3.select("#inputGarage").node().value;
    let landarea = d3.select("#inputLA").node().value;
    let floorarea = d3.select("#inputFA").node().value;
    let cbd = d3.select("#inputCBD").node().value;
    let schDist = d3.select("#inputNSclD").node().value;
    let schRank = d3.select("#inputNSclRank").node().value;
    let stnDist = d3.select("#inputNStnD").node().value;
    let builtYear = d3.select("#inputBYr").node().value;
    let postCode = d3.select("#inputPC").node().value;
    let lat = d3.select("#lat").node().value;
    let long = d3.select("#lon").node().value;
    d3.json(predictionURL).then(function (data) {
        prediction = data;
        showResult();
    });
}

//predict by passing values to api
function predictClick() {
    validateForm();
    //collectData();
    // Fetch the JSON data for standings


}
function showResult() {
    $('#pred').append(prediction);
    $('#exampleModal').modal('show');
}


