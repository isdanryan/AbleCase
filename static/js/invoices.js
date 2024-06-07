window.addEventListener('DOMContentLoaded', function () {
    var term = document.getElementById('id_term');
    var invoiceDate = document.getElementById('id_date');
    var dateDue = document.getElementById('id_date_due');
    var vat = document.getElementById('id_vat');
    var amount = document.getElementById('id_amount');
    var totalAmount = document.getElementById('id_total_due');

    // Event listener for changes in 'Term' field
    term.addEventListener('change', updateDateDueField);
    // Event listenr for changes in 'VAT' field
    vat.addEventListener('change', updateTotalAmountField);
    // Event listenr for changes in 'Amount' field
    amount.addEventListener('input', updateTotalAmountField);
    amount.addEventListener('focusout', () => {
        changeToDecimal(amount.value) });

    // Function to change the date due based on the term selected
    function updateDateDueField() {
        if (term.value == "Custom") {
            dateDue.value = "YYYY-MM-DD";
        } else {
            let daysToAdd = term.value === "On Receipt" ? 0 : term.value === "7 Days" ? 7 : term.value === "14 Days" ? 14 : 30;
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

    // Function to change the amount due based on the vat selected
    function updateTotalAmountField() {
        let amountToAdd = vat.value === "ZERO" ? 0 : vat.value === "10%" ? 0.1 : vat.value === "15%" ? 0.15 : 0.2;
        console.log(amount.value)
        totalAmount.value = calculateTotalAmount(amount.value, amountToAdd);
    }
    
    // Actual function that that carrys out the calculation
    function calculateTotalAmount(amountValue, amountToAdd) {
        // Format the string into floats to work with
        amountValue = parseFloat(amountValue);
        amountToAdd = parseFloat(amountToAdd)
        // Add value to calculated post vat value, then round to 2 decimal places
        let newAmount = parseFloat((amountValue * amountToAdd) + amountValue).toFixed(2);
        return newAmount;
    }

    // Function to make sure the amount value always show a 2 decimal value
    function changeToDecimal(value) {
        let decimalValue = parseFloat(value).toFixed(2);
        amount.value = decimalValue;
    }
});