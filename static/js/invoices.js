window.addEventListener('DOMContentLoaded', function () {
    var term = document.getElementById('id_term');
    var invoiceDate = document.getElementById('id_date');
    var dateDue = document.getElementById('id_date_due');
    var vat = document.getElementById('id_vat');
    var amount = document.getElementById('id_amount');
    var totalAmount = document.getElementById('id_total_amount');

    // Event listener for input changes in 'First Name' field
    term.addEventListener('change', updateDateDueField);

    // Create event listener and function to change vat when selected

    // Function to change the date due based on the term selected
    function updateDateDueField() {
        if (term.value == "Custom") {
            dateDue.value = "YYYY-MM-DD";
        } else {
            let daysToAdd = term.value === "7 Days" ? 7 : term.value === "14 Days" ? 14 : 30;
            dateDue.value = calculateNewDate(invoiceDate.value, daysToAdd);
        }
    }
    
    // Actual function that increases the days by the required amount
    function calculateNewDate(invoiceDateValue, daysToAdd) {
        // Format the date into a date value
        let dateParts = invoiceDateValue.split("-");
        let newDate = new Date(dateParts[0], dateParts[1] - 1, dateParts[2]);

        // Add the required number of days
        newDate.setDate(newDate.getDate() + daysToAdd);

        // Set the new date back to the original format
        let year = newDate.getFullYear();
        let month = String(newDate.getMonth() + 1).padStart(2, "0");
        let day = String(newDate.getDate()).padStart(2, "0");

        return `${year}-${month}-${day}`;
    }
});