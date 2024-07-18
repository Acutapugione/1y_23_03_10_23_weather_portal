const forecast5_block = document.getElementById("forecast5");
const today_forecast_block = document.getElementById("today_forecast");
const today_forecast_btn = document.getElementById("today_forecast_btn");
const forecast5_btn = document.getElementById("forecast5_btn");
const location_input = document.querySelector("#location_input");

forecast5_btn.addEventListener("click", forecast5);
today_forecast_btn.addEventListener("click", today_forecast);



function generate_forecast_cards(json_data) {
    console.log(json_data);
    const carousel_inner = forecast5_block.querySelector(".carousel-inner");
    let i = 0;
    json_data.forEach(element => {
        const carousel_item = document.createElement("div");
        carousel_item.classList.add("carousel-item");
        if (i == 0) {
            carousel_item.classList.add("active");
        }
        i += 1;
        const card = document.createElement("div");
        card.classList.add("card");

        const card_body = document.createElement("div");
        card_body.classList.add("card-body");
        card_body.innerText = `${element.date} -> Temp: ${element.temp}`;

        card.appendChild(card_body);

        carousel_item.appendChild(card);
        carousel_inner.appendChild(carousel_item);
    });

}
function fill_today_card(json_data) {
    const humidity_span = today_forecast_block.querySelector("#humidity");
    const temp_span = today_forecast_block.querySelector("#temp");
    const pressure_span = today_forecast_block.querySelector("#pressure");
    const clouds_span = today_forecast_block.querySelector("#clouds");
    const card_header = today_forecast_block.querySelector("#card-header-content");

    humidity_span.textContent = json_data.humidity;
    temp_span.textContent = json_data.temp;
    pressure_span.textContent = json_data.pressure;
    clouds_span.textContent = json_data.clouds;
    card_header.textContent = location_input.value;
}

function today_forecast(event) {
    event.preventDefault();
    
    if (location_input.value === "") {
        return 
    }
    today_forecast_block.style.display = "inherit";
    today_forecast_block.classList.add('disabled');
    
    fetch(`/api/v2/weather/${location_input.value}`)
        .then(responce => responce.json())
        .then(data => fill_today_card(data))
}
function forecast5(event) {
    event.preventDefault();
    
    if (location_input.value === "") {
        return 
    }
    forecast5_block.style.display = "inherit";
    forecast5_block.classList.add('disabled');
    
    fetch(`/api/v2/weather/${location_input.value}/forecast`)
        .then(responce => responce.json())
        .then(data => generate_forecast_cards(data))
}