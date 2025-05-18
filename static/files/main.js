document.addEventListener("DOMContentLoaded", function () {
    const gameForm = document.querySelector("#game-form");
    const gameButton = document.querySelector("#game-button");
    const spinnerContainer = document.querySelector("#spinner-container");

    // Add an event listener for the form submission
    gameForm.addEventListener("submit", function (event) {
        // Prevent the default form submission initially
        event.preventDefault();

        // Disable the button to prevent multiple clicks
        gameButton.disabled = true;
        gameButton.textContent = "Generating...";

        const spinner = document.createElement("div");
        spinner.classList.add("spinner-border");
        spinner.classList.add("text-secondary");
        spinner.setAttribute("role", "status");

        const visuallyHidden = document.createElement("span");
        visuallyHidden.classList.add("visually-hidden");
        visuallyHidden.textContent = "Loading...";

        spinner.appendChild(visuallyHidden);

        // Clear previous content
        spinnerContainer.innerHTML = "";

        // Append the spinner to the container
        spinnerContainer.appendChild(spinner);

        gameForm.submit();
    });
});