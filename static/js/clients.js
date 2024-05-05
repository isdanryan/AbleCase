
//Populate 'Display Name' field on client_create.html with 'First Name' and 'Last_Name'
window.addEventListener('DOMContentLoaded', function () {
    var firstName = document.getElementById('id_first_name');
    var lastName = document.getElementById('id_last_name');
    var displayName = document.getElementById('id_display_name');

    // Event listener for input changes in 'First Name' field
    firstName.addEventListener('input', updateCombinedField);

    // Event listener for input changes in 'Last Name' field
    lastName.addEventListener('input', updateCombinedField);

    // Function to update combinedField
    function updateCombinedField() {
        displayName.value = firstName.value + ' ' + lastName.value;
    }
});