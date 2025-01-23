let url = "https://used-car-price-ml-prediction.onrender.com/predict"

form = document.getElementById("CarDetails");
price = document.getElementsByClassName("price")[0]
predicted_tag = document.getElementById("predicted_tag")

form.addEventListener("submit", (e) => {
    e.preventDefault();

   formData = new FormData(e.target)
   formDataObject = Object.fromEntries(formData)

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formDataObject)
    })
    .then(res => res.json())
    .then((data) => {
        
        price.innerHTML = "₹" + (data["price"] * 1000)
        predicted_tag.classList.remove("hidden")
        predicted_tag.classList.add("flex")
        
    })
    .catch(error => console.log("Error", error))
   
});