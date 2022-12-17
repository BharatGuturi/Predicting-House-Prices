const predictionURL = "http://127.0.0.1:5000/api/v1.0/housePred";

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
  // d3.json(predictionURL).then(function (data) {
  //      prediction = data;
  //      showResult();
  // });

  d3.json(predictionURL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      "br": bedrooms,
      "bath": bathrooms,
      "gar": garages,
      "la": landarea,
      "fa": floorarea,
      'cb': cbd,
      "sdist": schDist,
      "sRank": schRank,
      "stnDis": stnDist,
      "by": builtYear,
      "pc": postCode,
      "latitude": lat,
      "longitude": long
    }),
  }).then(function (data) {
    prediction = data;
    showResult();
  });

}



//predict by passing values to api
function predictClick(e) {
  var form = document.querySelector(".needs-validation");
  if (form.checkValidity()) {
    collectData();
  } else {
    form.classList.add("was-validated");
  }
}
function showResult() {
  $("#pred").text("");
  $("#pred").append(prediction);
  $("#exampleModal").modal("show");
}
