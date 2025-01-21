let url = "http://127.0.0.1:5005/predict"

form = document.getElementById("CarDetails");
price = document.getElementsByClassName("price")[0]
predicted_tag = document.getElementById("predicted_tag")

form.addEventListener("submit", (e) => {
    e.preventDefault();

   formData = new FormData(e.target)
   formDataObject = Object.fromEntries(formData)
   
   console.log(formDataObject);

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formDataObject)
    })
    .then(res => res.json())
    .then((data) => {
        console.log(data);
        console.log(data["price"]);
        
        price.innerHTML = data["price"].toString()
        predicted_tag.classList.remove("hidden")
        predicted_tag.classList.add("flex")

        
    })
    .catch(error => console.log("Error", error))
   
});