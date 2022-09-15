let individualForms = document.querySelector(".individual_button_container");
let companyForms = document.querySelector(".company_button_container");

function companyBlock() {
    document.querySelector(".company_button_container").style.display = "flex";
    document.querySelector(".individual_button_container").style.display = "none";
};
function individualBlock() {
    document.querySelector(".individual_button_container").style.display = "flex";
    document.querySelector(".company_button_container").style.display = "none";
};
